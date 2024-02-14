
from machine_learning.entities.SoilMoinstureLinearRegression import SoilMoinstureLinearRegression
from machine_learning.entities.SoilMoinstureRandomForest import SoilMoinstureRandomForest
from numpy import ndarray

if __name__ == "__main__":

    BASE_PATH = f'C:\\Users\\franc\OneDrive - Brunel University London\\Aquo\\FYP\\project\\XAquo\\XAquo_test\\XAquo_test_ETo\\xaquow-backend\\machine_learning\\data\\'
    BASE_PATH_TRAINIG = f'{BASE_PATH}training\\'
    BASE_PATH_TARGET = f'{BASE_PATH}target\\'
    training_data_path: str = f'{BASE_PATH_TRAINIG}dataexport_2017_2023.csv'    
    holdout_data_path: str = f'{BASE_PATH_TARGET}full_weather_RFwithSM_simulation.csv'
    target_column: str = 'Basilea Next Day Soil Moisture [0-10 cm down]'
    dates_columns: "ndarray" = ['timestamp']
    
    print(f'Reading data...')

    smlr = SoilMoinstureLinearRegression(
        training_data_path=training_data_path,        
        target_column=target_column,
        holdout_data_path=holdout_data_path,
        dates_columns=dates_columns,        
        output_file_name="linear_regression_output.csv",        
        data_split=0.2,        
    )       
    
    ok = smlr.pre_process()
        
    if ok:
        print(f'Training Linear Regression..')
        smlr.training_(show_plotting=True)                          
        print(f'Done Linear Regression')        
             
    unselected_features = [
        'Basilea Snowfall Amount',
        'Basilea Sunshine Duration',
        'Basilea Shortwave Radiation',
        'Basilea Direct Shortwave Radiation',
        'Basilea Growing Degree Days [2 m elevation corrected]',
        'Basilea Precipitation Total',
        'Basilea Diffuse Shortwave Radiation',
        'Basilea FAO Reference Evapotranspiration [2 m]',
        'Basilea Cloud Cover Total',
        'Basilea Cloud Cover Low [low cld lay]',
        'Basilea Evapotranspiration',
        'Basilea Temperature [2 m elevation corrected]',
        'Basilea Temperature',
        'Basilea Vapor Pressure Deficit [2 m]',       
        'Basilea Wind Speed [10 m]',
        'Basilea Wind Direction [80 m]',
        'Basilea Wind Direction [10 m]',
        'Basilea Wind Speed [80 m]',
        'Basilea Wind Gust',
        'Basilea Relative Humidity [2 m]',
        'Basilea Soil Temperature [0-10 cm down]',
        'Basilea Cloud Cover High [high cld lay]',     
        'Basilea Temperature [1000 mb]',
        'Basilea Wind Direction [850 mb]',
        'Basilea Wind Speed [900 mb]',
        'Basilea Wind Direction [900 mb]',
        'Basilea Cloud Cover Medium [mid cld lay]',    
        'Basilea Wind Speed [850 mb]',
        'Basilea Geopotential Height [700 mb]',
        'Basilea Wind Direction [700 mb]',
        'Basilea Temperature [700 mb]',
        'Basilea Temperature [850 mb]',
        'Basilea CAPE [180-0 mb above gnd]',
        'Basilea Wind Speed [700 mb]',                
    ]
    
    rf = SoilMoinstureRandomForest(
        training_data_path=training_data_path,        
        target_column=target_column,
        holdout_data_path=holdout_data_path,
        dates_columns=dates_columns,        
        output_file_name="RF_with_SM_output.csv",
        data_split=0.2,                
    )

    ok = rf.pre_process(unselected_features=unselected_features)    
    if ok:
        print(f'Training Random Forest..')
        rf.training_(include_optimisation=False)                 
        print('Scores')            
        print(f'Done')   

    rf.test_on_unseen_data(unseen_data_path=holdout_data_path, unselected_features=unselected_features)


# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# # Your data
# data = {
#     'max_depth': [30, 30, 30, 30, 40, 40, 40, 40, 50, 50, 50, 50],
#     'n_estimators': [50, 100, 150, 200, 50, 100, 150, 200, 50, 100, 150, 200],
#     'mean_squared_error': [5.1684382875521105e-05, 5.041571926766229e-05, 4.990469748161466e-05, 4.988395180998598e-05,
#                            5.170915722908775e-05, 5.0454069734682454e-05, 4.9913466878712694e-05, 4.991830623844045e-05,
#                            5.170063298990368e-05, 5.0449898664193886e-05, 4.991082026925573e-05, 4.9916163760750865e-05]
# }

# df = pd.DataFrame(data)

# # Pivot the DataFrame for heatmap
# heatmap_data = df.pivot(index='max_depth', columns='n_estimators', values='mean_squared_error')

# # Create a heatmap
# plt.figure(figsize=(10, 8))
# sns.heatmap(heatmap_data, annot=True, fmt=".8f", cmap="viridis", linewidths=.5)
# plt.title('Grid Search Results - Mean Squared Error')
# plt.show()


# import matplotlib.pyplot as plt
# import pandas as pd

# # Your data
# data = {
#     'max_depth': [30, 30, 30, 30, 40, 40, 40, 40, 50, 50, 50, 50],
#     'n_estimators': [50, 100, 150, 200, 50, 100, 150, 200, 50, 100, 150, 200],
#     'mean_squared_error': [5.1684382875521105e-05, 5.041571926766229e-05, 4.990469748161466e-05, 4.988395180998598e-05,
#                            5.170915722908775e-05, 5.0454069734682454e-05, 4.9913466878712694e-05, 4.991830623844045e-05,
#                            5.170063298990368e-05, 5.0449898664193886e-05, 4.991082026925573e-05, 4.9916163760750865e-05]
# }

# df = pd.DataFrame(data)

# # Scatter plot with legend
# plt.figure(figsize=(10, 8))
# for depth in df['max_depth'].unique():
#     subset = df[df['max_depth'] == depth]
#     plt.scatter(subset['n_estimators'], subset['mean_squared_error'], label=f'Max Depth = {depth}', s=100)

# plt.xlabel('Number of Estimators')
# plt.ylabel('Mean Squared Error')
# plt.title('GridSearch Optimisation Results')
# plt.legend()
# plt.show()
