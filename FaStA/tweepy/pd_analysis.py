import pandas as pd

df = pd.read_csv('2017-06-19-realDonaldTrump-sentimentanalysis.csv')
df.describe()

df[['Negative Score', 'Retweet Count', 'Like Count']].corr()  # gets correlation between scores, retweets and likes
