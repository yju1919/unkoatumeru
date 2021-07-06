import tweepy
import time
import schedule

CONSUMER_KEY = CONFIG["G7w3N5D2zX9EeYtwPvD8TnAME"]
CONSUMER_SECRET = CONFIG["Uojw5wO2cv2QATMaOCG8avsWVISuDSb3u1riVgi1zCiAWuNuGW"]
ACCESS_TOKEN = CONFIG["1412356568054566918-5cnMxTEOCQeWRySzdQwCrdrLTB9GQP"]
ACCESS_SECRET = CONFIG["xuYoeS3Qdx77RhRkfgSW6atDd7NmIPnnF4N6F3mqFusAw"]

auth = tweepy.0AuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

def job():

    for status in api.search(q="うんこ💩", count=50):
        tweet_id = status.id

        try:

            api.retweet(tweet_id)
        except:
            print('error')
        
def main():
    schedule.every(1).minutes.do(job)


    while True:
        schedule.run_pending()
        time.sleep(1)

main()

