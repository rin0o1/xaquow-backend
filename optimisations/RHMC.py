from optimisations.Solution import Solution
from simulations.models.SimulatorParametersModel import SimulatorParametersModel
class RHMC:

    _default_plating_date: str = '05/01'
    _default_start_simulation: str = '2023/05/01'
    _default_end_simulation: str = '2023/09/11'
  

    def __init__(self, no_runs: int, simulation_parameters: SimulatorParametersModel) -> None:
        self.no_runs = no_runs        
        self.output_folder = "C:\\Users\\franc\\Desktop\\xaquow-backend\\"
        self.simulation_parameters = simulation_parameters


    def run(self) -> []:
        old_sol_simulation_parameters = self.simulation_parameters
        old_sol = Solution(old_sol_simulation_parameters, output_folder=self.output_folder)
        old_sol.generate_random_targets()
        old_sol.init_simulator()
        old_sol_f = old_sol.perform_fitness()
        

        for i in range (self.no_runs):
            new_sol_simulation_parameters = self.simulation_parameters
            new_sol_simulation_parameters.soil_moisture_target = old_sol.get_SMTS()            
            new_sol = Solution(new_sol_simulation_parameters, i, self.output_folder)
            new_sol.init_simulator()
            new_sol.small_change()
            new_sol_f = new_sol.perform_fitness()
            print(new_sol_f)
            if new_sol_f is None:
                print('Some errors occured during the optimisation.')
                return 
            # Maximising IWUE
            if (new_sol_f > old_sol_f):
                new_SMTS = new_sol.get_SMTS()        
                print(f'Better SMTS found: {new_SMTS} with a IWUE of {new_sol_f}')                
                old_sol = new_sol
                old_sol_f = new_sol_f
        
        return old_sol.get_SMTS(), old_sol.get_performance_data()