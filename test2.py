import numpy as np
import matplotlib.pyplot as plt

# Generate some example data
original_data = np.linspace(0, 10, 20)  # Example linear data from 0 to 10

# Set the seed for reproducibility (optional)
# np.random.seed(42)

# Parameters for the Gaussian noise
mean = 0

# Generate Gaussian noise
gaussian_noise = np.random.normal(mean, 0.6, len(original_data))  # Use a standard deviation of 1

# Scale the Gaussian noise based on the original data
scaling_factor = original_data / max(original_data)  # Adjust the scaling factor as needed
scaled_gaussian_noise = gaussian_noise * scaling_factor

# Add the scaled Gaussian noise to the original data
noisy_data = original_data + scaled_gaussian_noise

# Plot the original data and the data with scaled Gaussian noise
plt.plot(original_data, label='Original Data')
plt.plot(noisy_data, label='Noisy Data with Scaling')
plt.legend()
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Original Data vs. Noisy Data with Scaled Gaussian Noise')
plt.show()
