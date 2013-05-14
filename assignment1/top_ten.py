import sys, re, json 

# ==============================================================================================
# Introduction to Data Science 
# 
# Guillermo Santos (@gsantosgo) 
#
# Subject: Top ten hash tags
# Description: 
#	Write a Python script, top_ten.py, that computes the ten most frequently occurring hash tags from the data you gathered in Problem 1.
#
#	top_ten.py should take a file of tweets as an input and be usable in the following way:
#
#	   $ python top_ten.py <tweet_file>
#
#	Assume the tweet file contains data formatted the same way as the livestream data.
#	In the tweet file, each line is a Tweet object, as described in the twitter documentation.
#	You should not be parsing the "text" field.
#
# 	Your script should print to stdout each hashtag-count pair, one per line, in the following format:
#
#		<hashtag:string> <count:float>
#
#	For example, if you have the pair (baz, 30) it should appear in the output as:
#
#       baz 30.0
#
#	Remember your output must contain floats, not ints.
# 
# ---------------------------------------------------------------------------------------------
	
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

	
def top_ten(tweets): 		
	hashtag_dic = {}
	hashtag = re.compile(r'#[0-9a-zA-Z+_]+',re.IGNORECASE)	
	word_list = hashtag.findall(tweets)
	for word in word_list:
		try:
			hashtag_dic[word] += 1
		except:
			hashtag_dic[word] = 1	
		
	sorted_list = [x for x in hashtag_dic.iteritems()]
	#sorted_list.sort(key=lambda x: x[0]) # sort by key
	sorted_list.sort(key=lambda x: x[1]) # sort by value
	# to reverse the sort
	sorted_list.reverse()

	if len(sorted_list) >= 10:
		limit = 10
	else: 
		limit = len(sorted_list)
		
	for index in range(limit):
		print sorted_list[index][0] + " " + str(float(sorted_list[index][1]))
			
def main():
	# Tweets 
	tweets = lines_tweets_json(sys.argv[1]) 	
	#tweets = ["RT @gsantosgo Why Linux is faster than Windows http://blog.zorinaq.com/?e=74  written by a Windows kernel developer # #  #Windows","#Rstats Mineria Does not work doubt #hola can't stand", "Worth celebrated celebrates #RStats","#RStats prueba"]
	
	all_tweets = " ".join(tweets)
	# Calculate Sentiment Scores 
	top_ten(all_tweets)
	
if __name__ == '__main__':
	try:
		main()
	except Exception, e:
		print "Error:", e