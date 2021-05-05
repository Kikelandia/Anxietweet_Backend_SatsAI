import pandas as pd
import random
from datetime import datetime, timedelta
import tweepy as tw
from tqdm import tqdm

from app.tweeter_Login import AccessTweeterAPI
from app.constants import PublicConstants

pd.set_option('display.max_colwidth', None)

class GetTweets():

    def __init__(self):
        self.constants = PublicConstants()
        self.tweeterAPIAccessInfo = AccessTweeterAPI()

    #Get and return one single tweet from the dataframe used for the training part
    def getOneTweetFromLocalDB(self):
        #Reading the PD Dataframe
        tweets_df = pd.read_csv("app/tweets_data.csv")
        #Random number between 0 and DF length
        position = random.randint(self.constants.ZERO_AS_INTEGER,len(tweets_df))
        #Random tweet from the local DF
        TweetFromDB = tweets_df[self.constants.TEXT_STRING][position]
        return(TweetFromDB)

    def getOneTweetFromTweeterAPI(self):
        #Get encrypted user name and password to access tweeter
        encriptedinfo = self.tweeterAPIAccessInfo.encriptedUserIDandPassword()

        #This "api" object works to acces securely within the Tweeter API
        api = tw.API(encriptedinfo, wait_on_rate_limit = self.constants.BOOL_TRUE)

        #Cities used to get tweets from
        cities = self.constants.CITIES_WITH_COORDINATES_AND_RADIUS
        #Getting a random City from the list
        randomCity = random.choice(list(cities.keys()))
        #Search criteria for Tweeter API
        search_words = (self.constants.SEARCH_CRITERIA_FOR_TWEETER)
        #Today less 10 days
        tenDaysAgo = datetime.today() - timedelta(days = self.constants.TEN_AS_INTEGER)
        #10 Days ago as STR in format YYYY-MM-DD
        date_since = str(tenDaysAgo)[:self.constants.TEN_AS_INTEGER]
        #Random city with coordinates and radius
        place = cities[randomCity]
        #Total amount of tweets to retrieve
        total_items = self.constants.TEN_AS_INTEGER

        #Performing the actual search, inside tweeter with all the previous parameters
        tweets = tw.Cursor(api.search,
                              q = search_words,
                              geocode = place,
                              lang = self.constants.EN_STRING,
                              tweet_mode = self.constants.EXTENDED_STRING,
                              since = date_since).items(total_items)

        #Creating the DF with 10 tweets and the relevant information
        tweets_df = pd.DataFrame()
        for tweet in tqdm(tweets):
            tweets_df = tweets_df.append(pd.DataFrame({self.constants.USER_NAME_STRING: tweet.user.name,
                                                           self.constants.USER_LOC_STRING: tweet.user.location,
                                                           self.constants.USER_VERIF_STRING: tweet.user.verified,
                                                           self.constants.DATE_STRING: tweet.created_at,
                                                           self.constants.TEXT_STRING: tweet.full_text,
                                                           self.constants.ID_STRING: tweet.id},
                                                    index=[self.constants.ZERO_AS_INTEGER]))
        #getting a random tweet to minimize the possibility to work with a repeated item
        sampleTweet = tweets_df.sample()
        #Getting the actual string from the tweet
        TweetFromTwitter = sampleTweet.Text.item()
        #Getting the tweet id so we can verify the tweet
        tweetID = sampleTweet.ID.item()

        return(TweetFromTwitter, tweetID)