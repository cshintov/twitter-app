""" Loads the configuration from the yaml config file in config folder """

import yaml


def load_config(configfile):
    with open(configfile, 'r') as fh:
        cfg = yaml.load(fh)

    return cfg
