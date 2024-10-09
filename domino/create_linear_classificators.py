
from domino.domino_generate import get_random_array, get_six_ordered_domino_array
from domino.ML_learn import DominoLinearClassificatorCreator, DominoLogisticClassificatorCreator, \
    DominoSDGClassificatorCreator
from domino.config import RANDOM_SEED
from domino.db import model_to_db, set_best_model
from domino.best_model_container import BestModelContainer
from domino.order_check import get_learning_data_combine, mark_domino_to_classificate

best_model_container = BestModelContainer()

randoms = get_random_array(random_seed=RANDOM_SEED) 
ordered = get_six_ordered_domino_array(random_seed=RANDOM_SEED)

train_data, train_target = get_learning_data_combine(ordered.train_data.values, randoms.train_data.values, mark_domino_to_classificate)
test_data, test_target = get_learning_data_combine(ordered.test_data.values, randoms.test_data.values, mark_domino_to_classificate)


classificator_creator = DominoLinearClassificatorCreator(train_data, train_target, test_data, test_target)
classificator_creator.fit()
classificator_creator.log()
model_to_db(classificator_creator.data)
model_to_db(classificator_creator.scaler_data)
classificator_creator.add_score_data(best_model_container)

classificator_creator = DominoLogisticClassificatorCreator(train_data, train_target, test_data, test_target)
classificator_creator.fit()
classificator_creator.extract_auc()
classificator_creator.log()
model_to_db(classificator_creator.data)
classificator_creator.add_score_data(best_model_container)

classificator_creator = DominoSDGClassificatorCreator(train_data, train_target, test_data, test_target)
classificator_creator.fit()
classificator_creator.extract_auc()
classificator_creator.log()
model_to_db(classificator_creator.data)
classificator_creator.add_score_data(best_model_container)


set_best_model(best_model_container.best_model_name)

