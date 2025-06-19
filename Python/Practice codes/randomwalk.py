import random
import matplotlib.pyplot as plt

num_steps = 1000

pos = 0
positions = [pos]

for _ in range(num_steps):
    x = random.choice([-1, 1])
    pos += x
    positions.append(pos)

plt.plot(positions,label="Random Walk simulation")
plt.xlabel("Number of steps")
plt.ylabel("Position")
plt.legend()
plt.grid(True)
plt.show()
