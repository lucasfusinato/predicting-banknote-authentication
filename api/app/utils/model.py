import os
import re
import joblib

__home_folder = os.environ.get('API_HOME')
assert os.path.isdir(__home_folder), f'Environment "API_HOME" should be a valid folder (got {__home_folder})'

__model_folder = os.path.join(__home_folder, 'model')
assert os.path.isdir(__model_folder), f'Model folder doesn\'t exists (got {__model_folder})'

__model_version = os.environ.get('MODEL_VERSION')
assert re.match('^([0-9]+)\.([0-9]+)\.([0-9]+)?$', __model_version), f'Environment "__model_version" should match Semantic Version pattern (got {__model_version})'

__model_file = os.path.join(__model_folder, f'classifier-{__model_version}.pkl')
assert os.path.isfile(__model_file), f'Model file doesn\'t exists ({__model_file})'

def get_classifier_model():
    return joblib.load(__model_file)