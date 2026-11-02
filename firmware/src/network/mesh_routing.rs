// firmware/src/network/mesh_routing.rs
use heapless::Vec;

#[derive(Clone, Copy, Debug, PartialEq)]
pub struct NodeRoute {
    pub neighbor_id: u32,
    pub hop_count: u8,
    pub link_quality: f32, // SNR (Signal-to-Noise Ratio)
}

pub struct MeshNetworkTable {
    pub node_id: u32,
    routes: Vec<NodeRoute, 32>, // अधिकतम 32 पास के नोड्स की टेबल
}

impl MeshNetworkTable {
    pub fn new(node_id: u32) -> Self {
        Self {
            node_id,
            routes: Vec::new(),
        }
    }

    /// नए पड़ोसी नोड को जोड़ना या अपडेट करना
    pub fn update_route(&mut self, neighbor_id: u32, hop_count: u8, link_quality: f32) {
        if let Some(pos) = self.routes.iter().position(|r| r.neighbor_id == neighbor_id) {
            self.routes[pos] = NodeRoute { neighbor_id, hop_count, link_quality };
        } else {
            let _ = self.routes.push(NodeRoute { neighbor_id, hop_count, link_quality });
        }
    }

    /// यदि कोई नोड तबाह हो जाए, तो उसे राउटिंग टेबल से हटाना (Self-Healing Trigger)
    pub fn handle_node_failure(&mut self, failed_node_id: u32) {
        println!("[Mesh Warning] Node #{} stopped responding. Initiating Self-Healing Route Reconfiguration...", failed_node_id);
        self.routes.retain(|r| r.neighbor_id != failed_node_id);
    }

    /// सबसे बेस्ट और कम हॉप वाले नेक्स्ट-हॉप नोड को चुनना
    pub fn get_optimal_next_hop(&self) -> Option<u32> {
        self.routes
            .iter()
            .min_by_key(|r| r.hop_count)
            .map(|r| r.neighbor_id)
    }
}