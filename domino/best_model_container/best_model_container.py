
class BestModelContainer:

    def __init__(self):
        self.best_score = 0
        self.best_model_name = None

    def __setitem__(self, score: float, model_name: str):
        '''Принимает данные о новой модели и сохраняет их в случае, если они лучше предыдущих'''

        if score > self.best_score:
            self.best_score = score
            self.best_model_name = model_name



class BestThresholdContainer:

    def __init__(self):
        self.best_score = 0
        self.best_threshold = None

    def __setitem__(self, score: float, threshold: int):
        '''Принимает данные о новой модели и сохраняет их в случае, если они лучше предыдущих'''

        if score > self.best_score:
            self.best_score = score
            self.best_threshold = threshold