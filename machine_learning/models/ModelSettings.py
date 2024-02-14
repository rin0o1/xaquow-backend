
class ModelSettings:
    def __init__(self, 
            X_train: "DataFrame", 
            Y_train: "DataFrame", 
            X_test: "DataFrame", 
            Y_test: "DataFrame", 
            include_optimisation:bool, 
            show_plotting:bool):
        
        self.X_train = X_train
        self.Y_train = Y_train
        self.X_test = X_test
        self.Y_test = Y_test
        self.include_optimisation = include_optimisation
        self.show_plotting = show_plotting
