#!/usr/bin/env python
from flask import Flask, request, jsonify
from flask_cors import CORS

from app.data_Engineering import ProcessTweets
from app.retrieve_Tweets import GetTweets
from app.constants import PublicConstants

app = Flask(__name__)
CORS(app)

@app.route("/")
def home_view():
    return ("<h1>Welcome to AnxieTweet Backend</h1>")

#Route to retrieve one tweet form the Local Pandas DF then preprocess the text, tranfrom it to a vector
#get the prediction of the class and the prediction accuracy
@app.route('/getDBTweet', methods=['POST'])
def processAndPredictTweetsFromDB():
    #Instance of the class that retrieve tweets from local DF or tweeter API
    getInformation = GetTweets()
    #Instance of the class that preprocess/transforms the tweet into a vector
    processing = ProcessTweets()
    #Getting one tweet from local DF used during the training part
    tweetFromDB = getInformation.getOneTweetFromLocalDB()
    #Cleaning the tweet
    preprocessedTweetFromDB = processing.cleanTweet(tweetFromDB)
    #Transforming the tweet into a vector
    vectorizedTweetFromDB = processing.VectorizeTweet(preprocessedTweetFromDB)
    #Prediction using the vector
    finalPrediction = processing.predictResult(vectorizedTweetFromDB)
    #Prediction accuracy using the vector
    predAccuracy = processing.predictWithProba(vectorizedTweetFromDB)

    return jsonify({
        'tweetFromDB' : str(tweetFromDB),
        'preprocessedTweetFromDB' : preprocessedTweetFromDB,
        'vectorizedTweetFromDB' : str(vectorizedTweetFromDB),
        'finalPrediction' : str(finalPrediction),
        'predAccuracy' : str(predAccuracy)
        })


#Route to retrieve one tweet form the Tweeter API then preprocess the text, tranfrom it to a vector
#get the prediction of the class and the prediction accuracy
@app.route('/getRealTweet', methods=['POST'])
def processAndPredictRealTimeTweets():
    #Instance of the class that retrieve tweets from local DF or tweeter API
    getInformation = GetTweets()
    #Instance of the class that preprocess/transforms the tweet into a vector
    processing = ProcessTweets()
    #Getting one tweet from tweeter API as well the tweet's ID
    originalTweetFromTwitter, tweetID = getInformation.getOneTweetFromTweeterAPI()
    #Cleaning the tweet
    preprocessedRealTimeTweet = processing.cleanTweet(originalTweetFromTwitter)
    #Transforming the tweet into a vector
    realTimeVectorizedTweet = processing.VectorizeTweet(preprocessedRealTimeTweet)
    #Prediction using the vector
    finalPrediction = processing.predictResult(realTimeVectorizedTweet)
    #Prediction accuracy using the vector
    predAccuracy = processing.predictWithProba(realTimeVectorizedTweet)

    return jsonify({
        'recentTweet' : originalTweetFromTwitter,
        'tweetID' : str(tweetID),
        'recentTweetProcessed' : preprocessedRealTimeTweet,
        'recentTweetasNumbers' : str(realTimeVectorizedTweet),
        'finalPrediction' : str(finalPrediction),
        'predAccuracy' : str(predAccuracy)
        })


#Route to process the suctom text entered in the fron end then preprocess the text, tranfrom it to a vector
#get the prediction of the class and the prediction accuracy
@app.route('/processUserText', methods=['POST'])
def processTransformPredictUserText():
    #Instance of the class that preprocess/transforms the tweet into a vector
    processing = ProcessTweets()
    usersOriginalText = ""
    if request.method == 'POST':
        usersOriginalText = (request.json['message'])
    #Cleaning the user's text
    preprocessedUserText = processing.cleanTweet(usersOriginalText)
    #Transforming the user's text into a vector
    vectorizedUserText = processing.VectorizeTweet(preprocessedUserText)
    #Prediction using the vector
    userTextPrediction = processing.predictResult(vectorizedUserText)
    #Prediction accuracy using the vector
    predAccuracy = processing.predictWithProba(vectorizedUserText)

    return jsonify({
        'userTextProcessed' : preprocessedUserText,
        'userTextasNumbers' : str(vectorizedUserText),
        'finalPrediction' : str(userTextPrediction),
        'predAccuracy' : str(predAccuracy)
        })

#if __name__=='__main__':
#    app.run(host="0.0.0.0", port="5001", debug=True)