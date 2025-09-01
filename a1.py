import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# Physical constants
h = 6.626e-34
m_e = 9.10e-31
e = 1.6e-19
c = 2.99e8

# ------------------------------
# Parameters
beta = 8e8
Ip = 100e-12
Cc = 25e-3
Cs = 50e-3
E = 20 * 10**3 * e
DeltaE = 1 * e

# ------------------------------
# Wavelength λ (m)
lambda_m = h / np.sqrt(2 * m_e * E * (1 + E / (2 * m_e * c**2)))

# ------------------------------
# Semi-convergence angle (radians)
alpha_mrad = np.linspace(1, 30, 200)
alpha_rad = alpha_mrad * 1e-3

# ------------------------------
# Contributions to probe size
d_i = (0.63 * np.sqrt(Ip / beta)) / alpha_rad
d_d = 1.22 * lambda_m / np.sin(alpha_rad)
d_c = Cc * alpha_rad * (DeltaE / E)
d_s = 0.5 * Cs * alpha_rad**3
d_total = np.sqrt(d_i**2 + d_d**2 + d_c**2 + d_s**2)

x = np.argmin(d_total)
print(alpha_mrad[x], d_total[x])

# ------------------------------
# Plot
fig, ax = plt.subplots(figsize=(9,6))
colors = ['dodgerblue', 'orange', 'green', 'purple', 'black']
labels = ["Brightness limited ($d_i$)", "Diffraction ($d_d$)", "Chromatic ($d_c$)", "Spherical ($d_s$)", "Total probe size"]

for i, d in enumerate([d_i, d_d, d_c, d_s, d_total]):
    ax.fill_between(alpha_mrad, d, alpha=0.15 if i < 4 else 0, color=colors[i])
    ax.plot(alpha_mrad, d, color=colors[i], linewidth=2, label=labels[i])

ax.axvline(alpha_mrad[x], color='red', linestyle='--', label=f'Minimum at α={alpha_mrad[x]:.2f} mrad')
ax.set_xlabel("Semi-convergence angle α (mrad)", fontsize=12)
ax.set_ylabel("Contribution to probe diameter (m)", fontsize=12)
ax.set_title("SEM Probe Size Contributions — Shaded Style", fontsize=14, weight='bold')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(frameon=True, fontsize=10, loc='upper right')

# Authentication
ax.text(29, 0.0004, "Ansh Rastogi", fontsize=9, color='gray', alpha=0.7, ha='right')

plt.tight_layout()
plt.show()
