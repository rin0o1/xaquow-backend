from machine_learning.entities.SoilMoinstureModelsHandler import SoilMoistureModelsHandler
from simulations.entities.Simulator import Simulator
from simulations.models.SimulatorParametersModel import SimulatorParametersModel
from pandas import DataFrame

class SimulationHandler:
    
    models_handler: SoilMoistureModelsHandler = None
    simulator: Simulator = None
    output_folder: str = ""    

    def __init__(self, output_folder:str) -> None:
        self.output_folder = output_folder
        #self.init_model_handler(output_folder)

    def init_model_handler(self, output_folder:str) -> None:
        self.models_handler = SoilMoistureModelsHandler(output_folder)    
        pass

    def init_simulation(self, simulation_import_file:str) -> None:
        self.simulator = Simulator(simulation_import_file, self.output_folder)        

    def run_prediction(self) -> str:
        simulation_prediction_output = self.models_handler.run_RF_with_SM(use_cached_model=True)
        simulation_import_file = simulation_prediction_output
        simulation_import_file = "C:\\Users\\franc\\Desktop\\xaquow-backend\\RF_with_SM_output.csv"
        return simulation_import_file

    def create_simulation(self, simulation_parameters: SimulatorParametersModel) -> bool:
        try:
            simulation_import_file = self.run_prediction()
            self.init_simulation(simulation_import_file)
            ok = self.simulator.create_simulation_model(simulation_parameters)        
            return True
        except e as Exception:
            return False

    def run_simulation(self, simulation_export_file_name:str = None):
        self.simulator.run_simulation(simulation_export_file_name)

    def run_simulation_with_results(self, simulation_export_file_name:str = None):
        return self.simulator.run_simulation_with_results(True, simulation_export_file_name)
    

    