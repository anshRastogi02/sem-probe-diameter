import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# Physical constants
h = 6.626e-34
m_e = 9.10e-31
e = 1.601e-19
c = 2.99e8

# ------------------------------
# Parameters
beta = 8e8
Ip = 100e-12
Cc = 25e-3
Cs = 50e-3
E = 20 * 10**3 * e
lambda_m = h / np.sqrt(2 * m_e * E * (1 + E / (2 * m_e * c**2)))

# ------------------------------
# Semi-convergence angle
alpha_mrad = np.linspace(1, 30, 200)
alpha_rad = alpha_mrad * 1e-3

# ------------------------------
# Ratios for different DeltaE
ratios = {}
for DeltaE_eV in [0.01, 0.1, 1]:
    DeltaE = DeltaE_eV * e
    d_i = (0.63 * np.sqrt(Ip / beta)) / alpha_rad
    d_d = 1.22 * lambda_m / np.sin(alpha_rad)
    d_c = Cc * alpha_rad * (DeltaE / E)
    d_s = 0.5 * Cs * alpha_rad**3
    d_total = np.sqrt(d_i**2 + d_d**2 + d_c**2 + d_s**2)
    ratios[DeltaE_eV] = 100 * d_c / d_total

# ------------------------------
# Plot
fig, ax = plt.subplots(figsize=(9,6))
colors = ['purple', 'orange', 'green']

for i, (DeltaE_eV, ratio) in enumerate(ratios.items()):
    ax.fill_between(alpha_mrad, ratio, alpha=0.25, color=colors[i])
    ax.plot(alpha_mrad, ratio, color=colors[i], linewidth=2, label=f"ΔE = {DeltaE_eV} eV")

# Labels & title
ax.set_xlabel("Semi-convergence angle α (mrad)", fontsize=12)
ax.set_ylabel("Chromatic aberration contribution (%)", fontsize=12)
ax.set_title("Chromatic Aberration Contribution to Total (%) — Shaded Style", fontsize=14, weight='bold')

ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(frameon=True, fontsize=10, loc='upper right')

# Authentication
ax.text(29, 5, "Ansh Rastogi", fontsize=9, color='gray', alpha=0.7, ha='right')

plt.tight_layout()
plt.show()
