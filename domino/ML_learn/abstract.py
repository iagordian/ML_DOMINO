
from domino.schemas import ML_Object
from domino.config import DATA_PACKAGES_DIR
from domino.files_navigation import join_file_path

from abc import ABC
import io
import joblib
from typing import ByteString, Optional

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
    def data(self) -> ML_Object:
        return ML_Object(
            model_name=self.model_name,
            model_obj=self.to_bytes(),
            threshold=self.threshold,
            logs=self.log_data
        )

    def fit(self):
        '''Обучение модели'''
        self.model_obj.fit(self.train_data, self.train_target)

    def to_bytes(self) -> ByteString:
        '''Сохранение модели в байтовую строку'''
        
        bytes_container = io.BytesIO()
        joblib.dump(self.model_obj, bytes_container)
        bytes_container.seek(0)

        return bytes_container.getvalue()
    
    def save_file(self, filename: Optional[str] = None, bytes_container: Optional[ByteString] = None):
        '''Сохранение модели в файл'''

        if filename is None:
            filename = join_file_path(DATA_PACKAGES_DIR, f'{self.model_name}_bytes')

        if bytes_container is None:
            bytes_container = self.to_bytes()

        with open(filename, 'wb') as file:
            file.write(bytes_container)
    
    


