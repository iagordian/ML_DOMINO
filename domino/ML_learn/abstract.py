
from schemas import ML_Object

from abc import ABC
import io
import joblib

class LearningObject(ABC):
    model_obj_type = None
    model_params = {}
    
    def __init__(self):
        self.model_obj = self.model_obj_type(**self.model_params)
        self.model_name = self.model_obj_type.__name__
        self.log_data = {
            'model_name': self.model_name,
            **self.model_params
        }

    @property
    def data(self):
        return ML_Object(
            model_name=self.model_name,
            model_obj=self.to_bytes(),
            threshold=self.threshold,
            logs=self.log_data
        )

    def fit(self):
        self.model_obj.fit(self.train_data, self.train_target)

    def to_bytes(self):
        '''Сохранение модели в файл'''
        
        bytes_container = io.BytesIO()
        joblib.dump(self.model_obj, bytes_container)
        bytes_container.seek(0)

        return bytes_container.getvalue()
    
    


