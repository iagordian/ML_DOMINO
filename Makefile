


run:
	uvicorn domino.app:app --reload --port=5000

db_recreate_and_upload:
	python3 -m domino.upload.create_db

recreate_db:
	python3 -m domino.upload.create_tables

create_classificators:
	python3 -m domino.create_linear_classificators

create_decision_trees:
	python3 -m domino.create_decision_tree

models_to_json:
	python3 -m domino.save_models_to_json

samples_size_show:
	python3 -m domino.show_sample_size

save_sample_data:
	python3 -m domino.save_sample_data

activate_venv:
	source venv/bin/activate


install_libs:
	pip3 install -r requarements.txt