import numpy as np
import matplotlib.pyplot as plt

# Function to generate a Lorentzian line shape for NMR peaks
def lorentzian(x, x0, gamma):
    return 1 / (np.pi * gamma * (1 + ((x - x0) / gamma) ** 2))

# Parameters for ethanol NMR spectrum
ppm_range = np.linspace(0, 5, 1000)
ch3_shift = 1.2
ch2_shift = 3.7
oh_shift = 4.5
linewidth = 0.05
coupling_constant = 7.0

# Generate NMR signals for CH3 (triplet due to coupling with CH2)
ch3_signal = (lorentzian(ppm_range, ch3_shift - coupling_constant / 2, linewidth) +
              lorentzian(ppm_range, ch3_shift, linewidth) +
              lorentzian(ppm_range, ch3_shift + coupling_constant / 2, linewidth))

# Generate NMR signals for CH2 (quartet due to coupling with CH3)
ch2_signal = (lorentzian(ppm_range, ch2_shift - 3 * coupling_constant / 4, linewidth) +
              lorentzian(ppm_range, ch2_shift - coupling_constant / 4, linewidth) +
              lorentzian(ppm_range, ch2_shift + coupling_constant / 4, linewidth) +
              lorentzian(ppm_range, ch2_shift + 3 * coupling_constant / 4, linewidth))

# Generate NMR signal for OH (singlet, no coupling)
oh_signal = lorentzian(ppm_range, oh_shift, linewidth)

# Total NMR signal
total_signal = ch3_signal + ch2_signal + oh_signal

# Plot the NMR spectrum
plt.figure(figsize=(10, 6))
plt.plot(ppm_range, total_signal, 'b')
plt.gca().invert_xaxis()
plt.xlabel('Chemical Shift (ppm)')
plt.ylabel('Intensity')
plt.title('Simulated $^1H$ NMR Spectrum of Ethanol')
plt.show()
