import tweepy
from config import *


# 認証に必要なキーとトークンはconfigから取得
# APIの認証
API_Auth = tweepy.OAuthHandler(API_Key, API_Key_Secret)
API_Auth.set_access_token(Access_Token, Access_Token_Secret)

# キーワードからツイートを取得
api = tweepy.API(API_Auth)
#tweets = api.search_tweets(q=['ラーメン'], count=10)

#for tweet in tweets:
#    print('-----------------')
#    print(tweet.text)

#ツイート取得
data = []

#多くツイートを取得するための用意
pages = [1,2,3,4,5,6,7,8,9,10]

for page in pages:
    GetData = api.user_timeline(screen_name="tenkijp_jishin", count=200, page=page)
    for r in GetData:
		#r.textで、投稿の本文のみ取得する
        data.append(r.text)

LINE = ''.join(data)
with open("input_data.txt", 'wt') as TEXT:
    TEXT.write(LINE)


