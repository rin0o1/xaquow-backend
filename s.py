from simulations.entities.SimulationHandler import SimulationHandler
from simulations.models.SimulatorParametersModel import SimulatorParametersModel
from optimisations.RHMC import RHMC

if __name__ == "__main__":
    s = SimulationHandler("C:\\Users\\franc\\Desktop\\xaquow-backend\\")
    
    simulation_parameters = SimulatorParametersModel(
        soil_moisture_target=[15, 15, 15, 15],
        start_simulation_date='2023/05/01',
        end_simulation_date='2023/09/11',
        planting_date='05/01',
        simulation_type=0,
        crop='PotatoLocal',
        soil="SiltLoam"
    )

    ok = s.create_simulation(simulation_parameters)
    if ok:
        yield_value, irrigation_value, IWUE = s.run_simulation_with_results()
        print(IWUE)
        print(irrigation_value)
        print(yield_value)
        print('done')