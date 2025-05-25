import random
import hashlib
import time

class Vehicle:
    def __init__(self, vehicle_id, speed, position):
        self.id = vehicle_id
        self.speed = speed
        self.position = position
        self.salt = "vanet" + str(random.random())

    def move(self, dt):
        self.position = (
            self.position[0] + self.speed * dt * random.uniform(-0.1, 1.1),
            self.position[1] + self.speed * dt * random.uniform(-0.1, 1.1),
        )

    def check_collision(self, other, threshold=1):
        distance = ((self.position[0] - other.position[0]) ** 2 +
                    (self.position[1] - other.position[1]) ** 2) ** 0.5
        return distance < threshold

    def generate_message(self):
        message = {
            "vehicle_id": self.id,
            "speed": self.speed,
            "position": self.position,
        }
        return message, self.hash_message(message)

    def hash_message(self, message):
        message_bytes = str(message).encode()
        hashes = {}
        for algo in ['sha256', 'md5', 'sha1', 'blake2b', 'sha3_256']:
            start_time = time.time()
            digest = getattr(hashlib, algo)(message_bytes + self.salt.encode()).hexdigest()
            hashes[algo] = digest
            hashes[f"{algo}_time"] = time.time() - start_time
        return hashes

    def check_integrity(self, message, hashes):
        expected_hashes = self.hash_message(message)
        for algo in ['sha256', 'md5', 'sha1', 'blake2b', 'sha3_256']:
            if expected_hashes[algo] != hashes.get(algo):
                return False
        return True

    def receive_message(self, message, hashes):
        print(f"\nVehicle {self.id} received message from {message['vehicle_id']}: {message}")
        if self.check_integrity(message, hashes):
            print("✔️ Message integrity is valid.")
        else:
            print("❌ Message integrity is NOT valid!")
