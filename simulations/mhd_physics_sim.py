# simulations/mhd_physics_sim.py
import numpy as np

def calculate_lorentz_thrust(magnetic_field_t, current_a, channel_length_m):
    # F = I * (L x B) -> मैग्नेटोहाइड्रोडायनामिक थ्रस्ट कैलकुलेशन
    force = current_a * channel_length_m * magnetic_field_t
    return force

if __name__ == "__main__":
    b_field = 5.0  # Tesla
    current = 15.0 # Amps
    length = 0.5   # Meters
    thrust = calculate_lorentz_thrust(b_field, current, length)
    print(f"[MHD Physics] Generated Silent Electromagnetic Thrust: {thrust:.2f} Newtons")