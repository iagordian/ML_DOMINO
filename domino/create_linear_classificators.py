
from domino_generate import get_random_array, get_ordered_domino_array
from ML_learn import DominoLinearClassificatorCreator, DominoLogisticClassificatorCreator, \
    extract_ordered_marks, get_learning_data_combine, DominoSDGClassificatorCreator
from config import RANDOM_SEED
from db import model_to_db, set_best_model
from best_model_container import BestModelContainer

best_model_container = BestModelContainer()

randoms = get_random_array(random_seed=RANDOM_SEED) 
ordered = get_ordered_domino_array(random_seed=RANDOM_SEED)

ordered_train = extract_ordered_marks(ordered.train_data, is_callable=True)
ordered_test = extract_ordered_marks(ordered.test_data, is_callable=True)
random_train = extract_ordered_marks(randoms.train_data)
random_test = extract_ordered_marks(randoms.test_data)

test_data, test_target = get_learning_data_combine(ordered_test, random_test)
train_data, train_target = get_learning_data_combine(ordered_train, random_train)

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

