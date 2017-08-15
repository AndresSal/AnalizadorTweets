
import couchdb
import sys
import textblob

from couchdb import view
from textblob import TextBlob

URL = 'localhost'
db_name = 'tweetsuio'
db_name2 = 'cleanedtweets'

'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
server2 = couchdb.Server('http://'+URL+':5984/')
try:
    print(db_name)
    db = server[db_name]
    db2 = server2[db_name2]
    print('success')

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()


view = "tweetsview_UIO/viewOnlyText"
LIMIT_OF_DOCUMENTS = 1000

for data in db.view(view, limit=LIMIT_OF_DOCUMENTS):
    json_data = {}
    json_data = db.get(data['id'])
    text_es = TextBlob(data['value'])
    text_en = text_es.translate(to="en")
    polarity_value = text_es.sentiment.polarity * 100.0
    polarity = ""
    if polarity_value == 0:
        polarity = 'neutral'
    elif polarity_value < 0:
        polarity = 'negative'
    else:
        polarity = 'positive'
    subjectivity = text_es.sentiment.subjectivity
    json_data['label'] = {'polarity': polarity, 'polarity_value': polarity_value, 'subjectivity': subjectivity}
    db.save(json_data)
    print(text_es)






