from datetime import datetime

class UserRecord:
	def __init__(self, rawData):
		self.userId = rawData["user"]["id"]
		self.lastTimeSeen = datetime.now()
		self.octave = "4"
		self.dynamic = "mf"
		self.duration = 1.0
		self.timbre = 1

class RecordLibrary:
	def __init__(self):
		self.records = {}
		self.timeOutLength = 60 * 15
	
	def setTimeoutLength(self, timeOutLength):
		self.timeOutLength = timeOutLength
	
	def getRecord(self, rawData):
		userId = rawData["user"]["id"]
		
		# If the user ID has a record...
		if userId in self.records.keys():
			# See how long it's been since the last time it was seen.
			dateDiff = datetime.now() - self.records[userId].lastTimeSeen
			
			# If it timed out, kill the record.
			if dateDiff.seconds > self.timeOutLength:
				self.records.pop(userId, None)
		
		# Now, if the record is still there, return it. Else make a new one and return that.
		if userId in self.records.keys():
			self.records[userId].lastTimeSeen = datetime.now()
			return self.records[userId]
		else:
			self.records[userId] = UserRecord(rawData)
			return self.records[userId]
		