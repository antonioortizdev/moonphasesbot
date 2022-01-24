import schedule
from tweet import tweet
import tweepy

def main():
    schedule.every().day.at('12:00').do(tweet)

    while True:
        try:
            schedule.run_pending()
        except tweepy.errors.TweepError as e:
            raise e

if __name__ == "__main__":
    main()