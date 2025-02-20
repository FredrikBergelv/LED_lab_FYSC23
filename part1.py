import matplotlib.pyplot as plt
import numpy as np

# Data
Vin = np.array([1, 1.8, 2.2, 2.5, 2.9, 3.3, 3.7, 4.4, 5.3, 6.5, 7.3, 8.3, 9.1])
Vacross = np.array([1.14, 1.96, 2.41, 2.56, 2.66, 2.72, 2.76, 2.84, 2.93, 3.02, 3.08, 3.15, 3.20])
I_circuit = np.array([0.0, 0.0, 0.0, 0.36, 3.11, 6.21, 9.24, 15.24, 24.5, 35.2, 42.6, 52.0, 59.0])
Intensity = np.array([5.00, 8.00, 4.70, 590.30, 4377.70, 7979.50, 10846.90, 16080.10, 21958.10, 27642.20, 30184.80, 33590.00, 36153.70])

# Create Figures Directory if it doesn't exist
import os
if not os.path.exists("Figures"):
    os.makedirs("Figures")

# Plot 1: Input Voltage vs Current
plt.figure(figsize=(5, 5))
plt.plot(Vin, I_circuit, 'bo-', label="V_in vs I")
plt.xlabel("Input Voltage (V)")
plt.ylabel("Circuit Current (mA)")
plt.title("Input Voltage vs Current")
plt.legend()
plt.grid()
plt.savefig('LED_report/Figures/part1(a).pdf')  # Save the figure
plt.close()  # Close the figure to avoid overlap

# Plot 2: Current vs Intensity
plt.figure(figsize=(5, 5))
plt.plot(I_circuit, Intensity, 'ro-', label="I vs Intensity")
plt.xlabel("Circuit Current (mA)")
plt.ylabel("Intensity (counts)")
plt.title("Current vs Intensity")
plt.legend()
plt.grid()
plt.savefig('LED_report/Figures/part1(b).pdf')  # Save the figure
plt.close()

# Plot 3: Voltage Across vs Intensity
plt.figure(figsize=(5, 5))
plt.plot(Vacross, Intensity, 'go-', label="V_across vs Intensity")
plt.xlabel("Voltage Across (V)")
plt.ylabel("Intensity (counts)")
plt.title("Voltage Across vs Intensity")
plt.legend()
plt.grid()
plt.savefig('LED_report/Figures/part1(c).pdf')  # Save the figure
plt.close()

