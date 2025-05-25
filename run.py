from vanet_sim.vehicle import Vehicle
from vanet_sim.simulation import simulate
from vanet_sim.visualization import plot_hash_times, plot_speeds, plot_positions

v1 = Vehicle("V1", 65, (0, 0))
v2 = Vehicle("V2", 50, (10, 20))
v3 = Vehicle("V3", 35, (30, 50))
v4 = Vehicle("V4", 20, (10, 50))

# Tamper Test
message, hashes = v1.generate_message()
v2.receive_message(message, hashes.copy())
tampered_message = message.copy()
tampered_message["speed"] = 999
v2.receive_message(tampered_message, hashes.copy())

# Simulate and plot
df = simulate([v1, v2], 0.1, 500)
plot_hash_times(df)
plot_speeds([v1, v2], 100, 0.1)
plot_positions([v1, v2], 100, 0.1)
