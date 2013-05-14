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
	freq_dic = {}
	punctuation = re.compile(r'[.?!,":;)]') 
	word_list = tweets.split(" ")
	for word in word_list:
		# remove punctuation marks
		word = punctuation.sub("", word)
		try:
			freq_dic[word] += 1
		except:
			freq_dic[word] = 1	

	for word_key in freq_dic.keys():
		print word_key + " " + str(float(freq_dic[word_key]) / len(freq_dic))

	
def main():
	# Tweets 
	tweets = lines_tweets_json(sys.argv[1]) 	
	#tweets = ["RT @miguelinlas3 Why Linux is faster than Windows http://blog.zorinaq.com/?e=74  written by a Windows kernel developer","Does not work doubt can't stand", "Worth celebrated celebrates"]		
	all_tweets = " ".join(tweets)
	
	# Calculate Sentiment Scores 
	frequency(all_tweets)
		
if __name__ == '__main__':
	try:
		main()
	except Exception, e:
		print "Error:", e