class Note:
	def __init__(self):
		self.note = ""
		self.accent = ""
		self.octave = "4"
	
	def setNote(self, note):
		self.note = note
	
	def setAccent(self, accent):
		self.accent = accent
	
	def setOctave(self, octave):
		self.octave = octave
	
	def getValue(self):
		noteValueKey = {'c': 0, 'd': 2, 'e': 4, 'f': 5, 'g': 7, 'a': 9, 'b': 11}
		
		# Get base note
		noteValue = noteValueKey[self.note.lower()[0]]
		
		# Add accent value
		noteValue += 1 if self.accent == '#' else 0
		noteValue += -1 if self.accent == 'b' else 0
		
		# Shift by octave value
		noteValue += 12 * int(self.octave)
		
		# Shift by 12 for standard MIDI values
		noteValue += 12
		
		return noteValue