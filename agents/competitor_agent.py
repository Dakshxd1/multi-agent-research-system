# competitor_agent.py
import os
import google.generativeai as genai
from google.api_core.exceptions import TooManyRequests
import time

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def find_competitor_and_compare(topic):
    """
    Uses AI to find a top competitor and generate a Markdown table.
    """
    prompt = f"""
    Find a major competitor to {topic} and create a markdown table comparing them.
    Include at least: Founded Year, Monthly Active Users, Revenue Model, Content Focus.
    """
    retries = 3
    delay = 2
    while retries > 0:
        try:
            print(f"🤖 Finding competitor for: {topic}...")
            resp = model.generate_content(prompt)
            return resp.text.strip()
        except TooManyRequests:
            print(f"⚠️ Got 429 TooManyRequests, retrying in {delay} seconds...")
            time.sleep(delay)
            retries -= 1
            delay *= 2
        except Exception as e:
            print(f"❌ Failed to get competitor info: {e}")
            break
    return "N/A"
