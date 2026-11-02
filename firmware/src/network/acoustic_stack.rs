// firmware/src/network/acoustic_stack.rs
use heapless::Vec;

pub const MAX_ACOUSTIC_PAYLOAD: usize = 64; // बाइट्स (कम बैंडविड्थ के कारण पैकेट छोटा होता है)

pub struct AcousticPacket {
    pub sender_id: u32,
    pub threat_code: u8,
    pub timestamp: u64,
    pub payload: Vec<u8, MAX_ACOUSTIC_PAYLOAD>,
}

impl AcousticPacket {
    pub fn new(sender_id: u32, threat_code: u8, timestamp: u64, data: &[u8]) -> Self {
        let mut payload = Vec::new();
        payload.extend_from_slice(data).unwrap_or_default();

        Self {
            sender_id,
            threat_code,
            timestamp,
            payload,
        }
    }

    /// पैकेट को बाइट्स में बदलना (Serialization for Acoustic Transducer)
    pub fn serialize(&self) -> Vec<u8, 128> {
        let mut bytes = Vec::new();
        let _ = bytes.extend_from_slice(&self.sender_id.to_be_bytes());
        let _ = bytes.push(self.threat_code);
        let _ = bytes.extend_from_slice(&self.timestamp.to_be_bytes());
        let _ = bytes.extend_from_slice(&self.payload);
        bytes
    }
}