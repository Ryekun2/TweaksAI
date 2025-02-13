import random
import time
import os

# Simulated images (these would be actual file paths in a real implementation)
image_library = {
    "fps": ["images/fps_boost1.png", "images/fps_boost2.png", "images/fps_graph.png"],
    "latency": ["images/low_latency1.png", "images/input_lag_fix.png"],
    "overclocking": ["images/overclock_tips.png", "images/gpu_tuning.png"],
    "windows": ["images/windows_performance.png", "images/power_settings.png"],
    "general": ["images/gaming_setup.png", "images/pc_optimization.png"]
}

def select_image(category):
    """Randomly selects an image from the appropriate category."""
    if category in image_library and image_library[category]:
        return random.choice(image_library[category])
    return random.choice(image_library["general"])  # Default fallback

def generate_tweet_with_image():
    """Simulates a tweet with an attached image."""
    categories = list(image_library.keys())
    chosen_category = random.choice(categories)
    image = select_image(chosen_category)
    tweet = f"Optimize your {chosen_category} settings for maximum gaming performance! 🖥️🔥 {image}"
    return tweet

if __name__ == "__main__":
    while True:
        print(f"[Tweet with Image]: {generate_tweet_with_image()}")
        time.sleep(random.randint(3600, 7200))  # Post every 1-2 hours
