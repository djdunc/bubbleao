# working from standard yocto build on Edison
# make sure pip is upto date on edison
# sudo pip install --upgrade pip

# download and setup tweepy in root
# pip install tweepy
# (note tweepy at https://github.com/tweepy/tweepy)

# D Wilson June 2016 (original work 2014)



from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from settings import *
import mraa
import time
import json
import sys
 
relay = mraa.Gpio(3)
relay.dir(mraa.DIR_OUT)

led = mraa.Gpio(13)    
led.dir(mraa.DIR_OUT)

class StdOutListener(StreamListener):
	""" A listener handles tweets are the received from the stream.
	This is a basic listener that just prints received tweets to stdout.

	"""
	def on_data(self, data):
		try:
#            print data

			led.write(1)
			relay.write(1)
			time.sleep(10)
			led.write(0)
			relay.write(0)

			jsonData = json.loads(data)
			createdAt = jsonData['created_at']
			text = jsonData['text']
			followers_count = jsonData['user']['followers_count']
			name = jsonData['user']['name']
			screen_name = jsonData['user']['screen_name']

			saveThis = createdAt + " :: " + str(followers_count) + " :: " + name  + " :: " + screen_name  + " :: " + text

			print name
			saveFile = open('twitDB2icricities.json','a')
#            saveFile.write(data)
			saveFile.write(saveThis)

			saveFile.write('\n')
			saveFile.close()
			return True
		except BaseException, e:
			#print 'failed ondata, ',str(e)
			time.sleep(5)

	def on_error(self, status):
		print status

if __name__ == '__main__':
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	with open('hashtags.txt', 'r') as f:
		hashtags = f.read()
	
	stream = Stream(auth, l)
	stream.filter(track=[hashtags])


