
from abc import ABC

class BestObjectContainer(ABC):

    obj_name = None

    def __init__(self):
        self.best_score = 0
        setattr(self, self.obj_name, None)

    def __setitem__(self, score: float, obj: str):
        '''Принимает данные о новой модели и сохраняет их в случае, если они лучше предыдущих'''

        if score > self.best_score:
            self.best_score = score
            setattr(self, self.obj_name, obj)