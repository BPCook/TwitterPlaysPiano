import re

def regexMatch(str, pattern):
	regex = re.compile(pattern)
	return regex.match(str)