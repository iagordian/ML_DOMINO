


run:
	poetry run uvicorn domino.app:app --reload --port=5000

recreate_db:
	poetry run python3 -m domino.upload.create_db

create_classificators:
	poetry run python3 -m domino.create_linear_classificators

create_decision_trees:
	poetry run python3 -m domino.create_decision_tree

models_to_json:
	poetry run python3 -m domino.save_models_to_json

samples_size_show:
	poetry run python3 -m domino.show_sample_size

save_sample_data:
	poetry run python3 -m domino.save_sample_data