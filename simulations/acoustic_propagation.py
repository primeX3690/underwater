# simulations/acoustic_propagation.py
import numpy as np

def simulate_sound_speed_profile(depth_meters):
    # सोनार ध्वनि की गति तापमान, लवणता और दबाव के साथ बदलती है (Sound Speed Profile / SOFAR Channel)
    temperature = 15.0 - (depth_meters / 200.0)
    salinity = 35.0
    pressure = depth_meters / 10.0
    
    # कोप्प-रशेल इक्वेशन का संक्षिप्त रूप
    sound_speed = 1449.2 + (4.6 * temperature) - (0.055 * temperature**2) + (0.00029 * temperature**3) + (1.34 - 0.01 * temperature) * (salinity - 35.0) + (0.016 * pressure)
    return sound_speed

if __name__ == "__main__":
    depth = 1500 # 1500 meters deep ocean floor
    speed = simulate_sound_speed_profile(depth)
    print(f"[Acoustic Physics] Speed of sound at depth {depth}m: {speed:.2f} m/s")