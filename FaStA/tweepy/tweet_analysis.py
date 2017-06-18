from oauth import login
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
api = login()[2]

timeline = api.user_timeline(screen_name="realDonaldTrump",count=50)

count = 0
for tweet in timeline:
    if "RT" in tweet.text:
        continue
    vs = analyzer.polarity_scores(tweet.text)
    negative = vs['neg']
    retweet_count = tweet.retweet_count
    print("%s.\t%s\t%s\t%s" % (count, tweet.text, negative, retweet_count))
    count += 1
