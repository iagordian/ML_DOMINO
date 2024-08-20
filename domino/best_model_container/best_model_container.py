
class BestModelContainer:

    def __init__(self):
        self.best_score = 0
        self.best_model_name = None

    def __setitem__(self, score: float, model_name: str):
        '''Принимает данные о новой модели и сохраняет их в случае, если они лучше предыдущих'''

        if self.best_score is not None:
            if score > self.best_score:
                self.best_score = score
                self.best_model_name = model_name
            return
        self.best_model_name = model_name