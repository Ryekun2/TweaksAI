import time
import random
from datetime import datetime

# Define peak engagement hours (in 24-hour format)
PEAK_HOURS = [9, 12, 15, 18, 21]  # 9 AM, 12 PM, 3 PM, 6 PM, 9 PM

def is_peak_hour():
    """Checks if the current hour is within peak engagement hours."""
    current_hour = datetime.now().hour
    return current_hour in PEAK_HOURS

def schedule_tweet():
    """Schedules tweets to be posted only during peak hours."""
    while True:
        if is_peak_hour():
            print("[Scheduled Tweet]: AI agent is posting an optimized tweet!")
            # Here you would call the AI tweet generator (import and use `generate_ai_tweet()`)
        else:
            print("Outside peak hours. Waiting...")
        
        time.sleep(random.randint(1800, 3600))  # Check every 30-60 minutes

if __name__ == "__main__":
    schedule_tweet()
