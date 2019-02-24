# content of test_sample.py
import pytest
import twitter
from pprint import pprint

from utils import load_config
from twitter_app import Twitter

@pytest.fixture
def config():
    configfile = "./config/dev.yaml"
    return load_config(configfile)

@pytest.mark.skip
def test_invalid_credentials(config):
    with pytest.raises(twitter.error.TwitterError) as excinfo:
        config['twitter']['consumer']['key'] = ''

        twit = Twitter(config['twitter'])

        print(twit._api.VerifyCredentials())

        assert 'Could not authenticate you' in str(excinfo.value)

@pytest.mark.skip
def test_authentication(config):
    twit = Twitter(config['twitter'])

    assert twit._api.VerifyCredentials().id

@pytest.mark.skip
def test_tweet(config):
    twit = Twitter(config['twitter'])

    status = twit.tweet('I love python-twitter 2')

    assert 'I love python-twitter 2' == twit._api.GetStatus(status.id).text

def test_get_latest_status(config):
    twit = Twitter(config['twitter'])

    print twit.get_status()

    assert twit.get_status()

def test_get_status_with_id(config):
    twit = Twitter(config['twitter'])
    status_id = 1078947276859629569
    status =  twit.get_status(status_id)

    assert 'open position' in status
