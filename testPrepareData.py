import pandas as pd
import unittest

from pandas import DataFrame
from simulations.entities.Simulator import Simulator

from simulations.utils.DataAdapter import DataAdapter




class TestPrepareData(unittest.TestCase):

    import_data_path:str = "C:\\Users\\franc\\Desktop\\xaquow-backend\\RF_with_SM_import_test1.csv"
    output_data:str = "C:\\Users\\franc\\Desktop\\xaquow-backend"
    data_adapter: DataAdapter = None
    simualtor: Simulator = None


    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.data_adapter = DataAdapter(self.import_data_path, self.output_data)
        

    def test_prepare_data_correct_data_path(self):
        _import_data_path:str = "C:\\Users\\franc\\Desktop\\xaquow-backend\\RF_with_SM_import_test.csv"
        _output_data:str = "C:\\Users\\franc\\Desktop\\xaquow-backend"
        _simulator = Simulator(_import_data_path, _output_data)
        

        _simulator.prepare_data()

        simulation_input_dataframe = _simulator.simulation_input_dataframe

        self.assertTrue(simulation_input_dataframe is not None)

    def test_prepare_data_not_existing_import_path(self):
        _import_data_path:str = "C:\\Users\\franc\\Desktop\\xaquow-backend\\RF_with_SM_import_test1.csv"
        _output_data:str = "C:\\Users\\franc\\Desktop\\xaquow-backend"
        _simulator = Simulator(_import_data_path, _output_data)

        ok = _simulator.prepare_data()

        simulation_input_dataframe = _simulator.simulation_input_dataframe

        self.assertFalse(ok)

    def test_prepare_data_not_existing_output_path(self):
        _import_data_path:str = "C:\\Users\\franc\\Desktop\\xaquow-backend\\RF_with_SM_import_test.csv"
        _output_data:str = "C:\\Users\\franc\\Desktop\\xaquow-backend3"
        _simulator = Simulator(_import_data_path, _output_data)

        ok = _simulator.prepare_data()

        simulation_input_dataframe = _simulator.simulation_input_dataframe

        self.assertFalse(ok)
        
    

if __name__ == '__main__':
    unittest.main()
