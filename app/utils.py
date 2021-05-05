import re
import string
from nltk.corpus import stopwords
import pickle

from app.constants import PublicConstants

class Utilities():

    def __init__(self):
        self.constants = PublicConstants()
        self.bow_saved = pickle.load(open("app/pickle_Transformers/bow_AnxieTweet.pickle", "rb"))
        self.tfidf_saved = pickle.load(open("app/pickle_Transformers/tfidf_AnxieTweet.pickle", "rb"))
        self.svd_Pred_Mdl = pickle.load(open("app/pickle_Predictors/anxieTweet_Prediction_Model.pickle", "rb"))

    #With this function we will remove all the urls inside the tweet and also the labelings
    def removeUrlsAndLabeling(self,textAsString):
        strAslist = textAsString.split(self.constants.WHITESPACE)
        result = []
        for word in strAslist:
            if (word.startswith(self.constants.HTTP_STRING)
                or word.startswith(self.constants.HTTPS_STRING)
                or word.startswith(self.constants.AT_SYMBOL)):
                continue
            else:
                result += [word]
        result = ' '.join(result)
        #Some http and https instances might pass the previous filter so the string is split again
        #and finally the first element will be saved since the rest will be the ones with http or https
        result = re.split(self.constants.HTTP_WITH_DIAGS_AND_WILDCARD, str(result))[self.constants.ZERO_AS_INTEGER]
        result = re.split(self.constants.HTTPS_WITH_DIAGS_AND_WILDCARD, str(result))[self.constants.ZERO_AS_INTEGER]

        return(result)

    #removing special chars then removing stop words and finally returns the clean string
    def removePuncStopWords(self, textAsString):
        #To lower and then removing special chars
        nopunc = [char.lower() for char in textAsString if char not in string.punctuation + "“”"]
        nopunc = ''.join(nopunc)
        #Removing stop words, provided by nltk
        nopunc = [word + self.constants.WHITESPACE
                    for word in nopunc.split()
                        if word.lower() not in stopwords.words(self.constants.ENGLISH_STRING)]
        nopunc = ''.join(nopunc)
        return(nopunc)

    #String is converted to a Vector using the fitted "Bag Of Words" and then with the TFIDF transformation
    def transformToVector(self,textAsString):
        #Bag of Words transformation
        bow_Transformation = self.bow_saved.transform([textAsString])
        #TFIDF transformation
        tfidf_Transformation = self.tfidf_saved.transform(bow_Transformation)
        return(tfidf_Transformation)

    #Predicting the final class using the saved model from the training part
    def modelPrediction(self,sparseMatrix):
        #Model prediction
        prediction = self.svd_Pred_Mdl.predict(sparseMatrix)
        return(prediction[0])

    #Get the probability of the prediction using the saved model from the training part
    def modelPredictionWithProba(self,sparseMatrix):
        #Model probability prediction
        predictProba = self.svd_Pred_Mdl.predict_proba(sparseMatrix)
        return(predictProba[0])