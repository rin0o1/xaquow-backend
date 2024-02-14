


class SimulatorParametersModel:

    def __init__(
            self,            
            start_simulation_date: str,
            end_simulation_date: str,
            planting_date: str,
            simulation_type: int,
            crop: str,
            soil: str,
            soil_moisture_target: [] = [],

    ) -> None:
        self.soil_moisture_target = soil_moisture_target
        self.start_simulation_date = start_simulation_date
        self.end_simulation_date = end_simulation_date
        self.planting_date = planting_date
        self.simulation_type = simulation_type
        self.crop = crop
        self.soil = soil