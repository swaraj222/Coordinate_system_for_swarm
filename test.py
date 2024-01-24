import numpy as np
import matplotlib.pyplot as plt

# Set the seed for reproducibility (optional)
np.random.seed(42)

# Parameters for the Gaussian noise
mean = 1
std_dev = 1
num_samples = 1000

# Generate Gaussian noise
gaussian_noise = np.random.normal(mean, std_dev, num_samples)

# Create a linear scaling factor based on the position of each sample
scaling_factor = np.linspace(10, 20, num_samples)  # Adjust the range based on your requirements

# Multiply the Gaussian noise by the scaling factor
gaussian_noise_scaled = gaussian_noise * scaling_factor

# Plot the original Gaussian noise
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.hist(gaussian_noise, bins=30, density=True, alpha=0.7, color='blue', edgecolor='black')
plt.title('Original Gaussian Noise')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Plot the Gaussian noise with increasing amplitude
plt.subplot(1, 2, 2)
plt.hist(gaussian_noise_scaled, bins=30, density=True, alpha=0.7, color='orange', edgecolor='black')
plt.title('Gaussian Noise with Increasing Amplitude')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
