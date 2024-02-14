import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

# Data
data_split = ['50/50', '70/30', '80/20']
rf_with_sm = np.array([
    [0.962026929817027, 362.14],
    [0.971251578, 466.34],
    [0.973990266, 538.13]
])
rf_no_sm = np.array([
    [0.82164845, 303.15],
    [0.849204944, 422.34],
    [0.862360844, 487.21]
])

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

# Bar chart for R-squared with adjusted colors
bar_width = 0.35
index = np.arange(len(data_split))
bar1 = ax1.bar(index - bar_width/2, rf_with_sm[:, 0], bar_width, color='orange', alpha=0.7, label='RF with SM - R-squared')
bar2 = ax1.bar(index + bar_width/2, rf_no_sm[:, 0], bar_width, color='skyblue', alpha=0.7, label='RF no SM - R-squared')

ax1.set_xlabel('Data Split')
ax1.set_ylabel('R-squared', color='orange')
ax1.tick_params(axis='y', labelcolor='orange')
ax1.set_ylim([0.7, 1])  # Adjust the y-axis limit for better visibility

# Scatter plot for Computational Time
sc3 = ax2.scatter(data_split, rf_with_sm[:, 1], color='green', label='RF with SM - Comp Time', marker='s')
sc4 = ax2.scatter(data_split, rf_no_sm[:, 1], color='red', label='RF no SM - Comp Time', marker='s')

# Connect points with lines for Computational Time
ax2.plot(data_split, rf_with_sm[:, 1], color='green', linestyle='--')
ax2.plot(data_split, rf_no_sm[:, 1], color='red', linestyle='--')

ax2.set_ylabel('Computational Time (X)', color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Move the legend within the plot area on the left
fig.legend([sc3, sc4, bar1, bar2],
           ['RF with SM - Comp Time', 'RF no SM - Comp Time', 'RF with SM - R-squared', 'RF no SM - R-squared'],
           loc='upper left', bbox_to_anchor=(0.18, 0.9), fontsize='medium')

plt.show()



# Data
# data_split = ['50/50', '70/30', '80/20']
# rf_with_sm = np.array([
#     [0.004522374, 0.007959529],
#     [0.003814249, 0.006950715],
#     [0.003587786, 0.006626929]
# ])
# rf_no_sm = np.array([
#     [0.011590208,0.017231573],
#     [0.010451321, 0.015907112],
#     [0.009940768, 0.015243868]
# ])

# # Plotting
# fig, ax1 = plt.subplots(figsize=(10, 6))

# # Line chart for MAE
# line1, = ax1.plot(data_split, rf_with_sm[:, 0], marker='o', label='RF with SM - MAE', color='darkorange')
# line2, = ax1.plot(data_split, rf_no_sm[:, 0], marker='o', label='RF no SM - MAE', color='dodgerblue')

# ax1.set_xlabel('Data Split')
# ax1.set_ylabel('MAE', color='black')
# ax1.tick_params(axis='y', labelcolor='black')

# # Line chart for RMSE with a different scale
# ax2 = ax1.twinx()
# line3, = ax2.plot(data_split, rf_with_sm[:, 1], marker='s', label='RF with SM - RMSE', color='orangered')
# line4, = ax2.plot(data_split, rf_no_sm[:, 1], marker='s', label='RF no SM - RMSE', color='royalblue')

# ax2.set_ylabel('RMSE', color='black')
# ax2.tick_params(axis='y', labelcolor='black')

# # Set a different scale for RMSE without exponential notation
# ax2.get_yaxis().set_major_formatter(ScalarFormatter(useMathText=True))
# ax2.get_yaxis().get_major_formatter().set_scientific(False)

# # Combine legends
# legend1 = plt.legend(handles=[line1, line3], loc='upper left')
# legend2 = plt.legend(handles=[line2, line4], loc='upper right')
# plt.gca().add_artist(legend1)


# plt.show()
