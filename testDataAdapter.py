
import pandas as pd
import unittest

from pandas import DataFrame

from simulations.utils.DataAdapter import DataAdapter




class TestDataAdapter(unittest.TestCase):

    import_data_path:str = "C:\\Users\\franc\\Desktop\\xaquow-backend\\RF_with_SM_import_test.csv"
    output_data:str = "C:\\Users\\franc\\Desktop\\xaquow-backend\\RF_with_SM_output_test.csv"
    data_adapter: DataAdapter = None

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.data_adapter = DataAdapter(self.import_data_path, self.output_data)

    def test_adapt_soil_moisture_both_import_none_return_error(self):
        #Arrange
        _data_adapter:DataAdapter = self.data_adapter

        #Act
        max_soil_moisture, error = _data_adapter.add_soil_moinsture(None, None)

        #Assert
        self.assertTrue(error is not None)

    def test_adapt_soil_moisture_empty_soil_moisture_return_error(self):
        #Arrange
        _data_adapter = self.data_adapter

        #Act
        max_soil_moisture, error = _data_adapter.add_soil_moinsture([], None)

        #Assert
        self.assertTrue(error is not None)

    def test_adapt_soil_moisture_wrong_soil_moisture_parameter(self):
        #Arrange
        _data_adapter = self.data_adapter        
        df:DataFrame = pd.read_csv(self.import_data_path)
        if df is None: return

        daily_weather = df.sample(24)
        soil_moisture_parameter = "Wrong Soil Moisture Parameter"
            
        #Act
        max_soil_moisture, error = _data_adapter.add_soil_moinsture(daily_weather, soil_moisture_parameter)

        #Assert
        self.assertTrue(error is not None)
    
    
    def test_adapt_soil_moisture_correct_predict_soil_moisture(self):
        #Arrange
        _data_adapter = self.data_adapter        
        df:DataFrame = pd.read_csv(self.import_data_path)
        if df is None: return
        daily_weather = df.sample(24)        
        soil_moisture_parameter = "predicted_soil_m"
        print(daily_weather[soil_moisture_parameter].to_list())
        expected_output = max(daily_weather[soil_moisture_parameter]) * 100        
        print(f'Expected output {expected_output}')
        #Act
        max_soil_moisture, error = _data_adapter.add_soil_moinsture(daily_weather, soil_moisture_parameter)        
        print(f'Observed Output {max_soil_moisture}')
        #Assert
        self.assertTrue(expected_output == max_soil_moisture)

    def test_adapt_soil_moisture_correct_actual_soil_moisture(self):
        #Arrange
        _data_adapter = self.data_adapter        
        df:DataFrame = pd.read_csv(self.import_data_path)
        if df is None: return
        daily_weather = df.sample(24)        
        soil_moisture_parameter = "Basilea Next Day Soil Moisture [0-10 cm down]"
        print(daily_weather[soil_moisture_parameter].to_list())
        expected_output = max(daily_weather[soil_moisture_parameter]) * 100        
        print(f'Expected output {expected_output}')
        #Act
        max_soil_moisture, error = _data_adapter.add_soil_moinsture(daily_weather, soil_moisture_parameter)        
        print(f'Observed Output {max_soil_moisture}')

        #Assert
        self.assertTrue(expected_output == max_soil_moisture)

   
    

if __name__ == '__main__':
    unittest.main()
