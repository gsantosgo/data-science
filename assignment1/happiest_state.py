import sys, re, json 

# ==============================================================================================
# Introduction to Data Science 
# 
# Guillermo Santos (@gsantosgo) 
#
# Subject: Which State is happiest?
# Description: 
#	Write a Python script, happiest_state.py, that returns the name of the happiest state as a string.
# 
#	happiest_state.py should take a file of tweets as an input and be usable in the following way:
#
#		$ python happiest_state.py <sentiment_file> <tweet_file>
#
# 	The file AFINN-111.txt contains a list of pre-computed sentiment score.
#
#  	Assume the tweet file contains data formatted the same way as the livestream data.
#
# 
#	We recommend that you build on your solution to Problem 2.
#	There are three different objects within the tweet that you can use to determine it’s origin.
#	1 The coordinates object
#   2 The place object
#	3 The user object
#
#	You are free to develop your own strategy for determining the state that each tweet originates from.
#
# 	Limit the tweets you analyze to those in the United States.
#
# 	The live stream has a slightly different format from the response to the query you used in Problem 0. 
#   In this file, each line is a Tweet object, as described in the twitter documentation.
#	
#	Note: Not every tweet dictionary will have a text key -- real data is dirty. Be prepared to debug, and 
#		  feel free to throw out tweets that your code can't handle to get something working.  
#		  For example, non-English tweets.
#
#		  Your script should print the two letter state abbreviation to stdout.
#
#		  Your script will not have access to the Internet, so you cannot rely on third party services to resolve geocoded locations.
# 
# ---------------------------------------------------------------------------------------------

def lines_scores(filename):	
	sentiment_file = open(filename)
	scores = {} # initialize an empty dictionary
	for line in sentiment_file:
		term, score = line.split('\t', 1) # The file is tab-delimited. "\t" means "tab character"
	        scores[term] = int(score) # Convert the score to an integer.
	sentiment_file.close()
	return scores
	
def lines_tweets_json(filename):
	tweets_file = open(filename)
	tweets = []
	for line in tweets_file:
		tweet_dict = json.loads(line)
		
if all(k in tweets[index].keys() for k in ("text","place")):
            if not (tweets[index]["place"] == None):
                #if not (type(tweets[index]["place"]["state_code"]) == "NoneType"):
                    tweet_word = tweets[index]["text"].split()
                    tweet_state = tweets[index]["place"]["country_code"]
					
					
		if 'text' in tweet_dict.keys() and 'user' in tweet_dict.keys():
			text = tweet_dict["text"].encode('utf-8')
			tweets.append(text)
	tweets_file.close()
	return tweets

def processTweet(text, phrases=True):
	tokens = re.split(" ", text.lower())
	if phrases:
		pairs = []		
		lastAnt = None		
        last = None		
        for tok in tokens:			
			if lastAnt != None and last != None:
				pairs.append("%s %s %s" % (lastAnt, last, tok))
			if last != None:
				pairs.append("%s %s" % (last, tok))								
			lastAnt = last 
			last = tok
        tokens.extend(pairs)
	if '' in tokens:
		tokens.remove('')
	return tokens

def scores_sentiment_tweets (scores_dict, tweets): 	
	# Processing tweet 	
    for tweet in tweets: 		
		score = 0.0
		tweet_word_phrases = processTweet(tweet)
		for word_phrase in tweet_word_phrases: 
			if word_phrase in scores_dict: 
				score = score + scores_dict[word_phrase] 
				
		if score >= 0: 
			print "positive:" + str(score) + ""
		if score < 0: 		
			print "negative:" + str(score) + ""
	
def main():
	# Sentiment Dictionary 
	scores_dict =  lines_scores(sys.argv[1]) 	
	# Tweets 
	tweets = lines_tweets_json(sys.argv[2]) 
	
	#tweets = ["RT @gsantosgo Why Linux is faster than Windows http://blog.zorinaq.com/?e=74  written by a Windows kernel developer","Does not work doubt can't stand", "Worth celebrated celebrates"]
	# Calculate Sentiment Scores 
	scores_sentiment_tweets(scores_dict, tweets)
	
if __name__ == '__main__':
	try:
		main()
	except Exception, e:
		print "Error:", e