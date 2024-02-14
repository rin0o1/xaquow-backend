import matplotlib.pyplot as plt
import numpy as np

# Provided feature importance values
feature_importance_2 = np.array([9.82642734e-04, 4.43672511e-04, 2.50214446e-03, 4.66065517e-03,
                                4.16987275e-03, 3.46478319e-04, 3.82170834e-04, 4.40828366e-04,
                                6.72404152e-04, 6.33599389e-04, 5.29658827e-05, 1.78115020e-03,
                                7.74016795e-04, 2.18739486e-03, 2.77266917e-03, 8.00775029e-04,
                                4.71632184e-03, 6.87414754e-03, 8.24970217e-03, 1.05726818e-02,
                                3.42299567e-03, 5.18721164e-03, 9.77455069e-04, 7.63635157e-04,
                                1.01793140e-03, 1.93524005e-03, 8.38084690e-01, 1.24509454e-03,
                                1.41413481e-03, 1.47227057e-03, 1.47340219e-03, 1.46199219e-03,
                                1.58407195e-03, 2.58082764e-03, 2.74677612e-03, 3.31392278e-03,
                                2.57891672e-03, 5.01938515e-03, 4.15822360e-03, 6.54767432e-03,
                                6.75350981e-03, 8.19767307e-03, 1.75953401e-02, 2.64513310e-02])

# Provided feature names
feature_names_2 = ['Basilea Temperature [2 m elevation corrected]',
                   'Basilea Growing Degree Days [2 m elevation corrected]',
                   'Basilea Temperature [1000 mb]', 'Basilea Temperature [850 mb]',
                   'Basilea Temperature [700 mb]', 'Basilea Sunshine Duration',
                   'Basilea Shortwave Radiation', 'Basilea Direct Shortwave Radiation',
                   'Basilea Diffuse Shortwave Radiation', 'Basilea Precipitation Total',
                   'Basilea Snowfall Amount', 'Basilea Relative Humidity [2 m]',
                   'Basilea Cloud Cover Total', 'Basilea Cloud Cover High [high cld lay]',
                   'Basilea Cloud Cover Medium [mid cld lay]',
                   'Basilea Cloud Cover Low [low cld lay]',
                   'Basilea CAPE [180-0 mb above gnd]',
                   'Basilea Mean Sea Level Pressure [MSL]',
                   'Basilea Geopotential Height [1000 mb]',
                   'Basilea Geopotential Height [850 mb]',
                   'Basilea Geopotential Height [700 mb]',
                   'Basilea Geopotential Height [500 mb]', 'Basilea Evapotranspiration',
                   'Basilea FAO Reference Evapotranspiration [2 m]', 'Basilea Temperature',
                   'Basilea Soil Temperature [0-10 cm down]',
                   'Basilea Soil Moisture [0-10 cm down]',
                   'Basilea Vapor Pressure Deficit [2 m]', 'Basilea Wind Speed [10 m]',
                   'Basilea Wind Direction [10 m]', 'Basilea Wind Speed [80 m]',
                   'Basilea Wind Direction [80 m]', 'Basilea Wind Gust',
                   'Basilea Wind Speed [900 mb]', 'Basilea Wind Direction [900 mb]',
                   'Basilea Wind Speed [850 mb]', 'Basilea Wind Direction [850 mb]',
                   'Basilea Wind Speed [700 mb]', 'Basilea Wind Direction [700 mb]',
                   'Basilea Wind Speed [500 mb]', 'Basilea Wind Direction [500 mb]',
                   'month', 'Basilea Soil Moisture [0-10 cm down] lag',
                   'Basilea Soil Moisture [0-10 cm down] lag3']

# Sort features based on importance
sorted_indices_2 = np.argsort(feature_importance_2)
sorted_feature_importance_2 = feature_importance_2[sorted_indices_2]
sorted_feature_names_2 = [feature_names_2[i] for i in sorted_indices_2]

print(sorted_feature_names_2)

# Plotting
plt.figure(figsize=(10, 20))
plt.barh(range(len(feature_importance_2)), sorted_feature_importance_2, align='center', color='orange')
plt.yticks(range(len(feature_importance_2)), sorted_feature_names_2)
plt.xlabel('Feature Importance')
plt.title('Feature Importance Plot (Second Set)')
plt.show()
