// firmware/src/kernel/scheduler.rs
pub struct TaskScheduler {
    tick_counter: u64,
}

impl TaskScheduler {
    pub fn new() -> Self {
        Self { tick_counter: 0 }
    }

    pub fn tick(&mut self) {
        self.tick_counter = self.tick_counter.wrapping_add(1);
    }
}