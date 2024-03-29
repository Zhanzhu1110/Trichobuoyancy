import numpy as np

# Define parameter and variable ranges
g = 9.81  # m/s^2
phi = 1.0  # dimensionless
eta = 9.6e-4  # kg/(m·s)

rho_w_min, rho_w_max, num_rho_w = 1026.5, 1029, 100  # kg/m^3
rho_dust_min, rho_dust_max, num_rho_dust = 2100, 2600, 100  # kg/m^3
r_min, r_max, num_r = 0.442e-3, 1.282e-3, 100  # m

# Use linspace function to create arrays
rho_w_values = np.linspace(rho_w_min, rho_w_max, num_rho_w)  # kg/m^3
rho_dust_values = np.linspace(rho_dust_min, rho_dust_max, num_rho_dust)  # kg/m^3
r_values = np.linspace(r_min, r_max, num_r)  # m

# Initialize min and max K values
K_min = float("inf")
K_max = float("-inf")

# Loop over all possible combinations
for rho_w in rho_w_values:
    for rho_dust in rho_dust_values:
        for r in r_values:
            K = g * (1 - rho_w / rho_dust) / (6 * np.pi * r * phi * eta)
            K_min = min(K_min, K)
            K_max = max(K_max, K)

# Print K range in m/s/kg
print(f"K range: [{K_min:.2f}, {K_max:.2f}] m/s/kg")

# Convert K to m/d/ng
K_min_ng = K_min * 86400 / 1e12
K_max_ng = K_max * 86400 / 1e12

# Print K range in m/d/ng
print(f"K range: [{K_min_ng:.2f}, {K_max_ng:.2f}] m/d/ng")
