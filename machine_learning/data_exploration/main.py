
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_selected_features(df):    
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    selected_features = [
        'Basilea Temperature [2 m elevation corrected]',
        'Basilea Soil Temperature [0-10 cm down]',
        'Basilea Soil Moisture [0-10 cm down]',
        'Basilea Precipitation Total',
        'Basilea Relative Humidity [2 m]',
        'Basilea FAO Reference Evapotranspiration [2 m]',
        'Basilea Evapotranspiration',
        'Basilea Wind Speed [10 m]',
        'Basilea Vapor Pressure Deficit [2 m]',
        'Basilea Wind Speed [900 mb]',
        'Basilea CAPE [180-0 mb above gnd]',
        'Basilea Wind Gust'
    ]
    
    n_rows, n_cols = 4, 3
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 10))
    fig.suptitle('Selected Features over Time with Shifted Yearly Average Line', y=1.02)
    
    axes = axes.flatten()
    
    color_palette = sns.color_palette("husl", n_colors=len(selected_features))
    
    for i, feature in enumerate(selected_features):        
        sns.lineplot(data=df, x='timestamp', y=feature, ax=axes[i], label=feature, color=color_palette[i])
                
        yearly_average = df.groupby(df['timestamp'].dt.year)[feature].mean()        
        yearly_average.index = pd.to_datetime(yearly_average.index.astype(str) + '-01-01') + pd.DateOffset(years=1)
                
        axes[i].plot(yearly_average.index, yearly_average, marker='o', color='black', markersize=5, linestyle='-', label='average')

        axes[i].set_title(feature)
        axes[i].set_xlabel('Timestamp')
        axes[i].set_ylabel('Feature Value')
        axes[i].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.show()

def box_plot_by_month(df):
    # Convert 'timestamp' to datetime format for proper plotting
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Extract month from timestamp
    df['month'] = df['timestamp'].dt.month

    selected_features = [
        'Basilea Temperature [2 m elevation corrected]',
        'Basilea Soil Temperature [0-10 cm down]',
        'Basilea Soil Moisture [0-10 cm down]',
        'Basilea Precipitation Total',
        'Basilea Relative Humidity [2 m]',
        'Basilea FAO Reference Evapotranspiration [2 m]',
        'Basilea Evapotranspiration',
        'Basilea Wind Speed [10 m]',
        'Basilea Vapor Pressure Deficit [2 m]',
        'Basilea Wind Speed [900 mb]',
        'Basilea CAPE [180-0 mb above gnd]',
        'Basilea Wind Gust'
    ]
    
    n_rows, n_cols = 4, 3
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 10))
    fig.suptitle('Box Plots by Month for Selected Features', y=1.02)

    # Flatten the axes array for easier indexing
    axes = axes.flatten()

    # Plot box plots for each selected feature
    for i, feature in enumerate(selected_features):
        sns.boxplot(x='month', y=feature, data=df, ax=axes[i])
        axes[i].set_title(feature)
        axes[i].set_xlabel('Month')
        axes[i].set_ylabel('Feature Value')

    # Adjust layout to prevent overlapping
    plt.tight_layout()

    # Show the plot
    plt.show()

if __name__ == "__main__":

    BASE_PATH = f'C:\\Users\\franc\OneDrive - Brunel University London\\Aquo\\FYP\\project\\XAquo\\XAquo_test\\XAquo_test_ETo\\xaquow-backend\\machine_learning\\data\\'
    BASE_PATH_TRAINIG = f'{BASE_PATH}training\\'
    BASE_PATH_TARGET = f'{BASE_PATH}target\\'
    dataset_path: str = f'{BASE_PATH_TRAINIG}dataexport_2017_2023.csv'   

    data = pd.read_csv(dataset_path)
    #plot_selected_features(data)
    box_plot_by_month(data)
    