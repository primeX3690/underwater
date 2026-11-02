# simulations/hitl_socket_bridge.py
import socket
import struct
import random
import time

class HITLBridgeServer:
    def __init__(self, host='127.0.0.1', port=8080):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((host, port))
        print(f"[HITL Bridge] Active on {host}:{port} - Simulating Indian Ocean Hydrodynamics...")

    def generate_virtual_telemetry(self):
        # हाइड्रोस्टेटिक प्रेशर (Bar) और नकली सोनार नॉइज़ सिग्नेचर
        hydrostatic_pressure = random.uniform(400.0, 450.0) # 4000 meters depth equivalent
        enemy_propeller_freq = random.choice([0.0, 0.0, 1.0]) # 1.0 means propeller detected
        return struct.pack("!ff", hydrostatic_pressure, enemy_propeller_freq)

    def start_bridge(self):
        while True:
            try:
                data, addr = self.server_socket.recvfrom(1024)
                # फर्मवेयर से डेटा मिलने पर वर्चुअल सेंसर फीडबैक भेजना
                payload = self.generate_virtual_telemetry()
                self.server_socket.sendto(payload, addr)
                time.sleep(0.05)
            except KeyboardInterrupt:
                print("[HITL] Bridge terminated safely.")
                break

if __name__ == "__main__":
    bridge = HITLBridgeServer()
    bridge.start_bridge()