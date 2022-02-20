import os
from configparser import ConfigParser

__home_folder = os.environ.get('API_HOME')
assert os.path.isdir(__home_folder), f'Environment "API_HOME" should be a valid folder (got {__home_folder})'

__config_file = os.path.join(__home_folder, f'app.cfg')
assert os.path.isfile(__config_file), f'Config file doesn\'t exists ({__config_file})'

__configParser = ConfigParser()   
__configParser.read(__config_file)

title = __configParser.get('app', 'title')
version = __configParser.get('app', 'version')