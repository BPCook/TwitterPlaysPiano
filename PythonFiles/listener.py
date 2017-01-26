from tweepy import Stream
from tweepy import OAuthHandler 
from tweepy.streaming import StreamListener
import json
from user_record import UserRecord
from user_record import RecordLibrary
from maxdata import MaxData
from datetime import datetime
from time import sleep
import sys
import traceback

class Listener(StreamListener):
	
	def __init__(self, hashTag):
		self.hashTag = hashTag
		self.reconnectDelayTime = 60
		self.lastConnectStartTime = None
		self.firstReconnectAttempt = True
		self.recordLibrary = RecordLibrary()
	
	def connect(self, auth):
		self.auth = auth
		if self.lastConnectStartTime is not None:
			if self.firstReconnectAttempt:
				print "First reconnect attempt."
				self.lastConnectStartTime = datetime.now()
				self.firstReconnectAttempt = False
				self.internalConnect(auth)
			else:
				timeNow = datetime.now()
				timeDiff = timeNow - self.lastConnectStartTime
				if timeDiff.seconds < self.reconnectDelayTime:
					timeLeft = self.reconnectDelayTime
					while (timeLeft >= 0):
						minutes = timeLeft / 60
						seconds = timeLeft % 60
						if timeLeft > 0:
							sys.stdout.write("\rWaiting %d minutes and %d seconds before reattempt..." % (minutes, seconds))
						else:
							print "\rAttempting reconnect.                                           "
						timeLeft -= 1
						sleep(1)
					self.reconnectDelayTime *= 2
				self.lastConnectStartTime = datetime.now()
				self.internalConnect(auth)
		else:
			print "First connect attempt."
			self.lastConnectStartTime = datetime.now()
			self.internalConnect(auth)
	
	def internalConnect(self, auth):
		# Create stream for note data.
		twitterStream = Stream(auth, self)
		print "Connected."
		twitterStream.filter(track=[self.hashTag])
		# twitterStream.filter(follow=["364088274"], track=["#TwitterPlaysPiano"])
	
	def on_data(self, data):
		rawData = json.loads(data)
		
		# Make sure rawData is a json dictionary
		if not isinstance(rawData, dict):
			return
		
		if "text" not in rawData.keys():
			return
		
		# Build a Max data object from the Twitter text to send to Max. Then send it.
		try:
			record = self.recordLibrary.getRecord(rawData)
			maxData = MaxData(rawData, record)
			maxData.sendToMax()
		except Exception as e:
			print "ERROR!\n"
			print traceback.format_exc()
			pass
		
		return True
		
	def on_error(self, status):
		if status == 420:
			print "Good googly moogly! (A wild 420 appeared)\n"
			self.connect(self.auth)
		else:
			print "Error Code: ", status
