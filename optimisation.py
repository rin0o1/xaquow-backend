
from optimisations.RHMC import RHMC

if __name__ == "__main__":
    print(f'Init simulation process')
    hc = RHMC(no_runs=1000)
    print(f'Start running simulation')
    hc.run()
    
    