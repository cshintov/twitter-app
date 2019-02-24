""" Twitter related stuff """
import twitter

class Twitter:
    def __init__(self, cfg):
        self._type = 'twitter'
        self._api = twitter.Api(
                        consumer_key=cfg['consumer']['key'],
                        consumer_secret=cfg['consumer']['secret'],
                        access_token_key=cfg['access_token']['key'],
                        access_token_secret=cfg['access_token']['secret']
                    )

    def tweet(self, status):
        """ Tweets your deep thought to the world """
        return self._api.PostUpdate(status)

    def get_status(self, status_id=''):
        if status_id:
            return self._api.GetStatus(status_id).text

        return self._api.VerifyCredentials().status.text


