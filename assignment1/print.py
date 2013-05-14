import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
#print json.load(response)
pyresponse = json.load(response)
#print type(pyresponse)
#print (pyresponse.keys())
#print pyresponse["results"]
#print type(pyresponse["results"])
results = pyresponse["results"]
#print results[0]
#print results[0].keys()
#print len(results)
#print results[0]["text"]

for index in range(len(results)):
	print results[index]["text"] 

