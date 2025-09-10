import tweepy
from textblob import TextBlob
import pandas

# API credentials
bearer_token = ***

# Initialize tweepy
client = tweepy.Client(bearer_token)

# Function to collect recent tweets mentioning string passed in for search query
def fetch_tweets(query, max_results = 20):
    tweets = client.search_recent_tweets(query=query, max_results=max_results, tweet_field= ['text'])
    return [tweet.text for tweet in tweets.data]


googl_tweets = fetch_tweets("GOOGL", max_results=20)
msft_tweets = fetch_tweets("MSFT", max_results=20)

# Function for sentiment analysis using TextBlob and organization of results using DataFram
def analyze_sentiment(tweets):
    sentiments = [TextBlob(tweet).sentiment.polarity for tweet in tweets]
    return pandas.DataFrame({'Tweet': tweets, 'Sentiment': sentiments})

googl_sentiment = analyze_sentiment(googl_tweets)
msft_sentiment = analyze_sentiment(msft_tweets)

print(googl_sentiments.head())
print(msft_sentiments.head())

# Determine average sentiment
def summarize_sentiments(sentiments_df):
    avg_sentiment = sentiments_df['Sentiment'].mean()
    return avg_sentiment
    
googl_avg_sentiment = summarize_sentiments(googl_sentiment)
msft_avg_sentiment = summarize_sentiments(msft_sentiment)
