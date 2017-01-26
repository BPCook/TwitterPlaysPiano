from note import Note
from utility import regexMatch

class MaxData:
	
	def __init__(self, rawData, userRecord):
		# Default values set here.
		self.record = userRecord
		self.note = Note()
		self.note.octave = self.record.octave
		self.tweetText = rawData["text"]
		self.screenName = rawData["user"]["screen_name"]
	
	# Returns a dictionary of the 'volume' values for dynamics.
	def getDynamicValues(self):
		result = {}
		
		# Specify the options for dynamics here, and the range to generate values over
		dynamicOptions = ['pppp', 'ppp', 'pp', 'p', 'mp', 'mf', 'f', 'ff', 'fff', 'ffff']
		dynamicRange = 128	# Generates values from 0 to dynamicRange - 1
		
		i = len(dynamicOptions) - 1
		for option in dynamicOptions:
			result[option] = dynamicRange - (i * (dynamicRange / len(dynamicOptions)))
			i -= 1
		
		return result
	
	def sendToMax(self):
		self.parseRawText()
		dynamicValues = self.getDynamicValues()
		print "User %s" % (self.screenName)
		print "%s %d %d %.2f" % (self.record.timbre, self.note.getValue(), dynamicValues[self.record.dynamic], int(self.record.duration * 1000.0))
	
	def parseRawText(self):
		textParts = self.tweetText.split(" ")
		
		noteFound = False
		for textPart in textParts:
			# Check if text part is a note. Must get a note before anything else is counted (dynamics, duration, etc).
			if (not noteFound):
				if regexMatch(textPart, "^[a-gA-G]$"):
					# process single note
					self.note.setNote(textPart[0])
					noteFound = True
				elif regexMatch(textPart, "^[a-gA-G](#|b)$"):
					# process note + accent
					self.note.setNote(textPart[0])
					self.note.setAccent(textPart[1])
					noteFound = True
				elif regexMatch(textPart, "^[a-gA-G][0-8]$"):
					# process note + octave
					self.note.setNote(textPart[0])
					self.note.setOctave(textPart[1])
					self.record.octave = textPart[1]
					noteFound = True
				elif regexMatch(textPart, "^[a-gA-G](#|b)[0-8]$"):
					# process note + accent + octave
					self.note.setNote(textPart[0])
					self.note.setAccent(textPart[1])
					self.note.setOctave(textPart[2])
					self.record.octave = textPart[2]
					noteFound = True
			else:
				# Check if text part is a dynamic.
				if regexMatch(textPart.lower(), "^(f{1,4})$|^(p{1,4})$|^mf$|^mp$"):
					self.record.dynamic = textPart.lower()
					continue
				
				# Check if text part is a duration.
				if regexMatch(textPart, "^([1-9][0-9]*)|(([0-9]*[.][0-9]+)?)$"):
					self.record.duration = float(textPart)
					continue
				
				# Check if text part is a timbre.
				if regexMatch(textPart.lower(), "^t(([1-9])|(1[0-6]))$"):
					self.record.timbre = int(textPart[1:len(textPart)].lower())
					continue
		
		if not noteFound:
			raise Exception("No note data was found in tweet text.")