import time
import random

# Simulated tweet engagement data
tweet_engagement = {}

def track_engagement(tweet_id):
    """Simulates tracking engagement metrics for a tweet."""
    if tweet_id not in tweet_engagement:
        tweet_engagement[tweet_id] = {"likes": 0, "retweets": 0, "replies": 0}

    # Simulating engagement growth
    tweet_engagement[tweet_id]["likes"] += random.randint(1, 10)
    tweet_engagement[tweet_id]["retweets"] += random.randint(0, 5)
    tweet_engagement[tweet_id]["replies"] += random.randint(0, 3)

    return tweet_engagement[tweet_id]

def analyze_top_performing_tweets():
    """Analyzes which tweets are getting the most engagement."""
    if not tweet_engagement:
        return "No engagement data yet."

    sorted_tweets = sorted(tweet_engagement.items(), key=lambda x: x[1]["likes"], reverse=True)
    top_tweet = sorted_tweets[0]
    return f"Top Tweet (ID: {top_tweet[0]}) - Likes: {top_tweet[1]['likes']}, Retweets: {top_tweet[1]['retweets']}, Replies: {top_tweet[1]['replies']}"

if __name__ == "__main__":
    # Simulating tweet posting and engagement tracking
    for i in range(5):  # Simulating 5 tweets
        tweet_id = f"tweet_{i}"
        time.sleep(random.randint(5, 10))  # Short delay for realism
        print(f"Tracking engagement for {tweet_id}")
        track_engagement(tweet_id)

    print("Engagement Analysis:", analyze_top_performing_tweets())
