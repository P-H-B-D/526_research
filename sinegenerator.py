import numpy as np

# Parameters
num_samples = 1000  # Number of samples
amplitude_min = 0.0  # Minimum amplitude
amplitude_max = 1.0  # Maximum amplitude
scale_min = 0  # Minimum scaled value
scale_max = 999  # Maximum scaled value


t = np.linspace(0, 2, num_samples)
amplitude = amplitude_min + (amplitude_max - amplitude_min) * np.sin(2 * np.pi * t) + 1
amplitude = amplitude + 0.2*np.random.rand(num_samples)
scaled_amplitude = np.interp(amplitude, (amplitude.min(), amplitude.max()), (scale_min, scale_max))
import matplotlib.pyplot as plt


#draw 10 normally spaced samples from the sine wave and plot them as points on the sine wave
sample_indices = np.linspace(0, num_samples-1, 21)
sample_indices = sample_indices.astype(int)
sampled_amplitude = scaled_amplitude[sample_indices]
sampled_amplitude= sampled_amplitude.astype(int)

print(" ".join(sampled_amplitude.astype(str)))

plt.plot(t, scaled_amplitude)
plt.plot(t[sample_indices], sampled_amplitude, 'ro')
plt.show()

