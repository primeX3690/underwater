// firmware/src/sensors/six_dof_kinematics.rs
// 6-DOF (Six Degrees of Freedom) Kinematics & Hydrodynamic State Estimator for Underwater UUVs

pub struct SixDofState {
    // Linear Motion (Position in meters: X=Surge, Y=Sway, Z=Heave)
    pub position: [f32; 3],
    // Linear Velocities (m/s)
    pub velocity: [f32; 3],
    // Angular Orientation (Euler Angles in radians: Roll, Pitch, Yaw)
    pub orientation: [f32; 3],
    // Angular Velocities (rad/s)
    pub angular_velocity: [f32; 3],
}

impl SixDofState {
    pub fn new() -> Self {
        Self {
            position: [0.0, 0.0, -1500.0], // Seabed depth at 1500 meters
            velocity: [0.0, 0.0, 0.0],
            orientation: [0.0, 0.0, 0.0],
            angular_velocity: [0.0, 0.0, 0.0],
        }
    }

    /// Update 6-DOF hydrodynamics given external currents, buoyancy, and MHD thrust forces
    pub fn update_kinematics(&mut self, mhd_thrust_n: f32, current_vector: [f32; 3], dt_seconds: f32) {
        // 1. Hydrodynamic Drag & Current forces (Surge, Sway, Heave)
        let drag_coefficient = 0.85;
        let surge_force = mhd_thrust_n - (drag_coefficient * (self.velocity[0] - current_vector[0]).powi(2));
        let sway_force = -drag_coefficient * (self.velocity[1] - current_vector[1]).powi(2);
        let heave_force = -drag_coefficient * (self.velocity[2] - current_vector[2]).powi(2);

        // 2. Linear Acceleration calculation (Mass = 45 kg micro-UUV)
        let mass = 45.0;
        let accel = [surge_force / mass, sway_force / mass, heave_force / mass];

        // 3. Integrate Linear Kinematics
        for i in 0..3 {
            self.velocity[i] += accel[i] * dt_seconds;
            self.position[i] += self.velocity[i] * dt_seconds;
        }

        // 4. Rotational Stabilization (Roll, Pitch, Yaw damping)
        self.angular_velocity[0] *= 0.95; // Roll damping
        self.angular_velocity[1] *= 0.95; // Pitch damping
        self.angular_velocity[2] *= 0.98; // Yaw stabilization

        for i in 0..3 {
            self.orientation[i] += self.angular_velocity[i] * dt_seconds;
        }
    }
}