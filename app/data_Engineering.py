import pandas as pd
import random

from app.utils import Utilities

class ProcessTweets():

    def __init__(self):
        self.tools = Utilities()

    #Calling methods to clean text
    def cleanTweet(self,tweet):
        tweet_to_clean = tweet
        tweetNoURL = self.tools.removeUrlsAndLabeling(tweet_to_clean)
        tweetNoPuncNoStopWords = self.tools.removePuncStopWords(tweetNoURL)
        return(tweetNoPuncNoStopWords)

    #Calling method to transfrom the text
    def VectorizeTweet(self,tweet):
        tweet_to_vector = tweet
        tweetToVectorize = self.tools.transformToVector(tweet_to_vector)
        return(tweetToVectorize)

    #Calling method to predict class
    def predictResult(self,tweet):
        tweet_to_predict = tweet
        prediction = self.tools.modelPrediction(tweet_to_predict)
        return(prediction)

    #Calling method to predict prediction accuracy
    def predictWithProba(self,tweet):
        tweet_to_predict = tweet
        predictionProba = self.tools.modelPredictionWithProba(tweet_to_predict)
        return(predictionProba)