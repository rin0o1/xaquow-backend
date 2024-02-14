import os
import pandas as pd
from aquacrop.core import AquaCropModel
from aquacrop.utils import prepare_weather, get_filepath
from aquacrop.entities.crop import Crop
from aquacrop.entities.soil import Soil
from aquacrop.entities.inititalWaterContent import InitialWaterContent
from aquacrop.entities.irrigationManagement import IrrigationManagement
from pandas import DataFrame
import pandas as pd
from simulations.utils.DataAdapter import DataAdapter
from simulations.models.SimulatorParametersModel import SimulatorParametersModel
from aquacrop.utils import prepare_weather, get_filepath


class Simulator:
    """
    Aquacrop simulator

    Parameters:
        import_data_path (str): ML algorithms output
        export_data_path (str): output folder
    """

    import_data_path: str = ""
    export_data_path: str = ""
    weather_input_df: "DataFrame" = None    
    data_adapter: "DataAdapter" = None        
    model: "AquaCropModel" = None
    simulation_input_dataframe = None

    def __init__(
        self, 
        import_data_path: str, 
        export_data_path: str = '',        
    ) -> None:            
        self.import_data_path = import_data_path
        self.export_data_path = export_data_path        
        self.prepare_data()
        self.total_precipitation = 145.6

    def prepare_data(self) -> bool:        
        if not self.file_exist(self.export_data_path) or not self.file_exist(self.import_data_path):        
            print("This folder does not exist.")
            return False            
        
        self.data_adapter = DataAdapter(self.import_data_path, self.export_data_path)        
        migrated_weather_data_path = self.data_adapter.load()
        
        if migrated_weather_data_path is not None:
            print(f'Your data for the simulation has been saved in {migrated_weather_data_path}.')
            try:
                print(f'Checking data for the simulation')
                input_path = get_filepath(migrated_weather_data_path)
                self.simulation_input_dataframe = prepare_weather(input_path)                        
                if self.simulation_input_dataframe is not None:
                    self.current_soil_moisture_values, self.predicted_soil_moisture_values = self.data_adapter.get_all_soil_moisture_values()        
                    print(f'Your data is ready for simulation. Create the simulation model to get started.')                                             
                    return True
                else:
                    print(f'Some errore occured on prearing your data')
                    return False
            except Exception as e:
                print(f'Some errore occured on prearing your data. {e}')
                return False
    
    def file_exist(self, file_path:str) -> bool:
        return os.path.exists(file_path)

                                       
    def create_simulation_model(self, simulation_parameters: SimulatorParametersModel) -> bool:        
        s_p = simulation_parameters
        try:
            crop = Crop(s_p.crop, s_p.planting_date)
            soil = Soil(s_p.soil)        
            init_wc = InitialWaterContent(
                wc_type='Num', 
                value=[self.current_soil_moisture_values[0]/100]
            )
            irr_man = IrrigationManagement(
                irrigation_method=1,
                SMT=s_p.soil_moisture_target
            )

            self.model = AquaCropModel(            
                sim_start_time=s_p.start_simulation_date,
                sim_end_time=s_p.end_simulation_date,
                weather_df=self.simulation_input_dataframe,
                soil=soil,
                crop=crop,
                irrigation_management=irr_man,
                initial_water_content=init_wc,
                SMs=self.current_soil_moisture_values,
                FSMs=self.predicted_soil_moisture_values,
                TYPE=s_p.simulation_type
            )
            print(f'Simulation model created with success.')
            return True
        except Exception as e:
            print(f'Some errors occured on creating the simulation model. {e}')
            return False

    def run_simulation_with_results(
            self, return_model_results:bool, 
            simulation_export_file_name:str = None) :
        ok = self.run_simulation(simulation_export_file_name)

        if ok:
            if return_model_results:
                return self.get_model_results()            
        else:
            return None

    def run_simulation(self, simulation_export_file_name=None) -> bool:
        if self.model is not None:
            self.model.run_model(till_termination=True)
            if simulation_export_file_name is not None:
                self.data_adapter.export_simulation_results(self.model, simulation_export_file_name)
            print(f'Simulation exectued correctly. Simulation output saved in {self.export_data_path}')
            return True
        else:
            print(f'Please create a simulation model first. create_simulation_model()')
            return False
        
    def get_model_results(self) -> dict[float, float, float]:        
        simulation_results = self.model.get_simulation_results()                    
        yield_value = simulation_results.at[0, 'Yield (tonne/ha)']
        irrigation_value = simulation_results.at[0, 'Seasonal irrigation (mm)']
        IWUE = yield_value / (irrigation_value + self.total_precipitation) 
        return yield_value, irrigation_value, IWUE
    


