

from .abstratc import Model
from schemas import Domino

class DominoDecisionTree(Model):

    model_name = 'RandomForestClassifier'

    def predict(self, domino: Domino):
        up_order_data, down_order_data = domino.order_vars
        return int(self.model.predict(up_order_data)[0]), int(self.model.predict(down_order_data)[0])
    
    def ordered_check(self, domino: Domino):

        up, down = self.predict(domino)
        return all([
            up == domino.first[-1],
            down == domino.second[-1]
        ])