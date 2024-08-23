

from domino.domino_generate import all_samples
from domino.schemas import ML_Object
from domino.db import model_to_db

model_name = 'SampleGenerator'
name = {'model_name': model_name}
samples_data = {f'sample_size_of_length_{size}': len(arr) for size, arr in all_samples.items()}

model = ML_Object(
    model_name=model_name,
    logs={**name, **samples_data}
)

model_to_db(model)