import tweepy as tw

class AccessTweeterAPI():
    def __init__(self):
        self.consumer_api_key = "Twitter Developer Account User Name"
        self.consumer_api_secret = "Twitter Developer Account Password"


    def encriptedUserIDandPassword(self):
        auth = tw.OAuthHandler(self.consumer_api_key, self.consumer_api_secret)
        return(auth)