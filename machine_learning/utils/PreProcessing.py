from pandas import DataFrame
from numpy import ndarray
import pandas as pd
from  machine_learning.utils.Constants import C

class PreProcessing:
    """
    This is the class to clean the historical data given
    as input to the models

    Parameters:
        
    """

    __default_id_column: str = C.PRE_PROCESSING_DEFAULT_ID_COLUMN    

    def set_ids(self, data: "DataFrame") -> ("DataFrame", str):
        error = None
        try:
            data[self.__default_id_column] = range(1, len(data) + 1)    
        except Exception as _e:
            print(_e)
            error = 'Error on setting unique ids'

        return data, error

    def handle_dates(self, data: "DataFrame", dates_columns: "ndarray") -> ("DataFrame", str):         
        dates_columns = dates_columns
        error = None
        
        for i in range(0, len(dates_columns)):                
            c = dates_columns[i]            
            data[c] = pd.to_datetime(data[c], format="mixed")
            c_name_suffix = "_"*i            
            data[f'month{c_name_suffix}'] = data[c].dt.month            
            data = data.drop(columns=[c])        

        return data,error
    
    def feature_selection(self, data: "DataFrame", unselected_features:"ndarray") -> ("DataFrame", str):
        error = None
        try:                  
            data = data.drop(columns=unselected_features)
            return data, None
        except:
            error = 'Error on feature selection'
            return None, error


    def clean_data(self, data: "DataFrame") -> ("DataFrame", str):
        error = None
        try:
            data = data.dropna()
        except:
            error = 'Erorr on cleaning data'

        return data, error
        
    def prepare_target_variable(self, data : "DataFrame", target_variable: str)-> ("DataFrame", str):
        error = None
        try:
            data[target_variable] = data[C.SOIL_MOISTURE_VARIABLE].shift(-24)                     
            data['Basilea Soil Moisture [0-10 cm down] lag'] = data[C.SOIL_MOISTURE_VARIABLE].shift(24)
            data['Basilea Soil Moisture [0-10 cm down] lag3'] = data[C.SOIL_MOISTURE_VARIABLE].shift(72)            
            data = data.dropna()        
            return data, error    
        except:
            error = 'Erorr on cleaning data'

        return data, error
    
    def export_random_rows_to_csv(self, data, num_rows, csv_file_path):
        error = None
        
        try:
            if num_rows > len(data):
                error = 'Not enough rows'
            print('Before removal: ', len(data))
            random_rows = data.sample(n=num_rows, random_state=42)  
            random_rows.to_csv(csv_file_path, index=False, header=True)
            data = data.drop(random_rows.index)
            print('After removal: ', len(data))            
        
        except Exception as e:
            print(e)
            error = 'Error on export rows'
            
        

