from machine_learning.entities.SoilMoinstureModelsHandler import SoilMoistureModelsHandler
from simulations.entities.Simulator import Simulator
import sys

def build_string():
   BASE_PATH = f'C:\\Users\\franc\OneDrive - Brunel University London\\Aquo\\FYP\\project\\XAquo\\XAquo_test\\XAquo_test_ETo\\xaquow-backend\\machine_learning'
   OUTPUT_FOLDER = f'\\output\\'
   output_file_name = 'RF_with_SM_output.csv'
   export_predicted_values_path = rf'{BASE_PATH}{OUTPUT_FOLDER}{output_file_name}'
   return export_predicted_values_path
    

if __name__ == "__main__":

    BASE_PATH = 'C:\\Users\\franc\\OneDrive - Brunel University London\\Aquo\\FYP\\project\\XAquo\\XAquo_test\\XAquo_test_ETo\\'
    SUB_FOLDER_INPUT = 'xaquow-backend\\machine_learning\\output\\'
    SUB_FOLDER_OUTPUT = 'xaquow-backend\\simulations\\output'
    IMPORT_FILE = '\\RF_with_SM_output_after_refactoring.csv'
    EXPORT_FILE = '\\champion_climate_basilea.txt'    
    EXPORT_FULL_FOLDER = f'{BASE_PATH}{SUB_FOLDER_OUTPUT}'

    models_handler: SoilMoistureModelsHandler = SoilMoistureModelsHandler()
    IMPORT_FULL_PATH = models_handler.run_RF_with_SM(use_cached_model=True)
    
            
    s = Simulator(IMPORT_FULL_PATH, EXPORT_FULL_FOLDER)    
    s.create_simulation_model(        
        [30,30,30,30],
        '2023/05/01',
        '2023/09/11',
        '05/01'
    )
    s.run_simulation()



    
