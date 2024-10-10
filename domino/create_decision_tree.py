
from domino.config import RANDOM_SEED
from domino.ML_learn import random_forest_creators
from domino.db import model_to_db, random_forest_to_db
from domino.schemas import ML_Object
from domino.domino_generate import all_samples_generators
from domino.order_check import complex_ensemble_funcs

import numpy as np
from progress.bar import IncrementalBar

accuracy_data_label = 'RandomForestAccuracy'
complex_model_logs = {
    'model_name': accuracy_data_label
}

params_data_label = 'RandomForestParams'
params_data_logs = {
    'model_name': params_data_label
}

feature_importances = []

progress_bar = IncrementalBar('Throughing', max = 12)
for i in range(6, 19):

    sample_generator = all_samples_generators[i]
    random_forest_creator = random_forest_creators[i]

    data = sample_generator(random_seed=RANDOM_SEED)
    train_data = data.train_data
    test_data = data.test_data

    random_forest_creator = random_forest_creator(train_data, test_data)
    random_forest_creator.extract_order_vars()
    random_forest_creator.fit()
    random_forest_creator.to_log()
    random_forest_to_db(random_forest_creator.data)

    complex_model_logs[f'accuracy_{i}'] = random_forest_creator.log_data['accuracy']
    params_data_logs[f'field_size_{i}'] = random_forest_creator.model_params
    feature_importances.append(random_forest_creator.feature_importances)

    progress_bar.next()

progress_bar.finish()

accuracy_log_data = ML_Object(
    model_name = accuracy_data_label,
    logs = complex_model_logs
)
model_to_db(accuracy_log_data)

params_log_data = ML_Object(
    model_name = params_data_label,
    logs = params_data_logs
)
model_to_db(params_log_data)

feature_importances = np.mean(np.concatenate(feature_importances).reshape(len(all_samples_generators), complex_ensemble_funcs.processed_data_arr_length), axis=0)

feature_importances_label = 'FeatureImportances'
feature_importances_data = {'model_name': feature_importances_label}

for label, imp in zip(complex_ensemble_funcs.labels_generator_simple, feature_importances):
    feature_importances_data[label] = imp

feature_importances_log_data = ML_Object(
    model_name = feature_importances_label,
    logs = feature_importances_data
)
model_to_db(feature_importances_log_data)
