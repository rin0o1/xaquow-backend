import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from machine_learning.entities.SoilMoistureBaseModel import SoilMoistureBaseModel

class SoilMoinstureLinearRegression(SoilMoistureBaseModel):
    """
    This is the main class for Xaquo linear regression model.
    It is in charge of estimating the next day (t+1) 
    value from current (t) weather parameters. 

    Parameters:
        training_data_path (str): weather conditions for trainig       
        target_data_path (str): weather conditions for testing
        target_column (str): target column name
        dates_columns (ndarray): list of columns to be considered as dates
    """
        
    model: "LinearRegression" = None


    def run_model(self):      
        m_s = self.model_settings
        model = LinearRegression()
        model.fit(m_s.X_train, m_s.Y_train)        
        self.Y_pred = model.predict(m_s.X_test)                    
        self.evaluate_model(m_s.Y_test, self.Y_pred)    
        self.model = model                  

        if m_s.show_plotting:
            self.feature_importance()
                
                
    def feature_importance(self):
        X = self.X
        model = self.model
        coefficients = model.coef_
        exponential_coefficients = np.exp(coefficients)        
        feature_importance = list(zip(X.columns, exponential_coefficients))
        feature_importance.sort(key=lambda x: abs(x[1]), reverse=True)        
        print(feature_importance)
        print(exponential_coefficients)
        plt.figure(figsize=(10, 6))
        plt.barh(X.columns, exponential_coefficients)
        plt.xlabel('Coefficient Value')
        plt.ylabel('Feature')
        plt.title('Feature Importance')
        plt.show()

    def plot_moisture_over_time(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.Y, self.Y_pred, label='Y_pred', linestyle='-', marker='o', color='blue')
        plt.plot(self.data['timestamp'], self.Y, label='Y_train', linestyle='-', marker='o', color='green')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Y_pred and Y_train Over Time')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)  
        plt.show()
        
        
    # def next_7_days_soil_moisture(self, target_data_path):
    #     self.target_data_path = target_data_path
    #     self.next_7_days_soil_moisture()

        
