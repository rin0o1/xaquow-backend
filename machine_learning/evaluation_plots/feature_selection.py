import matplotlib.pyplot as plt
import numpy as np

# Data
# num_features = [40, 39, 38, 35, 30, 28, 26, 22, 17, 13]
# comp_time = [487.21, 488.96, 467.49, 433, 416.87, 394.01, 372.19, 341.62, 273.71, 208.44]
# r_squared = [0.862360844, 0.862789816, 0.86246037, 0.862646973, 0.862746723, 0.863608009, 0.865912592, 0.867382199, 0.863773785, 0.856457258]
# rmse = [0.015243868, 0.015220095, 0.015238356, 0.015228015, 0.015222485, 0.015174648, 0.015045901, 0.014963221, 0.015165423, 0.015567354]
num_features = num_features = [40, 39, 38, 35, 30, 28, 26, 22, 17, 13, 10, 9]
comp_time = [603.64, 564.83, 480.92, 453.87, 394.88, 394.58, 329.27, 294.1, 215.24, 152.85, 96.29, 85.69]
r_squared = [0.973890546, 0.973937242, 0.974000573, 0.974420134, 0.975043596, 0.975281017, 0.97590658, 0.97697696, 0.978706533, 0.979759848, 0.980990383, 0.97908639]
rmse = [0.006639621, 0.006633681, 0.006625616, 0.006571939, 0.006491355, 0.006460404, 0.006378133, 0.006234846, 0.005996082, 0.005845898, 0.005665406, 0.005942359]

# Reverse arrays
num_features = num_features[::-1]
comp_time = comp_time[::-1]
r_squared = r_squared[::-1]
rmse = rmse[::-1]

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 6))

# Primary Y-axis (left) for Computational Time
ax1.plot(num_features, comp_time, color='orange', label='Computational Time (Line)')
ax1.set_xlabel('Number of Features')
ax1.set_ylabel('Computational Time (s)', color='orange')
ax1.tick_params(axis='y', labelcolor='orange')
ax1.legend()

# Create a second Y-axis (right) for R-squared
ax2 = ax1.twinx()
ax2.scatter(num_features, r_squared, color='salmon', label='R-squared')
ax2.set_ylabel('R-squared', color='salmon')
ax2.tick_params(axis='y', labelcolor='salmon')

# Create a third Y-axis (right) for RMSE
ax3 = ax1.twinx()
ax3.scatter(num_features, rmse, color='lightgreen', label='RMSE')
ax3.spines['right'].set_position(('outward', 60))  # Adjust the position of the third axis
ax3.set_ylabel('RMSE', color='lightgreen')
ax3.tick_params(axis='y', labelcolor='lightgreen')

# Shaded region for cool effect
ax1.axvspan(9.5, 10.5, alpha=0.2, color='lightgray', label='Min comp time with Min RMSE, Max R-squared')

# Combine legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
ax1.legend(lines + lines2 + lines3, labels + labels2 + labels3, loc="upper left")


plt.show()


# import matplotlib.pyplot as plt

# # Provided data
# total_features = [39, 38, 35, 30, 28, 26, 22, 17, 13]
# comp_time = [541.5, 529, 477.53, 447.31, 430.26, 362.69, 300.46, 228.99, 180.32]
# mae = [0.004770586, 0.004763242, 0.004727565, 0.004662754, 0.004632779, 0.004574608, 0.004474901, 0.004366722, 0.00459361]
# r2 = [0.954023167, 0.954079884, 0.954586663, 0.955086384, 0.955300476, 0.956315092, 0.957271005, 0.95877539, 0.955410968]
# rmse = [0.008819335, 0.008813893, 0.008765123, 0.008716764, 0.008695964, 0.008596705, 0.008502128, 0.008351117, 0.00868521]

# # Reverse arrays
# total_features = total_features[::-1]
# comp_time = comp_time[::-1]
# mae = mae[::-1]
# r2 = r2[::-1]
# rmse = rmse[::-1]

# # Plotting
# fig, ax1 = plt.subplots(figsize=(10, 6))

# # Primary Y-axis (left) for Computational Time
# ax1.plot(total_features, comp_time, color='orange', label='Computational Time (Line)')
# ax1.set_xlabel('Number of Features')
# ax1.set_ylabel('Computational Time (s)', color='orange')
# ax1.tick_params(axis='y', labelcolor='orange')
# ax1.legend(loc='upper left')

# # Create a second Y-axis (right) for R-squared
# ax2 = ax1.twinx()
# ax2.scatter(total_features, r2, color='salmon', label='R-squared')
# ax2.set_ylabel('R-squared', color='salmon')
# ax2.tick_params(axis='y', labelcolor='salmon')

# # Create a third Y-axis (right) for RMSE
# ax3 = ax1.twinx()
# ax3.scatter(total_features, rmse, color='lightgreen', label='RMSE')
# ax3.spines['right'].set_position(('outward', 60))  # Adjust the position of the third axis
# ax3.set_ylabel('RMSE', color='lightgreen')
# ax3.tick_params(axis='y', labelcolor='lightgreen')

# ax1.axvspan(16.5, 17.5, alpha=0.2, color='lightgray', label='Min comp time with Min RMSE, Max R-squared')

# # Combine legends on the right
# lines, labels = ax1.get_legend_handles_labels()
# lines2, labels2 = ax2.get_legend_handles_labels()
# lines3, labels3 = ax3.get_legend_handles_labels()
# ax1.legend(lines + lines2 + lines3, labels + labels2 + labels3, loc="upper right")

# plt.show()
