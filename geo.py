#!/usr/bin/env python
from twitter import *
from textblob import TextBlob
import sys
import csv

latitude = float(input("please latitude:"))    # geographical centre of search
longitude = float(input("please longitude:"))   # geographical centre of search
max_range = float(input("please km?:"))            # search range in kilometres
num_results = float(input("please max tweet:"))
print("----------------------------wait please----------------------------------")        # minimum results to obtain
outfile = "output.csv"

import sys
sys.path.append(".")
import config


twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))


csvfile = open(outfile, "w")
csvwriter = csv.writer(csvfile)


row = [ "user", "text", "latitude", "longitude" ]
csvwriter.writerow(row)


result_count = 0
last_id = None
while result_count <  num_results:
    query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100, max_id = last_id)

    for result in query["statuses"]:

        if result["geo"]:
            user = result["user"]["screen_name"]
            text = result["text"]
            text = text.encode('utf-8')
            latitude = result["geo"]["coordinates"][0]
            longitude = result["geo"]["coordinates"][1]
            
            data = user,":","",text,"",latitude,longitude,"","sentiment analysis:"
            print(data)
            print("-------------------------------------------------------------")





            row = [ user, text, latitude, longitude ,sentiment ]
            csvwriter.writerow(row)
            result_count += 1
        last_id = result["id"]





csvfile.close()

print("Received intelligence data saved.. %s" % outfile)
