import random
import time

# Hashtag categories based on tweet type
hashtags = {
    "fps": ["#FPSBoost", "#GamingPerformance", "#MaxFPS", "#HighRefreshRate"],
    "latency": ["#LowLatency", "#InputLagFix", "#SmoothGameplay", "#Esports"],
    "overclocking": ["#Overclocking", "#GPUBoost", "#CPUPerformance", "#MaxPower"],
    "windows": ["#WindowsTweaks", "#PowerMode", "#OptimizePC", "#GamingSetup"],
    "general": ["#PCGaming", "#PerformanceTweaks", "#GamingCommunity", "#CompetitiveGaming"]
}

def select_hashtags(category):
    """Chooses the best hashtags based on the tweet's category."""
    if category in hashtags:
        return " ".join(random.sample(hashtags[category], 2))  # Select 2 random hashtags
    return " ".join(random.sample(hashtags["general"], 2))

def generate_tweet_with_hashtags():
    """Simulates a tweet with optimized hashtags."""
    categories = list(hashtags.keys())
    chosen_category = random.choice(categories)
    tweet = f"Boost your {chosen_category} settings for a smoother gaming experience! {select_hashtags(chosen_category)}"
    return tweet

if __name__ == "__main__":
    while True:
        print(f"[Hashtag Optimized Tweet]: {generate_tweet_with_hashtags()}")
        time.sleep(random.randint(3600, 7200))  # Post every 1-2 hours
