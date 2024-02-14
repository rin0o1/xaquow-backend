from simulations.entities.SimulationHandler import SimulationHandler
from simulations.models.SimulatorParametersModel import SimulatorParametersModel
from optimisations.RHMC import RHMC

if __name__ == "__main__":
    simulation_parameters = SimulatorParametersModel(        
        start_simulation_date='2023/05/01',
        end_simulation_date='2023/09/11',
        planting_date='05/01',
        simulation_type=1,
        crop='PotatoLocal',
        soil="SiltLoam"
    )
    solutions_iwue = []
    solutions_irr_vs = []
    solutions_y_vs = []
    solutions_SMTS = []
    for x in range(0,100): 
        o = RHMC(100, simulation_parameters)
        best_sol_SMTS, old_sol_performance = o.run()           
        best_sol_y_v, best_solt_irr_v, old_sol_IWUE = old_sol_performance
        print(f'For Restart {x+1}: Best SMTS {best_sol_SMTS} with a WE {old_sol_IWUE} a Y : {best_sol_y_v} and Irr : {best_solt_irr_v}')
        solutions_iwue.append(old_sol_IWUE)      
        solutions_SMTS.append(best_sol_SMTS) 
        solutions_irr_vs.append(best_solt_irr_v)
        solutions_y_vs.append(best_sol_y_v)

    print('IWUE values')
    print(solutions_iwue)
    print('Irr values')
    print(solutions_irr_vs)
    print('Y values')
    print(solutions_y_vs)
    print('SMTS')
    print(solutions_SMTS)

    best_sol_we = 0
    best_sol_idx = -1
    for i in range(0, len(solutions_iwue)):
        e = solutions_iwue[i]
        if e > best_sol_we:
            best_sol_idx = i
            best_sol_we = e

    print(f'Best SMTS {solutions_SMTS[best_sol_idx]} with a WE {best_sol_we} a Y : {solutions_y_vs[best_sol_idx]} and Irr : {solutions_irr_vs[best_sol_idx]}')
    
        
