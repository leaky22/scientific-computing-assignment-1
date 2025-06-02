
Assignment 1 - Scientific Computing
Adm No: BSCCS/2023/72109


Q (a): Line graph of temperature readings over a week 
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperatures = [20, 22, 19, 23, 21, 24, 20]

plt.plot(days, temperatures, marker='o', linestyle='-', color='blue')
plt.title("Temperature Readings Over a Week")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

Q (b): Arithmetic sequence generation 
start = 5
difference = 3
terms = 8

sequence = [start + i * difference for i in range(terms)]
print("Arithmetic sequence:", sequence)

Q (c): Approximate volume under the surface z = x^2 + y^2 over 0 ≤ x, y ≤ 1 

import numpy as np
def f(x, y):
    return x**2 + y**2

x_vals = np.linspace(0, 1, 100)
y_vals = np.linspace(0, 1, 100)
dx = dy = x_vals[1] - x_vals[0]

volume = 0
for x in x_vals:
    for y in y_vals:
        volume += f(x, y) * dx * dy

print("Approximate volume under surface z = x^2 + y^2 is:", volume)
