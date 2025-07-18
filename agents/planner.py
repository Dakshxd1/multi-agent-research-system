# agents/planner.py
import google.generativeai as genai
import os
import time

# Configure Gemini with your API key
genai.configure(api_key="AIzaSyCs5fIyQsGb0BGYOuCCFEmHA_6HeQjoeBQ")
planner = genai.GenerativeModel("gemini-2.0-flash")

def plan_topic(topic):
    prompt = f"Divide the topic '{topic}' into 3–5 detailed subtopics for research."

    retries = 3
    delay = 2
    while retries > 0:
        try:
            print(f"🧠 Sending request to Gemini for topic: {topic} ...")
            resp = planner.generate_content(prompt, safety_settings=None)
            text = resp.text
            print("✅ Response received from Gemini.")
            subtopics = text.strip().split('\n')
            cleaned = [s.strip('-• ').strip() for s in subtopics if s.strip()]
            print(f"📋 Planned subtopics: {cleaned}")
            return cleaned
        except Exception as e:
            print(f"⚠️ Error: {e} — retrying in {delay} seconds...")
            time.sleep(delay)
            retries -= 1
            delay *= 2
    print("❌ Failed to get subtopics after retries.")
    return []
