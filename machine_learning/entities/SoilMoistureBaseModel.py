from machine_learning.utils.Constants import C
from pandas import DataFrame
from numpy import ndarray 
from machine_learning.utils.PreProcessing import PreProcessing
from machine_learning.utils.DataHandler import DataHandler
from machine_learning.models.ModelSettings import ModelSettings
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split

class SoilMoistureBaseModel(object):
   
    data_handler: DataHandler = None    
    pre_processing: PreProcessing = None    
    model_settings: ModelSettings = None

    def __init__(
        self,
        training_data_path: str,                
        target_column: str,
        holdout_data_path: str,
        dates_columns: "ndarray",
        output_file_name: str, 
        output_folder_name: str,
        data_split: float,
        generate_hold_out_sample: bool = False,
        model_name: str = ""
    ) -> None:        
        self.default_data_split:float = data_split
        self.training_data_path: str = training_data_path
        self.target_column: str = target_column        
        self.dates_columns: "ndarray" = dates_columns
        self.training_data: "DataFrame" = []        
        self.holdout_data_path: str = holdout_data_path        
        self.generate_hold_out_sample = generate_hold_out_sample
        self.output_file_name: str = output_file_name
        self.output_folder_name = output_folder_name
        self.model_name = model_name

        self.predicted_column_name = C.SOIL_MOINSTURE_MODELS_PREDICTED_COLUMN_NAME        

        self.data_handler = DataHandler()
        self.pre_processing = PreProcessing()
        self.training_data, e = self.read_data_from_path() 

        if e != None:
            print(e)

    def read_data_from_path(self, path: str = None) -> (DataFrame, str):        
        data, e = self.data_handler.from_path_to_dataframe(path or self.training_data_path)         

        if e != None:
            print(f'Some errors occured while reading data from: {self.training_data_path}')

        return data, e       

    def pre_process(self, unselected_features: ndarray = [], data: DataFrame = None):      
        print('Starting pre_processing...')        

        if data is not None:
            return self.perform_pre_process(data, unselected_features)
        else:
            data = self.training_data                    
            self.training_data = self.perform_pre_process(data, unselected_features)
            return True
            
    def perform_pre_process(self, data: DataFrame, unselected_features: ndarray) -> DataFrame:                                 
        data, e = self.pre_processing.set_ids(data)           
        data, e = self.pre_processing.handle_dates(data, self.dates_columns)        
        data, e = self.perform_target_variable_preparation(data)
        data, e = self.pre_processing.feature_selection(data, unselected_features)        
        data, e = self.pre_processing.clean_data(data)          

        if self.generate_hold_out_sample:
            self.pre_processing.export_random_rows_to_csv(data, 100, self.holdout_data_path)
        
        if e!= None:
            print(e)
            return False
                
        return data
    
    def perform_target_variable_preparation(self, data: DataFrame) -> (DataFrame, str):
        data, e = self.pre_processing.prepare_target_variable(data, self.target_column)                  

        return data, e

    def training_(self, include_optimisation:bool = False, show_plotting:bool = False):        
        self.X, self.Y = self.prepare_data(self.training_data)                           
        X_train, X_test, Y_train, Y_test = train_test_split(
            self.X,
            self.Y, 
            test_size = self.default_data_split, 
            random_state=42
        )        
        X_train = X_train.dropna()
        Y_train = Y_train[X_train.index]
        X_test = X_test
        Y_test = Y_test[X_test.index]
        self.model_settings: ModelSettings = ModelSettings(
            X_train = X_train,
            Y_train = Y_train,
            X_test = X_test,
            Y_test = Y_test,
            include_optimisation = include_optimisation,
            show_plotting = show_plotting
        )        
        self.run_model()
        return True

    def prepare_data(self, data: DataFrame) -> (DataFrame, DataFrame):        
        Y = data[self.target_column]    
        X = data.drop(columns=[self.target_column, 'ID'])
            
        return X, Y
    
    def evaluate_model(self, Y_test: DataFrame, Y_pred: DataFrame):
        rmse = mean_squared_error(Y_test, Y_pred, squared=False)
        r2 = r2_score(Y_test, Y_pred)
        mae = mean_absolute_error(Y_test, Y_pred)   
        self.rmse = rmse
        self.r2 = r2
        self.mae = mae             
        print(f"Mean Absolute Error: {mae}")
        print(f"R-squared: {r2}")
        print(f"Root mean squared error: {rmse}")

