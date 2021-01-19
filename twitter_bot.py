import tweepy as tw

consume_key='xxx'
consumer_secret='xxxxxx'
access_token='xxxx'
access_token_secret='xxxxx'

# handling authentication

auth = tw.OAuthHandler(consume_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth, wait_on_rate_limit=True)

#posting a tweet example

api.update_status("This tweet is to check my api access from #python script")

# .cursor() method will be used to create a iterator object that can leverage api commands and store tweets/info returned.

search_words = "#Zeroday -filter:retweets"
date_since = "2021-01-18" # use a date to specify search scope

tweets = tw.Cursor(api.search, q=search_words, lang="en", since=date_since).items(5)

for tweet in tweets:
    print(tweet.text)

#additional info from tweet like user name and their location

user_info = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]

print(user_info)


