#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:06:23 2025

@author: fredrik
"""

import matplotlib.pyplot as plt
import numpy as np

# Data
Vin = np.array([1, 1.8, 2.2, 2.5, 2.9, 3.3, 3.7, 4.4, 5.3, 6.5, 7.3, 8.3, 9.1])
Vacross = np.array([1.14, 1.96, 2.41, 2.56, 2.66, 2.72, 2.76, 2.84, 2.93, 3.02, 3.08, 3.15, 3.20])
I_circuit = np.array([0.0, 0.0, 0.0, 0.36, 3.11, 6.21, 9.24, 15.24, 24.5, 35.2, 42.6, 52.0, 59.0])
Intensity = np.array([5.00, 8.00, 4.70, 590.30, 4377.70, 7979.50, 10846.90, 16080.10, 21958.10, 27642.20, 30184.80, 33590.00, 36153.70])

size=(6, 5)


"""
Plot 1: Input Voltage vs Current
"""

coefficients = np.polyfit(Vin[4:], I_circuit[4:], 1)  
linear_fit = np.poly1d(coefficients)

# Create a range of x values for the fitted line
Vin_fit = np.linspace(Vin[4], Vin[-1], 100)
I_fit = linear_fit(Vin_fit)

k = coefficients[0]  # Slope (mA/V)
m = coefficients[1]  # Intercept (mA)

# Fit equation string with proper LaTeX formatting
fit_string = rf"$I(V) = {k:.1f} \,\mathrm{{mA/V}} \cdot V_{{in}} {m:.1f} \,\mathrm{{mA}}$"


plt.figure(figsize=size)
plt.scatter(Vin, I_circuit, label="Measured data") 
plt.plot(Vin_fit, I_fit, label=f"Linear Fit: "+fit_string, color='red')   
plt.xlabel(r"Input Voltage ($V$)")  
plt.ylabel(r"Circuit Current (mA)")
plt.title("Input Voltage vs Current")
plt.legend()
plt.grid()
plt.savefig('LED_report/Figures/part1(a).pdf')  
plt.close()  



"""
Plot 2: Current vs Intensity
"""

plt.figure(figsize=size)
plt.scatter(I_circuit, Intensity, label="Measured data")
plt.xlabel("Circuit Current (mA)")
plt.ylabel("Intensity (counts)")
plt.title("Current vs Intensity")
plt.legend()
plt.grid()
plt.savefig('LED_report/Figures/part1(b).pdf')  
plt.close()


"""
Plot 3: Voltage Across vs Intensity
"""
plt.figure(figsize=size)
plt.scatter(Vacross, Intensity, label="Measured data")
plt.xlabel("Voltage across LED (V)")
plt.ylabel("Intensity (counts)")
plt.title("Voltage LED vs Intensity")
plt.legend()
plt.grid()
plt.savefig('LED_report/Figures/part1(c).pdf') 
plt.close()
