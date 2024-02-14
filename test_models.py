
from machine_learning.entities.SoilMoinstureModelsHandler import SoilMoistureModelsHandler


models_handler = SoilMoistureModelsHandler("C:\\Users\\franc\\Desktop\\xaquow-backend\\")
print(models_handler.run_RF_no_SM(use_cached_model=True))