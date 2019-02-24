""" Do twitter tasks """
from twitter_app import Twitter
from utils import load_config
from pprint import pprint
from settings import env

configfile = "./config/{env}.yaml".format(**{'env': env})

cfg = load_config(configfile)

twit = Twitter(cfg['twitter'])

print(twit._api.VerifyCredentials().status.text)
