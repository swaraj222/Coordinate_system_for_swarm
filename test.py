# import numpy as np
# import matplotlib.pyplot as plt

# # Set the seed for reproducibility (optional)
# np.random.seed(42)

# # Parameters for the Gaussian noise
# mean = 1
# std_dev = 1
# num_samples = 1000

# # Generate Gaussian noise
# gaussian_noise = np.random.normal(mean, std_dev, num_samples)

# # Create a linear scaling factor based on the position of each sample
# scaling_factor = np.linspace(10, 20, num_samples)  # Adjust the range based on your requirements

# # Multiply the Gaussian noise by the scaling factor
# gaussian_noise_scaled = gaussian_noise * scaling_factor

# # Plot the original Gaussian noise
# plt.figure(figsize=(12, 4))

# plt.subplot(1, 2, 1)
# plt.hist(gaussian_noise, bins=30, density=True, alpha=0.7, color='blue', edgecolor='black')
# plt.title('Original Gaussian Noise')
# plt.xlabel('Value')
# plt.ylabel('Frequency')

# # Plot the Gaussian noise with increasing amplitude
# plt.subplot(1, 2, 2)
# plt.hist(gaussian_noise_scaled, bins=30, density=True, alpha=0.7, color='orange', edgecolor='black')
# plt.title('Gaussian Noise with Increasing Amplitude')
# plt.xlabel('Value')
# plt.ylabel('Frequency')

# plt.tight_layout()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

def generate_scaled_noisy_data(original_value, scaling_factor):
    # Set the seed for reproducibility (optional)
    # np.random.seed(42)

    # Generate Gaussian noise
    gaussian_noise = np.random.normal(0, scaling_factor * original_value)

    # Add the Gaussian noise to the original value
    noisy_data = original_value + gaussian_noise

    return noisy_data

# Generate some example data
original_value = 0.28  # Example original value

# Set the scaling factor (adjust this single value as needed)
scaling_factor = 0.1  # You can experiment with different scaling factors

# Generate noisy data for the given original value
noisy_data = generate_scaled_noisy_data(original_value, scaling_factor)

# Print the results
print(f'Original Value: {original_value}')
print(f'Noisy Data: {noisy_data}')

# Plot the original value and the noisy data
plt.scatter(original_value, original_value, label='Original Value', color='blue')
plt.scatter(original_value, noisy_data, label='Noisy Data', color='red')
plt.legend()
plt.xlabel('Index')
plt.ylabel('Value')
plt.title(f'Original Value vs. Noisy Data (Scaling Factor: {scaling_factor})')
plt.show()
