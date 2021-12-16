import tweepy
import schedule
import requests
import json

client= tweepy.Client(bearer_token="Enter you bearer token here", consumer_key=" enter consumer keys", consumer_secret="enter consumer secret", access_token="enter access token ", access_token_secret="enter access token secret", wait_on_rate_limit=False)


def tweet():
    

    #tweeting
    client.create_tweet(text="Buy when there's blood in the streets, even if the blood is your own.")

def check():
    t= requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").text
    t=json.loads(t)
    price=int(t['bitcoin']['usd'])
    m=requests.get("https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1&interval=daily").text
    m=json.loads(m)
    old=(m["prices"][0][1])
    x=(old-price)/old
    if(x>=.03):
        tweet()
        print("Market is bearish, tweeted")
    

check()
schedule.every(12).hours.do(check)


while True:
   schedule.run_pending()
   time.sleep(1) # wait one minute