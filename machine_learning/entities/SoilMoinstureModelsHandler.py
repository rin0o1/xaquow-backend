from machine_learning.entities.SoilMoinstureLinearRegression import SoilMoinstureLinearRegression
from machine_learning.entities.SoilMoinstureRandomForest import SoilMoinstureRandomForest

class SoilMoistureModelsHandler:

    def __init__(self, output_data_folder:str = None, test_data_path:str = None) -> None:         
        self.BASE_PATH = f'C:\\Users\\franc\OneDrive - Brunel University London\\Aquo\\FYP\\project\\XAquo\\XAquo_test\\XAquo_test_ETo\\xaquow-backend\\machine_learning'
        self.BASE_PATH_TRAINIG = f'{self.BASE_PATH}\\data\\training\\'
        self.BASE_PATH_TARGET = f'{self.BASE_PATH}\\data\\target\\'

        self.training_data_path: str = f'{self.BASE_PATH_TRAINIG}dataexport_2017_2023.csv'      
        self.output_data_folder = output_data_folder or rf'{self.BASE_PATH}\\output'        
        self.holdout_data_path: str = test_data_path or f'{self.BASE_PATH_TARGET}full_weather_RFwithSM_simulation.csv'

        self.target_column: str = 'Basilea Next Day Soil Moisture [0-10 cm down]'
        self.dates_columns: list = ['timestamp']

    def run_RF_with_SM(self, use_cached_model = False):        
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
        output_file_name = "RF_with_SM_output.csv"

        rf = SoilMoinstureRandomForest(
            training_data_path=self.training_data_path,        
            target_column=self.target_column,
            holdout_data_path=self.holdout_data_path,
            dates_columns=self.dates_columns,        
            output_file_name=output_file_name,
            output_folder_name=self.output_data_folder,
            data_split=0.2,                       
        )

        if not use_cached_model:
            ok = rf.pre_process(unselected_features=unselected_features)    
            if ok:
                print(f'Training Random Forest with SM..')
                rf.training_(include_optimisation=False)                 
                print('Scores')            
                print(f'Done')   

        rf.test_on_unseen_data(unseen_data_path=self.holdout_data_path, unselected_features=unselected_features)
        
        export_predicted_values_path = rf'{self.output_data_folder}{output_file_name}'
        return export_predicted_values_path
    
    def run_RF_no_SM(self, use_cached_model = False):
        unselected_features = [
            'Basilea Snowfall Amount',
            'Basilea Soil Moisture [0-10 cm down]',
            'Basilea Precipitation Total',
            'Basilea Sunshine Duration',
            'Basilea Cloud Cover Low [low cld lay]',
            'Basilea Growing Degree Days [2 m elevation corrected]',
            'Basilea Cloud Cover Total',
            'Basilea Temperature [2 m elevation corrected]',
            'Basilea Diffuse Shortwave Radiation',
            'Basilea Shortwave Radiation',
            'Basilea Direct Shortwave Radiation',
            'Basilea Wind Direction [10 m]',
            'Basilea Wind Speed [80 m]',
            'Basilea Wind Direction [80 m]',
            'Basilea Wind Speed [10 m]',
            'Basilea Geopotential Height [1000 mb]',
            'Basilea Wind Gust',
            'Basilea Cloud Cover Medium [mid cld lay]',
            'Basilea CAPE [180-0 mb above gnd]'                                     
        ]
        output_file_name = "RF_no_SM_output.csv"
        rf = SoilMoinstureRandomForest(
            training_data_path=self.training_data_path,        
            target_column=self.target_column,
            holdout_data_path=self.holdout_data_path,
            dates_columns=self.dates_columns,        
            output_file_name=output_file_name,
            output_folder_name=self.output_data_folder,
            data_split=0.2,  
            model_name="RF_model_no_SM"                     
        )

        if not use_cached_model:
            ok = rf.pre_process(unselected_features=unselected_features)    
            if ok:
                print(f'Training Random Forest no SM ...')
                rf.training_(include_optimisation=False)                 
                print('Scores')            
                print(f'Done')   

        rf.test_on_unseen_data(unseen_data_path=self.holdout_data_path, unselected_features=unselected_features)
        
        export_predicted_values_path = rf'{self.output_data_folder}{output_file_name}'
        return export_predicted_values_path

    def run_LR(self):
        smlr = SoilMoinstureLinearRegression(
            training_data_path=self.training_data_path,        
            target_column=self.target_column,
            holdout_data_path=self.holdout_data_path,
            dates_columns=self.dates_columns,        
            output_file_name="linear_regression_output.csv",    
            output_folder_name=self.output_data_folder,    
            data_split=0.2,        
        )       
        ok = smlr.pre_process()
        
        if ok:
            print(f'Training Linear Regression..')
            smlr.training_(show_plotting=True)                          
            print(f'Done Linear Regression')        
             
    