# import numpy as np
# import matplotlib.pyplot as plt

# # Generate some example data
# original_data = np.linspace(0, 15, 1000)  # Example linear data from 0 to 10

# # Set the seed for reproducibility (optional)
# # np.random.seed(42)

# # Parameters for the Gaussian noise
# mean = 0

# # Generate Gaussian noise
# gaussian_noise = np.random.normal(mean, 0.4, len(original_data))  # Use a standard deviation of 1

# # Scale the Gaussian noise based on the original data
# scaling_factor = original_data / max(original_data)  # Adjust the scaling factor as needed
# scaled_gaussian_noise = gaussian_noise * scaling_factor

# # Add the scaled Gaussian noise to the original data
# noisy_data = original_data + scaled_gaussian_noise

# # Plot the original data and the data with scaled Gaussian noise
# plt.plot(original_data, label='Original Data')
# plt.plot(noisy_data, label='Noisy Data with Scaling')
# plt.legend()
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.title('Original Data vs. Noisy Data with Scaled Gaussian Noise')
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

def apply_moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# Generate some example data with Gaussian noise
original_data = np.linspace(0, 15, 1000)  # Example linear data from 0 to 10
noise = np.random.normal(0, 0.4, len(original_data))  # Gaussian noise
noisy_data = original_data + noise

# Apply a moving average filter to mitigate the noise
window_size = 10
filtered_data = apply_moving_average(noisy_data, window_size)

# Plot the original data, noisy data, and filtered data
plt.plot(original_data, label='Original Data')
plt.plot(noisy_data, label='Noisy Data')
plt.plot(filtered_data, label=f'Filtered Data (Moving Average, Window Size={window_size})')
plt.legend()
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Original Data vs. Noisy Data vs. Filtered Data')
plt.show()
