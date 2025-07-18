import google.generativeai as genai
import os

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-pro")

def disambiguate_topic(topic: str) -> str:
    """
    Uses Gemini to clarify ambiguous topics (e.g., Apple → Apple Inc.).
    Ensures returned topic is short and suitable for Wikipedia/Web research.
    """
    prompt = f"""Disambiguate the following topic for AI research:
If it's ambiguous (e.g., "Apple"), specify whether it's a company, fruit, person, etc.
Give a short, unambiguous version of the topic suitable for web research and Wikipedia lookup.

Examples:
- Topic: Apple → Refined: Apple Inc.
- Topic: Amazon → Refined: Amazon (company)
- Topic: Mercury → Refined: Mercury (planet)

Now refine this:
Topic: {topic}
Refined:"""

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()

        # Parse the refined topic from the response
        if "Refined:" in text:
            refined = text.split("Refined:")[-1].strip().strip('"')
        else:
            refined = text.strip().strip('"')

        # Return refined if not empty, else fallback
        return refined if refined else topic

    except Exception as e:
        print(f"⚠️ Failed to disambiguate topic: {e}")
        return topic
