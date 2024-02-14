from pandas import DataFrame
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class DataHandler:

    def __init__(self) -> None:
        pass

    def from_path_to_dataframe(self, path:str):
        e = None
        try:
            data = pd.read_csv(path)
            return data, e
        except Exception as e:            
            return None , e
        
    def analyse_data(self, data: "DataFrame") -> None:
        
        # Point 2: Correlation Matrix
        correlation_matrix = data.corr()
        print("\nCorrelation Matrix:")
        print(correlation_matrix)
        correlation_matrix.to_csv('correlation_matrix.csv')

        # Point 4: Box Plots for Key Variables (selecting a subset)
        #key_variables = ['Basilea Temperature [850 mb]', 'Basilea Relative Humidity [2 m]', 'Basilea CAPE [180-0 mb above gnd]', 'Basilea Geopotential Height [500 mb]', 'Basilea FAO Reference Evapotranspiration [2 m]', 'Basilea Soil Temperature [0-10 cm down]', 'Basilea Vapor Pressure Deficit [2 m]', 'Basilea Wind Speed [80 m]', 'Basilea Wind Speed [850 mb]', 'ID', 'month', 'Basilea Next Day Soil Moisture [0-10 cm down]']
        #data[key_variables].boxplot()
        #plt.title("Box Plots for Key Variables")

        # Point 5: Heatmap for Correlation
        plt.figure(figsize=(12, 10))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title("Correlation Heatmap")
        plt.savefig('correlation_matrix.png')
        plt.show()

        