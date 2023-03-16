import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(from:elonmusk) until:2023-03-03 since:2015-01-01"
tweets = []
limit = 1000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

df.to_csv('tweets.csv')

# to save to csv
# df.to_csv('tweets.csv')