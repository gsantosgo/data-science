import sys, re, json 

# ==============================================================================================
# Introduction to Data Science 
# 
# Guillermo Santos (@gsantosgo) 
#
# Subject: Derive the sentiment of new terms
# Description: 
#		You will be creating a script that computes the sentiment for the terms that do not appear in the file AFINN-111.txt.
#
#		Here's how you might think about the problem: We know we can use certain words to deduce the sentiment of a tweet. 
#		Once you know the sentiment of the tweets that contain some term, you can assign a sentiment to the term itself. 

# 		You are provided with a skeleton file, tweet_sentiment.py, which can be executed using the following command:
#          $ python tweet_sentiment.py <sentiment_file> <tweet_file>
#
#       Ex:$ python tweet_sentiment.py AFINN-111.txt output.json
#
#		The file AFINN-111.txt contains a list of pre-computed sentiment scores. Each line in the file contains 
#		a word or phrase followed by a sentiment score. Each word or phrase found in a tweet, 
#		but not in AFINN-111.txt should be given a sentiment score of 0. 
#		See the file AFINN-README.txt for more information.
#
#
#		Your script should print to stdout the sentiment of each tweet in the file, one sentiment per line:     
#          <sentiment:float>
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
		if 'text' in tweet_dict.keys():
			text = tweet_dict["text"].encode('utf-8')
			tweets.append(text)
	tweets_file.close()
	return tweets

def processTweet(text):	
	tokens = re.split(" ", text.lower())
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
		
		for word_phrase in tweet_word_phrases: 					
			word_score = scores_dict[word_phrase] if word_phrase in scores_dict else (float(score)/len(tweet_word_phrases))
			print "" + word_phrase + " " + str(float(word_score)) + ""
	
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