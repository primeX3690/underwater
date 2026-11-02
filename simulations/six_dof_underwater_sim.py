# simulations/six_dof_underwater_sim.py
import numpy as np

class SixDOFUnderwaterSimulator:
    """
    6-DOF (Surge, Sway, Heave, Roll, Pitch, Yaw) Underwater Hydrodynamic Simulator
    Models UUV trajectory under deep-sea currents, buoyancy gradients, and MHD thrust.
    """
    def __init__(self, mass_kg=45.0, simulation_time_sec=10.0, dt=0.01):
        self.mass = mass_kg
        self.time = simulation_time_sec
        self.dt = dt
        
        # State vector: [x, y, z, u, v, w, phi, theta, psi, p, q, r]
        # Pos (x,y,z), LinVel (u,v,w), Euler (phi,theta,psi), AngVel (p,q,r)
        self.state = np.zeros(12)
        self.state[2] = -1500.0 # Seafloor depth in meters

    def step(self, mhd_thrust_n, ocean_current_vector):
        u, v, w = self.state[3:6]
        phi, theta, psi = self.state[6:9]
        
        # Hydrodynamic forces (Damping & Added Mass)
        X_u = -0.85 * (u - ocean_current_vector[0])
        Y_v = -0.85 * (v - ocean_current_vector[1])
        Z_w = -0.85 * (w - ocean_current_vector[2])
        
        # Total force along body axes
        F_surge = mhd_thrust_n + X_u
        F_sway = Y_v
        F_heave = Z_w
        
        # Acceleration
        a_x = F_surge / self.mass
        a_y = F_sway / self.mass
        a_z = F_heave / self.mass
        
        # Integrate linear motion
        self.state[3:6] += np.array([a_x, a_y, a_z]) * self.dt
        self.state[0:3] += self.state[3:6] * self.dt
        
        # Angular restoration (Righting moment from metacenter)
        restoring_torque_pitch = -2.5 * theta
        restoring_torque_roll = -3.0 * phi
        
        self.state[9:12] += np.array([restoring_torque_roll, restoring_torque_pitch, 0.0]) * self.dt
        self.state[6:9] += self.state[9:12] * self.dt
        
        return self.state

    def run_6dof_simulation(self, thrust=15.0, current=[0.3, 0.1, -0.05]):
        steps = int(self.time / self.dt)
        print(f"[6-DOF Sim] Simulating {self.time}s trajectory with MHD Thrust={thrust}N and Current={current} m/s...")
        
        for _ in range(steps):
            state = self.step(thrust, current)
            
        print(f"[Results] Final 6-DOF State:")
        print(f"  - Position (Surge, Sway, Heave): [{state[0]:.2f}m, {state[1]:.2f}m, {state[2]:.2f}m]")
        print(f"  - Velocity: [{state[3]:.2f}m/s, {state[4]:.2f}m/s, {state[5]:.2f}m/s]")
        print(f"  - Orientation (Roll, Pitch, Yaw): [{np.degrees(state[6]):.2f}°, {np.degrees(state[7]):.2f}°, {np.degrees(state[8]):.2f}°]")

if __name__ == "__main__":
    sim = SixDOFUnderwaterSimulator()
    sim.run_6dof_simulation()