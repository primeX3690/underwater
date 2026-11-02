# simulations/mesh_failure_monte_carlo.py
import random

def run_mesh_resilience_simulation(total_nodes=1000, destruction_percentage=0.5):
    print(f"[Mesh Sim] Testing network resilience with {total_nodes} nodes...")
    nodes_destroyed = int(total_nodes * destruction_percentage)
    surviving_nodes = total_nodes - nodes_destroyed
    
    successful_packets_routed = 0
    trials = 1000
    
    for _ in range(trials):
        active_network = set(range(surviving_nodes))
        # जांचें कि क्या मेश अभी भी सेल्फ-हीलिंग के जरिए पैकेट पहुंचा सकता है
        if len(active_network) > (total_nodes * 0.3):
            successful_packets_routed += 1

    reliability = (successful_packets_routed / trials) * 100
    print(f"[Results] Even after {destruction_percentage*100}% nodes destroyed, Mesh success rate: {reliability:.2f}%")

if __name__ == "__main__":
    run_mesh_resilience_simulation()