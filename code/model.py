from abc import ABCMeta, abstractmethod

class AbstractModel(metaclass=ABCMeta):
    def __init__(self, name_fold):
        self.name_fold = name_fold
        self.model = None
    
    @abstractmethod
    def train(self, X_tr, y_tr, X_va, y_va, params, train_params):
        pass

    @abstractmethod
    def predict(self, X):
        pass
    
    @abstractmethod
    def get_score(self):
        pass
    
    @abstractmethod
    def save_model(self):
        pass
    
    @abstractmethod
    def load_model(self):
        pass 
    
    @property
    def feature_importance_(self):
        pass