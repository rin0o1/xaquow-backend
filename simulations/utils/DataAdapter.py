import pandas as pd
from pandas import DataFrame
from .Constants import C
import os

class DataAdapter:
    
    weather_input_df: "DataFrame" = None
    weather_export_df: "DataFrame" = None
    current_soil_moinsture_values = []
    predicted_soil_moinsture_values = []
    import_data_path: str = ""
    export_data_path: str = ""

    def __init__(
            self, 
            import_data_path: str, 
            export_data_folder: str = '',
        ) -> None:
        
        if os.path.exists(import_data_path):            
            self.weather_input_df = pd.read_csv(import_data_path)
            self.export_data_folder = export_data_folder
            
            
        else:
            print(f'Error on opening {import_data_path}. \
                    Please enter a valid weather file input')
    
    def load(self) -> str:        
        self.init_export_dataframe()                        
        self.export_migration_path = self.export_data_folder + C.DATA_ADAPTER_EXPORT_FILE_NAME

        # Merge hours in days
        days_df, error_on_merging = self.merge_hours_into_days()
        if error_on_merging is not None:
            print(f'Error on grouping weather by date. {error_on_merging}')
            return None
        
        # Perform migation form import dataframe to export dataframe
        error_on_migrating = self.perform_migration(days_df=days_df)
        if error_on_migrating is not None:
            print(f'Error on migrating. {error_on_migrating}')
            return None
        
        # Adjust types
        error_on_adjusting_types = self.adjust_exported_types()
        if error_on_adjusting_types is not None:
            print(f'Error on exporting. {error_on_adjusting_types}')
            return None
        
        # Save as csv file on disk       
        error_on_saving_df_as_csv = self.save_export_df_as_csv()
        if error_on_saving_df_as_csv is not None:
            print(f'Error on saving dataframe as csv. {error_on_saving_df_as_csv}')
            return None
        
        print(f'Migration completed with success.')

        return self.export_migration_path        

    def perform_migration(self, days_df: "DataFrame") -> str:
        error_on_migrating = None        

        for day, daily_weather in days_df:
            error_on_migrating = self.perform_single_day_migration(daily_weather)               

            if error_on_migrating is not None:                
                return f'Error on migrating: {error_on_migrating}'
            
            current_soil_moinsture_value, error_on_migrating = self.add_soil_moinsture(daily_weather, 'Basilea Soil Moisture [0-10 cm down]')            

            if error_on_migrating is not None:
                return f'Error on exporting current soil moisture values. {error_on_migrating}'            
            
            self.current_soil_moinsture_values.append(current_soil_moinsture_value)
            predicted_soil_moinsture_value, error_on_migrating = self.add_soil_moinsture(daily_weather, 'predicted_soil_m')            

            if error_on_migrating is not None:
                return f'Error on exporting predicted soil moisture values. {error_on_migrating}'
            
            self.predicted_soil_moinsture_values.append(predicted_soil_moinsture_value)

            if error_on_migrating is not None:
                return f'Error on reading SM: {error_on_migrating}'          
            
        return error_on_migrating

    def save_export_df_as_csv(self) -> str:
        error_on_saving_df_as_csv = None
        try:
            self.weather_export_df.to_csv(
                path_or_buf=self.export_migration_path,
                index=False,
                sep='\t'
            )              
        except Exception as e:
            error_on_saving_df_as_csv = e

        return error_on_saving_df_as_csv

    def adjust_exported_types(self) -> str:           
        error_on_adjusting_types = None
        try:                    
            self.weather_export_df[C.DATA_APTER_EXPORT_DAY] = \
            self.weather_export_df[C.DATA_APTER_EXPORT_DAY].astype(int)

            self.weather_export_df[C.DATA_APTER_EXPORT_MONTH] = \
            self.weather_export_df[C.DATA_APTER_EXPORT_MONTH].astype(int)

            self.weather_export_df[C.DATA_APTER_EXPORT_YEAR] = \
            self.weather_export_df[C.DATA_APTER_EXPORT_YEAR].astype(int)

            self.weather_export_df[C.DATA_APTER_EXPORT_TMIN] = \
            self.weather_export_df[C.DATA_APTER_EXPORT_TMIN].round(2)

            self.weather_export_df[C.DATA_APTER_EXPORT_TMAX] = \
            self.weather_export_df[C.DATA_APTER_EXPORT_TMAX].round(2)

            self.weather_export_df[C.DATA_APTER_EXPORT_PREC] = \
            self.weather_export_df[C.DATA_APTER_EXPORT_PREC].round(2)

            self.weather_export_df[C.DATA_APTER_EXPORT_ET0] = \
            self.weather_export_df[C.DATA_APTER_EXPORT_ET0].round(2) 
          
        except Exception as e:
            error_on_adjusting_types = e

        return error_on_adjusting_types

    def init_export_dataframe(self) -> bool:
        self.weather_export_df = pd.DataFrame()        
        self.weather_export_df[C.DATA_APTER_EXPORT_DAY] = []
        self.weather_export_df[C.DATA_APTER_EXPORT_MONTH] = []
        self.weather_export_df[C.DATA_APTER_EXPORT_YEAR] = []
        self.weather_export_df[C.DATA_APTER_EXPORT_TMIN] = []
        self.weather_export_df[C.DATA_APTER_EXPORT_TMAX] = []        
        self.weather_export_df[C.DATA_APTER_EXPORT_PREC] = []        
        self.weather_export_df[C.DATA_APTER_EXPORT_ET0] = []                

    def merge_hours_into_days(self) -> ("DataFrame", str):
        err = None
        days_df = None
        # Convert dates
        try:
            self.weather_input_df['timestamp'] = pd.to_datetime(
                self.weather_input_df['timestamp'], 
                format="mixed"
            )              
            days_df = self.weather_input_df.groupby(
                self.weather_input_df['timestamp'].dt.date
            )        
        except Exception as e:
            err = e            

        return days_df, err

    def perform_single_day_migration(self, daily_weather: "DataFrame") -> str:
        err = None

        try:
            min_temp = min(daily_weather[C.DATA_ADAPTER_IMPORT_TEMP])
            max_temp = max(daily_weather[C.DATA_ADAPTER_IMPORT_TEMP])
            total_precipitation = sum(daily_weather[C.DATA_ADAPTER_IMPORT_PREC])
            total_et0 = sum(daily_weather[C.DATA_ADAPTER_IMPORT_ET])
            year = int(daily_weather[C.DATA_ADAPTER_IMPORT_TIME].dt.year.unique()[0])        
            month = int(daily_weather[C.DATA_ADAPTER_IMPORT_TIME].dt.month.unique()[0])        
            day = int(daily_weather[C.DATA_ADAPTER_IMPORT_TIME].dt.day.unique()[0])        

            entry = {                                
                C.DATA_APTER_EXPORT_DAY: day,
                C.DATA_APTER_EXPORT_MONTH: month,
                C.DATA_APTER_EXPORT_YEAR: year,
                C.DATA_APTER_EXPORT_TMIN: min_temp,
                C.DATA_APTER_EXPORT_TMAX: max_temp,
                C.DATA_APTER_EXPORT_PREC: total_precipitation,
                C.DATA_APTER_EXPORT_ET0: total_et0
            }
            self.weather_export_df = self.weather_export_df._append(
                entry, 
                ignore_index=True
            )

        except Exception as e:
            err = e

        return err
      
    def add_soil_moinsture(self, daily_weather: "DataFrame", soil_moisture_param:str) -> (DataFrame, str):
        error_on_reading_soil_moinsture = None
        max_soil_moisture = 0
        try:            
            daily = daily_weather[soil_moisture_param]        
            max_soil_moisture = max(daily)*100
        except Exception as e:
            error_on_reading_soil_moinsture = e

        return max_soil_moisture, error_on_reading_soil_moinsture
    
    def get_all_soil_moisture_values(self) -> (DataFrame, DataFrame):
        return self.current_soil_moinsture_values, self.predicted_soil_moinsture_values
    
    def export_simulation_results(self, model, file_name=None) -> bool:
        error_on_exporting_simulation_results = None
        try:
            _water_storage = model.get_water_storage()
            _water_flux = model.get_water_flux()
            _crop_growth = model.get_crop_growth()
            _simulation_results = model.get_simulation_results()
            full_data_output = pd.concat(
                [
                    _water_storage,
                    _water_flux,
                    _crop_growth,
                    _simulation_results
                ],
                axis=1
            )   
            EXPORT_SIMULATION_RESULTS_FILE = ''
            if file_name is not None:
                EXPORT_SIMULATION_RESULTS_FILE = self.export_data_folder + file_name
            else:
                EXPORT_SIMULATION_RESULTS_FILE = self.export_data_folder + C.DATA_ADAPTER_EXPORT_SIMULATION_FILE_NAME
                
            full_data_output.to_csv(EXPORT_SIMULATION_RESULTS_FILE, index=False)
            print(f'Simulation exported with success')
            return True
        
        except Exception as e:
                error_on_exporting_simulation_results = e
                print(error_on_exporting_simulation_results)
                return False
        
        
