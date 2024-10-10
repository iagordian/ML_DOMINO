
from domino.best_model_container import BestModelObjectContainer
from domino.order_check import process_order_vars_full, simmetric_marc
from domino.domino_generate import all_samples_generators
from domino.config import RANDOM_SEED

from domino.order_check import ProcessFunc, ProcessFuncsList
from domino.order_check import ordered_balance
from domino.order_check import balanced_mark
from domino.entrope import get_secondary_growth_entrope, get_entrope

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from progress.bar import IncrementalBar
import numpy as np

# print(simmetric_marc(np.array([1, 1, 1, 1, 1, 1])))

gen_num = 18
sample_generator = all_samples_generators[gen_num]

complex_ensemble_funcs = ProcessFuncsList(
  ProcessFunc(get_secondary_growth_entrope, 'Изменение энтропии'),
  ProcessFunc(get_entrope, 'Энтропия', procces_volume_param='both'), 
  ProcessFunc(ordered_balance, 'Энтропия характеристик упорядоченности'), 
  ProcessFunc(balanced_mark, 'Сбалансированность', procces_volume_param='both'), 
  ProcessFunc(simmetric_marc, 'Оценка симметричности'),
)

sample = sample_generator(random_seed=RANDOM_SEED)

train_data_base = sample.train_data
test_data_base = sample.test_data

train_target = train_data_base[5]
test_target = test_data_base[5]

train_data = process_order_vars_full(train_data_base, complex_ensemble_funcs)
test_data = process_order_vars_full(test_data_base, complex_ensemble_funcs)

best_model_container = BestModelObjectContainer()

n_estimators = [2 ** i for i in range(3, 8)]
max_depth = [2 ** i for i in range(3, 8)]
min_samples_split = [2 ** i for i in range(4, 0, -1)]
min_samples_leafs = [2 ** i for i in range(3)]
max_features = ['sqrt', 'log2']
criteries = ['gini', 'entropy', 'log_loss']

length = 5 * 5 * 4 * 3 * 3 * 2
progress_bar = IncrementalBar('Throughing', max = length)

for e in n_estimators:
    for d in max_depth:
        for min_spl in min_samples_split:
            for min_lfs in min_samples_leafs:
                for f in max_features:
                    for c in criteries:

                        model = RandomForestClassifier(
                            n_estimators=e,
                            max_depth=d,
                            max_features=f,
                            min_samples_leaf=min_lfs,
                            min_samples_split=min_spl,
                            criterion=c,
                            random_state=RANDOM_SEED
                        )
                        model.fit(train_data, train_target)

                        predicted = model.predict(test_data)
                        accuracy = accuracy_score(predicted, test_target)

                        best_model_container[accuracy] = model

                        progress_bar.next()

progress_bar.finish()
print(best_model_container, end='\n\n')
print(train_data_base.shape[1])

if train_data_base.shape[1] == 6:
    print(
        best_model_container.best_model.predict(process_order_vars_full(np.array([[1, 2, 3, 4, 5, 6]]), complex_ensemble_funcs)) == 6,
        best_model_container.best_model.predict(process_order_vars_full(np.array([[6, 5, 4, 3, 2, 1]]), complex_ensemble_funcs)) == 1,
        best_model_container.best_model.predict(process_order_vars_full(np.array([[0, 1, 2, 3, 4, 5]]), complex_ensemble_funcs)) == 5,
        best_model_container.best_model.predict(process_order_vars_full(np.array([[5, 4, 3, 2, 1, 0]]), complex_ensemble_funcs)) == 0,
        sep='\n'
    )