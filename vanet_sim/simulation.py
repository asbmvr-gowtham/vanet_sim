import pandas as pd
from vanet_sim.vehicle import Vehicle

def simulate(vehicles, dt, num_steps):
    import time
    hash_times = {algo: [] for algo in ['sha256', 'md5', 'sha1', 'blake2b', 'sha3_256']}
    for _ in range(num_steps):
        for vehicle in vehicles:
            vehicle.move(dt)
            collisions = [other for other in vehicles if vehicle != other and vehicle.check_collision(other)]
            if collisions:
                print(f"Collision detected between vehicle {vehicle.id} and: {', '.join(other.id for other in collisions)}")

            message, hashes = vehicle.generate_message()
            for other in vehicles:
                if hasattr(other, 'receive_message'):
                    other.receive_message(message.copy(), hashes.copy())

            for algo in hash_times:
                hash_times[algo].append(hashes[f"{algo}_time"])

    return pd.DataFrame([
        {"hash_type": algo, "time": t}
        for algo, times in hash_times.items()
        for t in times
    ])
