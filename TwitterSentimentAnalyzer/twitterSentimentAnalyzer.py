import tweepy
from textblob import TextBlob
import pandas

bearer_token = ***

client = tweepy.Client(bearer_token)

def fetch_tweets(query, max_results = 20):
    tweets = client.search_recent_tweets(query=query, max_results=max_results, tweet_field= ['text'])
    return [tweet.text for tweet in tweets.data]

msft_tweets = fetch_tweets("MSFT", max_results=20)

def analyze_sentiment(tweets):
    sentiments = [TextBlob(tweet).sentiment.polarity for tweet in tweets]
    return pandas.DataFrame({'Tweet':tweets, 'Sentiment':Sentiments})
    
msft_sentiment = analyze_sentiment(msft_tweets)

print(msft_sentiments.head())


def summarize_sentiments(sentiments_df):
    avg_sentiment = sentiments_df['Sentiment'].mean()
    return avg_sentiment
    
msft_avg_sentiment = summarize_sentiments(msft_sentiment)
