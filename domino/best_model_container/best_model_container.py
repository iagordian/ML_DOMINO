

from .abstract import BestObjectContainer

class BestModelContainer(BestObjectContainer):
    obj_name = 'best_model_name'

class BestThresholdContainer(BestObjectContainer):
    obj_name = 'best_threshold'

class BestModelObjectContainer(BestObjectContainer):
    obj_name = 'best_model'
    attrs = [
        'criterion', 'n_estimators', 'max_depth',
        'min_samples_split', 'min_samples_leaf',
        'max_features'
    ]

    def __repr__(self):

        obj = getattr(self, self.obj_name)
        params_vals = [f'{attr_name}={getattr(obj, attr_name, None)}' for attr_name in self.attrs]

        return f'Параметры лучшей модели:\naccuarancy={self.best_score}' + '\n' + '\n'.join(params_vals)
