

from domino.db import get_all_models_data, get_all_thresholdes
from domino.config import DATA_PACKAGES_DIR
from domino.files_navigation import join_file_path

import json

all_models = get_all_models_data()

file_name = join_file_path(DATA_PACKAGES_DIR, 'ml_objects.json')
with open(file_name, 'w') as file:
    json.dump(all_models.model_dump(mode='json', exclude_none=True), file, ensure_ascii=False, indent=3)


thresholdes = get_all_thresholdes()
file_name = join_file_path(DATA_PACKAGES_DIR, 'thresholdes.json')
with open(file_name, 'w') as file:
    json.dump(thresholdes.model_dump(mode='json', exclude_none=True), file, ensure_ascii=False, indent=3)