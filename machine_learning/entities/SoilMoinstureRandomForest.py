from pandas import DataFrame
from numpy import ndarray
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
import joblib
import numpy as np
import time
from machine_learning.entities.SoilMoistureBaseModel import SoilMoistureBaseModel

class SoilMoinstureRandomForest(SoilMoistureBaseModel):
    """
    This is the main class for Xaquo linear regression model.
    It is in charge of estimating the next day (t+1) 
    value from current (t) weather parameters. 

    Parameters:
        training_data_path (str): weather conditions for trainig           
        target_column (str): target column name
        dates_columns (ndarray): list of columns to be considered as dates
    """
    
        
    def run_model(self) -> None:  
        m_o = self.model_settings
        if m_o.include_optimisation:            
            self.run_random_forest_with_optimisation()
        else:   
            self.run_random_forest()
        

    def run_random_forest(self) -> None:      
        start_time = time.time()
        model = RandomForestRegressor(
            n_estimators=100, 
            random_state=42,                                                                          
        )            
        m_s = self.model_settings
        model.fit(m_s.X_train, m_s.Y_train)            
        Y_pred = model.predict(m_s.X_test)
        end_time = time.time()
        delta_time = end_time - start_time
        print(f"Total computational time: {delta_time:.2f} seconds")
        self.evaluate_model(m_s.Y_test, Y_pred)

        if m_s.show_plotting:            
            self.plot_learning_curve(model, m_s.X_train, m_s.Y_train)
            self.plot_feature_importance(model, m_s.X_train, m_s.X_train.columns)
            self.plot_wave(m_s.Y_test, Y_pred)

        joblib.dump(model, self.model_name)            

    
    def run_random_forest_with_optimisation(self) -> dict[str, str]:        
        param_grid = {
            'n_estimators': [50, 100, 150, 200],
            'max_depth' : [30, 40, 50]
        }
        model = RandomForestRegressor(random_state=42, max_samples=20000)
        m_s = self.model_settings
        scoring = 'neg_mean_squared_error'
        grid_search = GridSearchCV(model, param_grid, scoring=scoring, cv=2)
        grid_search.fit(m_s.X_train, m_s.Y_train)        
        results = {
            'best_params': grid_search.best_params_,
            'best_score': grid_search.best_score_,
            'cv_results': grid_search.cv_results_,
            'test_predictions': grid_search.best_estimator_.predict(m_s.X_test),
            'test_labels': m_s.Y_test
        }        
        print("Grid Search Results:")
        for i, params in enumerate(grid_search.cv_results_['params']):
            print(f"Parameters: {params}, Mean Squared Error: {-grid_search.cv_results_['mean_test_score'][i]}")        
        results_df = pd.DataFrame({
            'best_params': [results['best_params']],
            'best_score': [results['best_score']],
            'cv_results': [results['cv_results']],
            'test_predictions': [results['test_predictions']],
            'test_labels': [results['test_labels']]
        })
        results_df.to_csv('grid_search_results.csv', index=False)        
        print("\nBest Parameters:", results['best_params'])
        print("Best Score:", results['best_score'])        
        self.evaluate_model(results['test_labels'], results['test_predictions'])
        self.model = grid_search.best_estimator_
        return results    
            

    def plot_wave(self, Y_test: DataFrame, Y_pred: DataFrame, num_rows: int=100) -> None:                
        ID = list(range(1, num_rows + 1))                
        Y_test_subset = Y_test[:num_rows]
        Y_pred_subset = Y_pred[:num_rows]                
        sd = np.std(Y_test_subset)                
        plt.plot(ID, Y_test_subset, label='Y_test', marker='o', linestyle='-', color='blue')
        plt.plot(ID, Y_pred_subset, label='Y_pred', marker='x', linestyle='-', color='orange')        
        plt.fill_between(ID, np.array(Y_test_subset) - sd, np.array(Y_test_subset) + sd, color='gray', alpha=0.3, label='SD')        
        plt.xlabel('ID')
        plt.ylabel('Soil Moinsture (m³/m³)')
        plt.title('Y_test and Y_pred Comparison with SD (First 100 Rows)')        
        metrics_text = f"RMSE: {self.rmse:.4f}\nR^2: {self.r2:.4f}\nMAE: {self.mae:.4f}"
        plt.text(num_rows, min(Y_test_subset), metrics_text, ha='right', va='bottom', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
        plt.legend()        
        plt.show()


    def plot_learning_curve(self, model: RandomForestRegressor, X_train: DataFrame, Y_train: DataFrame) -> None:                
        train_sizes = np.linspace(.1, 1.0, 3)
        train_sizes, train_scores, test_scores = learning_curve(
            model, X_train, Y_train, cv=5, scoring='neg_mean_squared_error',
            n_jobs=-1, train_sizes=train_sizes
        )
        train_scores_mean = -np.mean(train_scores, axis=1)
        test_scores_mean = -np.mean(test_scores, axis=1)
        plt.figure(figsize=(12, 6))
        plt.plot(train_sizes, train_scores_mean, label='Training error')
        plt.plot(train_sizes, test_scores_mean, label='Cross-validation/Test set error')
        plt.xlabel('Training Set Size')
        plt.ylabel('Mean Squared Error')
        plt.title('Learning Curve for Random Forest Model2')
        plt.legend()
        plt.show()


    def plot_feature_importance(self, model: RandomForestRegressor, X_train: DataFrame, feature_names: ndarray) -> None:
        importances = model.feature_importances_
        indices = np.argsort(importances)[::-1]
        print('Featue importance result')
        print(importances)
        print(feature_names)
        print(feature_names)
        plt.figure(figsize=(12, 6))
        plt.bar(range(X_train.shape[1]), importances[indices], align='center')
        plt.xticks(range(X_train.shape[1]), [feature_names[i] for i in indices], rotation=90)
        plt.xlabel('Feature Importance')
        plt.ylabel('Feature')
        plt.title('Feature Importance for Random Forest')
        plt.show()
            
   
    def test_on_unseen_data(self, unseen_data_path:str = None, unselected_features:ndarray = None) -> None:                       

        if not self.generate_hold_out_sample and unseen_data_path is None:
            print('Either you provide an external dataset or you set generate_hold_out_sample to True')        
            return

        data, e = self.read_data_from_path(unseen_data_path or self.holdout_data_path)                              
        data_default = data.copy()

        if unseen_data_path is not None:                        
            data_default, e = self.perform_target_variable_preparation(data_default)
            data = self.pre_process(data=data, unselected_features=unselected_features)                                    
                            
        X, Y = self.training_set(data)                
        self.model = joblib.load(filename='machine_learning/RF_model_no_SM')
        Y_pred = self.model.predict(X)        
        self.evaluate_model(Y, Y_pred)  
        self.plot_wave(Y, Y_pred)   
        predicted_column_name = self.predicted_column_name
        data_default[predicted_column_name] = Y_pred
        export_file_name = self.output_folder_name + self.output_file_name
        data_default.to_csv(export_file_name, index=False)  
        