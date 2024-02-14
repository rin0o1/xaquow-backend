import pandas as pd
from aquacrop.core import AquaCropModel
from aquacrop.entities.crop import Crop
from aquacrop.entities.soil import Soil
from aquacrop.entities.inititalWaterContent import InitialWaterContent
from aquacrop.entities.irrigationManagement import IrrigationManagement
from simulations.models.SimulatorParametersModel import SimulatorParametersModel
from simulations.entities.SimulationHandler import SimulationHandler
from numpy import ndarray
import random

class Solution:

    simulator_handler: SimulationHandler
    simulation_parameters: SimulatorParametersModel    

    def __init__(self, simulation_parameters: SimulatorParametersModel, S_NO = 0, output_folder: str = None):                        
        self._export_path: str = ''
        self._import_path: str = ''
        self.BASE_PATH = 'C:\\Users\\franc\\OneDrive - Brunel University London\\Aquo\\FYP\\project\\XAquo\\XAquo_test\\XAquo_test_ETo\\'
        self.SUB_FOLDER_INPUT = 'xaquow-backend\\optimisations\\input'
        self.SUB_FOLDER_OUTPUT = 'xaquow-backend\\optimisations\\output'
        self.IMPORT_FILE = '\\full_season_weather.csv'    
        self.S_NO = S_NO
        self.fitness = 0            
        self.simulation_parameters = simulation_parameters            
        self._export_path = output_folder + "optimisation\\output" or f'{self.BASE_PATH}{self.SUB_FOLDER_OUTPUT}'    
        self.simulator_handler = SimulationHandler(self._export_path)        
    
    def generate_random_targets(self) -> None:
        soil_moisture_targets = []
        for i in range(4):
            SMNT = random.randint(15,50)    
            soil_moisture_targets.append(SMNT)
        print(len(soil_moisture_targets))
        self.simulation_parameters.soil_moisture_target = soil_moisture_targets        

    def init_simulator(self) -> bool:
        return self.simulator_handler.create_simulation(self.simulation_parameters)
    
    def perform_fitness(self) -> float:        
        return self.run_model()

    def small_change(self) -> None:
        i = random.randint(0,3)
        SMNT = random.randint(15,50)    
        self.simulation_parameters.soil_moisture_target[i] = SMNT
        self.simulation_parameters.soil_moisture_target.sort()
    
    def get_SMTS(self) -> ndarray:
        return self.simulation_parameters.soil_moisture_target
         
    def get_performance_data(self) -> dict[float, float, float]:
        return self.yield_value, self.irrigation_value, self.IWUE
    
    def run_model(self) -> float:
        simulation_export_file_name = f'{self.simulation_parameters.soil_moisture_target}_{self.S_NO}.csv'
        yield_value, irrigation_value, IWUE = self.simulator_handler.run_simulation_with_results()        
        if yield_value is None or irrigation_value is None:
            print(f'Some errors occured while reading simulation results.')
            return None        
        self.yield_value = yield_value
        self.irrigation_value = irrigation_value
        self.IWUE = IWUE                            
        return IWUE
        

