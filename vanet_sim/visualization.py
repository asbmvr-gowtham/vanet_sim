import matplotlib.pyplot as plt
import pandas as pd

def plot_hash_times(hash_df):
    hash_df.boxplot(column="time", by="hash_type", showmeans=True)
    plt.title("Hash Generation Times")
    plt.ylabel("Time (s)")
    plt.xlabel("Hash Function")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_speeds(vehicles, num_steps, dt):
    speeds = {v.id: [] for v in vehicles}
    times = list(range(num_steps))
    for _ in times:
        for v in vehicles:
            v.move(dt)
            speeds[v.id].append(v.speed)
    pd.DataFrame(speeds, index=times).plot(figsize=(10, 5), title="Vehicle Speeds Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Speed")
    plt.show()

def plot_positions(vehicles, num_steps, dt):
    positions = {v.id: [] for v in vehicles}
    for _ in range(num_steps):
        for v in vehicles:
            v.move(dt)
            positions[v.id].append(v.position)
    for v_id, pos_list in positions.items():
        xs, ys = zip(*pos_list)
        plt.plot(xs, ys, label=f"Vehicle {v_id}")
    plt.legend()
    plt.title("Vehicle Positions Over Time")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.grid(True)
    plt.show()
