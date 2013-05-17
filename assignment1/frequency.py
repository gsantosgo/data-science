import sys, re, json

# ==============================================================================================
# Introduction to Data Science 
# 
# Guillermo Santos (@gsantosgo) 
#
# Subject: Compute Term Frequency
# Description: 
#		You will compute the sentiment of each tweet based on the sentiment scores of the terms in the tweet. 
#
#		The frequency of a term can be calculate with the following formula:
#		[# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]
#
# 
#		frequency.py should take a file of tweets as an input and be usable in the following way:
#
#          $ python frequency.py <tweet_file>
# 		Assume the tweet file contains data formatted the same way as the livestream data.
#
#		Your script should print to stdout each term-frequency pair, one pair per line, in the following format:      
#          <term:string> <frequency:float>
#
#		For example, if you have the pair (bar, 0.1245) it should appear in the output as:
#          bar 0.1245
#
# 		Frequency measurements may take phrases into account, but this is not required. 
#		We only ask that you compute frequencies for individual tokens.
#
#		Depending on your method of parsing, you may end up with frequencies for hashtags, links, stop words, phrases, etc. 
#		Some noise is acceptable for the sake of keeping parsing simple.
# ---------------------------------------------------------------------------------------------
	
def lines_tweets_json(filename):
	tweets_file = open(filename)
	tweets = []
	for line in tweets_file:
		tweet_dict = json.loads(line)
		if 'text' in tweet_dict.keys():
			text = tweet_dict["text"].encode('utf-8')
			tweets.append(text.lower())
	tweets_file.close()
	return tweets
		
def frequency(tweets): 			
	totalTerms  = 0.0 
	freq_dic = {}
	for x in tweets:
		for word in x.split():
			totalTerms += 1 
			if word in freq_dic:
				x = (freq_dic)[word] + 1.0		
				freq_dic[word] += x
			elif word.isalnum() or "," in word:
				freq_dic[word] = 1.0
	for x in range(len(freq_dic)):
		print freq_dic.keys()[x] + " " + str(freq_dic.values()[x] / totalTerms)	
	
def main():
	# Tweets 
	tweets = lines_tweets_json(sys.argv[1]) 	
	#tweets = ["RT @miguelinlas3 Why Linux is faster than Windows http://blog.zorinaq.com/?e=74  written by a Windows kernel developer","Does not work doubt can't stand", "Worth celebrated celebrates"]		
		
	# Calculate Sentiment Scores 
	frequency(tweets)
		
if __name__ == '__main__':
	try:
		main()
	except Exception, e:
		print "Error:", e