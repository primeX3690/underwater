


// firmware/src/network/time_sync.rs

pub struct UnderwaterClock {
    local_ticks: u64,
    offset_nanos: i64,
}

impl UnderwaterClock {
    pub fn new() -> Self {
        Self {
            local_ticks: 0,
            offset_nanos: 0,
        }
    }

    /// ध्वनि की गति (1500 m/s) के आधार पर पैकेट डिले कैलिब्रेट करना
    pub fn calibrate_sync_packet(&mut self, t1: u64, t2: u64, t3: u64, t4: u64, sound_speed_mps: f32) {
        let rtt = (t4 - t1).saturating_sub(t3 - t2);
        let propagation_delay = rtt / 2;
        
        self.offset_nanos = ((t2 as i64 - t1 as i64) - (t4 as i64 - t3 as i64)) / 2;
        let estimated_distance = (propagation_delay as f32) * sound_speed_mps;
        
        println!("[TimeSync] Clock synced. Offset: {} ns | Prop. Distance: {:.2} meters", self.offset_nanos, estimated_distance);
    }

    pub fn get_synchronized_timestamp(&self) -> u64 {
        (self.local_ticks as i64 + self.offset_nanos).max(0) as u64
    }
}