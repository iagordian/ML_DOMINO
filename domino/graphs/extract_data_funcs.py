

import pandas as pd
import numpy as np

from domino.order_check import complex_ensemble_funcs
from domino.db import get_ml_learned

def get_random_forest_importants_pd() -> pd.DataFrame:
    
    importances = get_random_forest_importants_data()
    rows = []
    for k, l in zip(complex_ensemble_funcs.labels_generator_simple, complex_ensemble_funcs.labels_generator):
        rows.append([l, importances[k]])

    importances = pd.DataFrame(
        rows,
        columns=['Признак', 'Важность признака']
    )

    return importances

def get_random_forest_importants_data() -> np.ndarray:

    model = get_ml_learned('FeatureImportances')
    return model.logs


def get_effectivity_pd():
    
    effectivity_data = get_effectivity_data()
    rows = []

    for size, effectivity in effectivity_data.items():
        rows.append([size, effectivity])

    effectivity = pd.DataFrame(
        rows,
        columns = [
            'Длина ряда',
            'Точность прогноза'
        ]
    )

    return effectivity

def get_effectivity_data():

    model = get_ml_learned('RandomForestAccuracy')

    size_data = {}
    for param_label, param in model.logs.items():
        if 'accuracy' in param_label:
            sample_size = int(param_label.split('_')[1])
            size_data[sample_size] = param

    return size_data
