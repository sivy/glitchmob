import pathlib
import yaml

# BASE_DIR = pathlib.Path(__file__).parent
config_path = 'config.yaml'

def get_config(path):
    with open(path) as f:
        config = yaml.load(f)
    return config

config = get_config(config_path)
