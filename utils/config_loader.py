import yaml


def load_config(config_path: str = "/Users/venkatasivapraveenpallaprolu/first_document/config/config.yaml") -> dict:
    with open(config_path, "r") as file:
        config=yaml.safe_load(file)
    return config

load_config("/Users/venkatasivapraveenpallaprolu/first_document/config/config.yaml")