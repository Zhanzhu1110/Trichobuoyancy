import numpy as np

# Define parameters and variable ranges
g = 9.81  # m/s^2
phi = 1.0  # unitless
eta = 9.6e-4  # kg/(m·s)

# Get input from user
rho_w = float(input("Please enter the density of water (kg/m^3): "))
r = float(input("Please enter the colony radius (m): "))
rho_dust = float(input("Please enter the density of dust (kg/m^3): "))

# Calculate K value
K = g * (1 - rho_w / rho_dust) / (6 * np.pi * r * phi * eta)

# Convert K unit from m/s/kg to m/d/ng
K_ng = K * 86400 / 1e12

# Output K result and unit
print(f"K = {K:.2f} m/s/kg = {K_ng:.2f} m/d/ng")
