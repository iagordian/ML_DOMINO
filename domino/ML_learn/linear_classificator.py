
from sklearn.linear_model import LinearRegression, LogisticRegression, SGDClassifier

from .abstract_classificator import ClassificatorLearning

class DominoLinearClassificatorCreator(ClassificatorLearning):

    '''
    Объект класса создает линейный классификатор для
    отличия упорядоченного массива от случайного
    '''

    model_obj_type = LinearRegression
    threshold = 0.5

    def predict(self, data) -> bool:
        '''Предсказание модели'''
        return self.model_obj.predict(data) > self.threshold


class DominoLogisticClassificatorCreator(ClassificatorLearning):

    '''
    Объект класса создает логистический классификатор для
    отличия упорядоченного массива от случайного
    '''

    model_obj_type = LogisticRegression
    model_params = {
        'C': 0.5, 
        'dual': False, 
        'l1_ratio': 0.1, 
        'penalty': 'l2'
    }
    
class DominoSDGClassificatorCreator(ClassificatorLearning):

    model_obj_type = SGDClassifier
    model_params = dict(
        loss='modified_huber', 
        penalty=None,
        n_jobs=1, 
    )


    

    

    

    