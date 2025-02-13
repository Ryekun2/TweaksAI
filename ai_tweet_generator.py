import time
import random
import openai  # Assuming OpenAI API, but you can swap it with any local LLM API

# Set up OpenAI API key (Replace with your local LLM endpoint if needed)
openai.api_key = "your-api-key-here"  # Replace with actual API key

def generate_ai_tweet():
    """Generates a tweet using an LLM based on performance optimization themes."""
    prompt = (
        "Generate a short, engaging tweet about gaming performance optimizations. "
        "Focus on increasing FPS, reducing input delay, and optimizing system settings."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use "gpt-4", "gpt-3.5-turbo" or your custom LLM
            messages=[{"role": "system", "content": "You are an AI expert in gaming performance."},
                      {"role": "user", "content": prompt}],
            max_tokens=50
        )
        tweet = response["choices"][0]["message"]["content"].strip()
        return tweet

    except Exception as e:
        return f"Error generating tweet: {e}"

if __name__ == "__main__":
    while True:
        tweet = generate_ai_tweet()
        print(f"[AI Generated Tweet]: {tweet}")
        time.sleep(random.randint(3600, 7200))  # Post every 1-2 hours
