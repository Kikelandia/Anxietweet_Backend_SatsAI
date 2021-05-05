class PublicConstants():
    def __init__(self):
        self.BOOL_TRUE = True
        self.BOOL_FALSE = False
        self.AT_SYMBOL = "@"
        self.HTTP_STRING = "http"
        self.HTTPS_STRING = "https"
        self.HTTP_WITH_DIAGS_AND_WILDCARD = "http:\/\/.*"
        self.HTTPS_WITH_DIAGS_AND_WILDCARD = "https:\/\/.*"
        self.TEXT_STRING = "Text"
        self.ID_STRING = "ID"
        self.DATE_STRING = "Date"
        self.USER_NAME_STRING = "User_name"
        self.USER_LOC_STRING = "User_location"
        self.USER_VERIF_STRING = "User_verified"
        self.EN_STRING = "en"
        self.ENGLISH_STRING = "english"
        self.EXTENDED_STRING = "extended"
        self.EMPTY_STRING = ""
        self.WHITESPACE = " "
        self.ZERO_AS_INTEGER = 0
        self.TEN_AS_INTEGER = 10
        self.SEARCH_CRITERIA_FOR_TWEETER = "lang:en -filter:retweets covid OR COVID OR coronavirus OR #coronavirus OR #covid19 OR covid19 OR #covid-19 OR cov2 OR #COVID OR #covid"
        self.CITIES_WITH_COORDINATES_AND_RADIUS = {
                        'New_York': "40.6643,-73.9385,10mi",
                        'San_Francisco' : "37.781157,-122.398720,10mi",
                        'Oklahoma': "35.4671,-97.5137,10mi",
                        'London': "51.5072,-0.1275,10mi",
                        'Vancouver': "49.3023,-123.107,10mi",
                        'Houston': "29.7805,-95.3863,10mi",
                        'Los_Angeles': "34.0194,-118.411,10mi",
                        'Sidney': "-33.86785,151.20732,10mi",
                        'Wellington': "-41.28664,174.77557,10mi",
                        'Dublin':"53.333060,-6.248890,10mi"
                    }