from twython import Twython
from klout import *
import sys
import time
import codecs

APP_KEY = 'tXf1XOnwXYgvQvg7NNolaA'
APP_SECRET = 'Xh6lDbUmAhyv2EuLSnxCeWBnHBKB1EsxRSYiYAMSA4'

#TWITTER LOGIN/SEARCH INFO

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)#uses twitter.py code to secure info
ACCESS_TOKEN = twitter.obtain_access_token() #uses twitter.py code to secure info

twitter1 = Twython(APP_KEY, access_token=ACCESS_TOKEN) # Twitter login/oauth information
counter = 30 #sets number of records to search
save = twitter1.search(q='@cacsdotorg', result_type='recent', count=counter)#uses login auth -> search

#KLOUT SEARCH INFO
k = Klout('jnmrzxs6ya7wmv8tcheqy3cm')  #Logs via Klout API

tweets = save['statuses']
f = codecs.open ('rawdata.csv', 'r+', 'utf-8') #below line corresponds to column titles of spreadsheet

exfilect = f.read()
#print exfilect

f.write("Twitter ID#"+','+"Twitter User ID"+','+"Klout Score" + ',' + "Fol. Ct" + ',' + "Location" ','  +"Tweet Creation Date"+','+"Tweet Text Contents \n")

progbarcounter=0

for tweet in tweets:
  
  progbarcounter+=1
  
  usernameactual = tweet['user']['screen_name']
  usrloc = tweet ['user']['location']
  
  progbarmult = (1/(float(len(tweets))))*100
  progbarmultint = int((1/(float(len(tweets))))*100) #gets inverse of tweets to use as multiplier
  sys.stdout.write('\r')  #PROGRESS BAR
  # the exact output you're looking for:
  sys.stdout.write("%-100s %d%%" % ('='*progbarcounter*progbarmultint, progbarcounter*progbarmult))
  sys.stdout.flush()
  
  time.sleep(1) #do this in order to avoid overloading servers and hitting limits with APIs
  
  while True:
    try:
      kloutId = k.identity.klout(screenName=str(usernameactual), timeout=1).get('id') #Gets ID of screenname specified
      score = k.user.score(kloutId=kloutId, timeout=1).get('score') #by using ID, gets score
      break
    except:
      score = "No Value"
      break #returns http error for some reason, using breaks as a workaround for now
      
  writeline = (tweet['id_str']+','+usernameactual+','+str(score)+ ',' + str(tweet['user']['followers_count'])+ ',' + usrloc.replace(",","") + ',' +tweet['created_at']+','+tweet['text'].replace(",",""))
  f.write(writeline+'\n')
  #print tweet['id_str'], '*', usernameactual, '*', score, '*', tweet['user']['followers_count'], '*', usrloc, '*', tweet['created_at'], '*',  tweet['text'].replace(",","")  Print total test


print ("Done!").rjust(20)
f.write(exfilect)
f.close()
  #----
  #nameid = (str(tweet['entities']['user_mentions']).find("u'screen_name'"))+17   #finds location of screen_name
  #endofnameid =  str(tweet['entities']['user_mentions']).find(", u'name'")  #finds end-location of screen_name
  #namecontents = str(tweet['entities']['user_mentions']) #contents of user_mentions which includes user_name.  Had to convert to string and use [x:y] to find elements of string because 3d array search is not supported by Twython
  #usernameactual = namecontents[nameid:endofnameid].replace("'","")