from tweepy import Stream
from tweepy import OAuthHandler 
from tweepy.streaming import StreamListener
from listener import Listener

if __name__ == "__main__":
	apiKey = "QY8f8scdZYb0sPnFMq6G48FMh"
	apiSecret = "Sxin83rprEg5YUMiThQQ47LZKJRmvLiRLJXJKskB8uno5z62EI"
	accessToken = "364088274-UvVg9icnCYo0LT8q9mXdKdtGAhOh5WQMgM0Jd7MY"
	accessSecret = "woi5HaLwnzfMfWQsAp6O15hECxBzIRzknEyiF2cFx83f8"
	
	# Set Twitter authorization.
	auth = OAuthHandler(apiKey, apiSecret)
	auth.set_access_token(accessToken, accessSecret)
	
	streamListener = Listener("#tpp")
	streamListener.connect(auth)
	print ": )"
