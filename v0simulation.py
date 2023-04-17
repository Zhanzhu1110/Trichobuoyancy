import numpy as np

# Define function to calculate V0
def calc_v0(g, V_cell, rho_cell, rho_w, r, phi, eta):
    return g * V_cell * (rho_cell - rho_w) / (6 * np.pi * r * phi * eta)

# Define parameter ranges and step sizes
V_cell_range = np.linspace(3.9e-13, 23e-13, 100)  # m^3
rho_cell_range = np.linspace(920, 1242, 100)  # kg/m^3
rho_w_range = np.linspace(1026.5, 1029, 100)  # kg/m^3
r_range = np.linspace(0.442e-3, 1.282e-3, 100)  # m

# Define other parameters
g = 9.81  # m/s^2
phi = 1.0  # dimensionless
eta = 9.6e-4  # kg/(m·s)

# Initialize minimum and maximum V0 values
V0_min = float("inf")
V0_max = float("-inf")

# Loop over all possible parameter combinations and update V0 min/max values
for V_cell in V_cell_range:
    for rho_cell in rho_cell_range:
        for rho_w in rho_w_range:
            for r in r_range:
                V0 = calc_v0(g, V_cell, rho_cell, rho_w, r, phi, eta)
                V0_min = min(V0_min, V0)
                V0_max = max(V0_max, V0)

# Output V0 range in m/s
print(f"V0 range: [{V0_min:.1e} m/s, {V0_max:.1e} m/s]")

# Convert V0 range to m/d
V0_min_d = V0_min * 86400
V0_max_d = V0_max * 86400

# Output V0 range in m/d
print(f"V0 range: [{V0_min_d:.0f} m/d, {V0_max_d:.0f} m/d]")
