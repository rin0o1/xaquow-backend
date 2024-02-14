import matplotlib.pyplot as plt
import numpy as np

# Data
num_features = [14, 18, 23, 27, 29, 31, 36, 39, 40]
comp_time = [188.97, 268.98, 331.93, 344.92, 360.42, 378.36, 400.00, 416.99, 435.50]
r_squared = [0.8277105691457871, 0.8351390902970198, 0.8344785450133718,
             0.8355121007286794, 0.8403191651719566, 0.8392291966238417,
             0.8392559935557978, 0.8394641326295778, 0.8394859300663693]
rmse = [0.017072440597143506, 0.016700333274677345, 0.016733756293893946,
        0.016840929946090634, 0.016593022018622842, 0.01664955702436725,
        0.01664816941035405, 0.01663738749359577, 0.016636257949403526]

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
ax1.axvspan(28.5, 29.5, alpha=0.2, color='lightgray', label='Min comp time with Min RMSE, Max R-squared')

# Combine legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
ax1.legend(lines + lines2 + lines3, labels + labels2 + labels3, loc="upper left")

plt.show()


# import matplotlib.pyplot as plt

# # Given data
# training_set_size = [3884, 21363, 38842]
# training_error = [8.42892254e-05, 5.40964045e-05, 4.30081224e-05]
# test_set_error = [0.0005969, 0.00038177, 0.00030232]
# computational_time = [20.95, 140, 425]

# # Plotting MSE and training set as a line
# plt.figure(figsize=(10, 6))

# # Plotting training error as a line
# plt.plot(training_set_size, training_error, color='blue', marker='o', label='Training Error')

# # Plotting test set error as a line
# plt.plot(training_set_size, test_set_error, color='orange', marker='x', label='Test Set Error')

# # Adding labels and title
# plt.xlabel('Training Set Size')
# plt.ylabel('Mean Squared Error')
# plt.title('Line Plot of Training and Test Set Errors with Computational Time')

# # Adding legend in the middle
# plt.legend(loc='upper center')

# # Creating a second y-axis for computational time
# ax2 = plt.gca().twinx()
# ax2.plot(training_set_size, computational_time, color='green', marker='s', linestyle='dashed', label='Computational Time')
# ax2.set_ylabel('Computational Time (s)')

# # Adding legend for computational time
# ax2.legend(loc='upper right')

# # Add vertical shadow between 20000 and 23000
# plt.axvspan(20000, 23000, color='gray', alpha=0.2)

# # Show the plot
# plt.show()
