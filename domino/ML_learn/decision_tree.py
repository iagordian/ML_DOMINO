
from .abstract_decision_tree import RandomForestLearning
from domino.config import RANDOM_SEED

class RandomForestClassifierCreator_6(RandomForestLearning):
    field_size = 6

    model_params = {
        'criterion': 'gini',
        'n_estimators': 128, 
        'max_depth': 32, 
        'min_samples_split': 2,
        'min_samples_leaf': 1,
        'max_features': 'sqrt',
        'random_state': RANDOM_SEED,
    }

class RandomForestClassifierCreator_7(RandomForestLearning):
    field_size = 7

    model_params = {
        'criterion': 'gini',
        'n_estimators': 32, 
        'max_depth': 16, 
        'min_samples_split': 4,
        'min_samples_leaf': 2,
        'max_features': 'log2',
        'random_state': RANDOM_SEED,
    }

class RandomForestClassifierCreator_8(RandomForestLearning):
    field_size = 8

    model_params = {
        'criterion': 'gini',
        'n_estimators': 128, 
        'max_depth': 32, 
        'min_samples_split': 4,
        'min_samples_leaf': 2,
        'max_features': 'log2',
        'random_state': RANDOM_SEED,
    }

class RandomForestClassifierCreator_9(RandomForestLearning):
    field_size = 9

    model_params = {
        'criterion': 'entropy',
        'n_estimators': 128, 
        'max_depth': 8, 
        'min_samples_split': 4,
        'min_samples_leaf': 1,
        'max_features': 'sqrt',
        'random_state': RANDOM_SEED,
    }

class RandomForestClassifierCreator_10(RandomForestLearning):
    field_size = 10

    model_params = {
        'criterion': 'gini',
        'n_estimators': 64, 
        'max_depth': 32, 
        'min_samples_split': 4,
        'min_samples_leaf': 1,
        'max_features': 'sqrt',
        'random_state': RANDOM_SEED,
    }

class RandomForestClassifierCreator_11(RandomForestLearning):
    field_size = 11

    model_params = {
        'criterion': 'gini',
        'n_estimators': 64, 
        'max_depth': 8, 
        'min_samples_split': 2,
        'min_samples_leaf': 1,
        'max_features': 'sqrt',
        'random_state': RANDOM_SEED,
    }

class RandomForestClassifierCreator_12(RandomForestLearning):
    field_size = 12

    model_params = {
        'criterion': 'gini',
        'n_estimators': 8, 
        'max_depth': 8, 
        'min_samples_split': 16,
        'min_samples_leaf': 1,
        'max_features': 'sqrt',
        'random_state': RANDOM_SEED,
    }

class RandomForestClassifierCreator_13(RandomForestLearning):
    field_size = 13

    model_params = {
        'criterion': 'gini',
        'n_estimators': 64, 
        'max_depth': 16, 
        'min_samples_split': 8,
        'min_samples_leaf': 4,
        'max_features': 'sqrt',
        'random_state': RANDOM_SEED,
    }


class RandomForestClassifierCreator_14(RandomForestLearning):
    field_size = 14

    model_params = {
        'criterion': 'gini',
        'n_estimators': 16, 
        'max_depth': 16, 
        'min_samples_split': 16,
        'min_samples_leaf': 1,
        'max_features': 'log2',
        'random_state': RANDOM_SEED,
    }

class RandomForestClassifierCreator_15(RandomForestLearning):
    field_size = 15

    model_params = {
        'criterion': 'gini',
        'n_estimators': 128, 
        'max_depth': 8, 
        'min_samples_split': 8,
        'min_samples_leaf': 1,
        'max_features': 'log2',
        'random_state': RANDOM_SEED,
    }

class RandomForestClassifierCreator_16(RandomForestLearning):
    field_size = 16

    model_params = {
        'criterion': 'gini',
        'n_estimators': 64, 
        'max_depth': 8, 
        'min_samples_split': 8,
        'min_samples_leaf': 1,
        'max_features': 'sqrt',
        'random_state': RANDOM_SEED,
    }

class RandomForestClassifierCreator_17(RandomForestLearning):
    field_size = 17

    model_params = {
        'criterion': 'gini',
        'n_estimators': 128, 
        'max_depth': 16, 
        'min_samples_split': 2,
        'min_samples_leaf': 1,
        'max_features': 'sqrt',
        'random_state': RANDOM_SEED,
    }

class RandomForestClassifierCreator_18(RandomForestLearning):
    field_size = 18

    model_params = {
        'criterion': 'entropy',
        'n_estimators': 8, 
        'max_depth': 16, 
        'min_samples_split': 4,
        'min_samples_leaf': 1,
        'max_features': 'log2',
        'random_state': RANDOM_SEED,
    }

random_forest_creators = {
    6: RandomForestClassifierCreator_6,
    7: RandomForestClassifierCreator_7,
    8: RandomForestClassifierCreator_8,
    9: RandomForestClassifierCreator_9,
    10: RandomForestClassifierCreator_10,
    11: RandomForestClassifierCreator_11,
    12: RandomForestClassifierCreator_12,
    13: RandomForestClassifierCreator_13,
    14: RandomForestClassifierCreator_14,
    15: RandomForestClassifierCreator_15,
    16: RandomForestClassifierCreator_16,
    17: RandomForestClassifierCreator_17,
    18: RandomForestClassifierCreator_18,
}