

from domino.domino_generate import all_samples
from domino.schemas import ML_Object
from domino.db import model_to_db

model_name = 'SampleGenerator'
name = {'model_name': model_name}
samples_data = {f'sample_size_of_length_{size}': gen().data.shape[0] for size, gen in all_samples.items()}

model = ML_Object(
    model_name=model_name,
    logs={**name, **samples_data}
)

model_to_db(model)