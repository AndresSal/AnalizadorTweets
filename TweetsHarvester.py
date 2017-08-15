import couchdb
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

ckey = "y5xTsnS6pZLGxwguTfZUFBIGL"
csecret = "zGF0FwiaVosMTEcv1Wpy2nLEF5VpqV8O0QKpDNONE8I1G3yXpC"
atoken = "885227847106924544-SQ5aWBwpZLMSOcafAv9JcQl7AbIgeqC"
asecret = "JpGeQnNDEFB2lSiN135GcxM7MiQsPqosRzlXdzHf3HfwT"


class listener(StreamListener):
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print("SAVED" + str(doc) + "=>" + str(data))
        except:
            print("Already exists")
            pass
        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

URL = 'localhost'
db_name = 'tweetsuio'

'''========couchdb'=========='''
server = couchdb.Server('http://' + URL + ':5984/')  # () poner la url de su base de datos
try:
    print(db_name)
    db = server[db_name]

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()

'''===============LOCATIONS=============='''

twitterStream.filter(locations=[-78.593445, -0.370099, -78.386078, -0.081711])  # QUITO

