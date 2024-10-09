

from domino.db import get_all_models_data, get_all_random_forest
from domino.config import DATA_PACKAGES_DIR
from domino.files_navigation import join_file_path

import json

all_models = get_all_models_data()

file_name = join_file_path(DATA_PACKAGES_DIR, 'ml_objects.json')
with open(file_name, 'w') as file:
    json.dump(all_models.encoded_data, file, ensure_ascii=False, indent=3)


random_forest_models = get_all_random_forest()

file_name = join_file_path(DATA_PACKAGES_DIR, 'random_forest_models.json')
with open(file_name, 'w') as file:
    json.dump(random_forest_models.encoded_data, file, ensure_ascii=False, indent=3)