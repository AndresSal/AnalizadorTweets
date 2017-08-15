import couchdb
import sys
import textblob
import re
from couchdb import view
from textblob import TextBlob

URL = 'localhost'
db_name = 'tweetsuio'

'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos

try:
    print(db_name)
    db = server[db_name]
    print('success')

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()

def clean_tweet(text):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

view = "tweetsview_UIO/viewOnlyText"
myfile = open("tweetslimpios2.txt",'w')

for data in db.view(view):
    json_data = {}
    json_data = db.get(data['id'])
    text_es = TextBlob(data['value'])
    print(text_es)
    analisis = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", str(text_es)).split())
    myfile.write(analisis)
    myfile.write("\n")

myfile.close()