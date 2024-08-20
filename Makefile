


run:
	poetry run python domino/app.py

recreate_db:
	poetry run python domino/upload.py

create_classificators:
	poetry run python domino/create_linear_classificators.py

create_decision_trees:
	poetry run python domino/create_decision_tree.py