#! /usr/bin/env python3
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import validus

analyzer = SentimentIntensityAnalyzer()

df = pd.read_csv('/home/deeplearning/python/FaStA/facebook-page-post-scraper/759985267390294_facebook_statuses.csv')

#TODO: Make plot with pandas. Append other columns using sentiment analysis tool
for i in range(15):
    sentence = df['status_message'][i]
    try:
        if validus.isurl(sentence) or validus.isfloat(sentence):
            continue
        else:
            vs = analyzer.polarity_scores(sentence)
            print("{:-<65} {}".format(sentence, str(vs)))
    except TypeError:
        print('Not a string!!!!')
