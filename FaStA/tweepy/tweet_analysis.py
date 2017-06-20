from oauth import login
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import date
import csv
import tweepy

analyzer = SentimentIntensityAnalyzer()
api = login()[2]

screen_name = "realDonaldTrump"
today = date.today()

#timeline = api.user_timeline(screen_name=screen_name,count=1000)

count = 1

fields = ['Number', 'Tweet Text', 'Negative Score', 'Positive Score', 'Retweet Count', 'Like Count']

print("Now gathering tweet data for %s..." % screen_name)

with open('%s-%s-sentimentanalysis.csv' % (today, screen_name), 'w') as stats:
    stats_writer = csv.writer(stats)
    stats_writer.writerow(fields)

    page_list = []
    for page in tweepy.Cursor(api.user_timeline, count=200, id=screen_name).pages(16):
        page_list.append(page)

    for page in page_list:
        for tweet in page:
            if "RT" in tweet.text:
                continue
            vs = analyzer.polarity_scores(tweet.text)
            negative = vs['neg']
            positive = vs['pos']
            like_count = tweet.favorite_count
            retweet_count = tweet.retweet_count
            print("%s.\t%s\t%s\t%s\t%s\t%s" % (count, tweet.text, negative, positive, retweet_count, like_count))
            stats_writer.writerow([count, tweet.text, negative, positive, retweet_count, like_count])
            count += 1
