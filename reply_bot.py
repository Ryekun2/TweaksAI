import time
import random

# Simulated incoming tweets
incoming_tweets = [
    "My FPS keeps dropping, any fixes?",
    "Best settings for lower input delay?",
    "Should I overclock my GPU for better performance?",
    "Windows update ruined my FPS. Help!",
    "What’s the best power plan for gaming?"
]

# Predefined AI-generated responses
responses = [
    "Try tweaking your in-game settings and disabling V-Sync for a smoother experience!",
    "Lower input delay by adjusting your polling rate and enabling high-performance mode.",
    "Overclocking can help, but make sure to monitor temps and use safe voltage settings.",
    "Rollback the latest Windows update or disable background tasks for better FPS.",
    "Set your power plan to High Performance and disable unnecessary startup programs."
]

def auto_reply():
    """Randomly selects an incoming tweet and generates a reply."""
    tweet = random.choice(incoming_tweets)
    response = random.choice(responses)
    return f"Replying to: '{tweet}'\nAI Response: '{response}'"

if __name__ == "__main__":
    while True:
        print(auto_reply())
        time.sleep(random.randint(1800, 5400))  # Auto-reply every 30-90 minutes
