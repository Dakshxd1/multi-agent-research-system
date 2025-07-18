import google.generativeai as genai
import os
import time
import random

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
critic = genai.GenerativeModel("gemini-2.0-flash")

def is_weak_claim(text):
    """
    Checks if a claim is vague, generic, or lacks specificity.
    """
    weak_starters = [
        "the article discusses", "this article is about", "this piece talks about",
        "information is provided", "this is an overview", "the main topic is"
    ]
    text_lower = text.lower()
    return any(text_lower.startswith(ws) for ws in weak_starters) or len(text) < 40

def retry_with_alternative(article, max_retries=2):
    """
    If the original claim is weak, regenerate it from the same content.
    """
    for _ in range(max_retries):
        try:
            prompt = f"Regenerate the main claim more clearly from the following:\n{article['content'][:1000]}"
            resp = critic.generate_content(prompt)
            alt_claim = resp.text.strip().split('\n')[0]
            if not is_weak_claim(alt_claim) and len(alt_claim) > 20:
                return alt_claim
            time.sleep(1.5)
        except Exception as e:
            print(f"⚠️ Retry failed: {e}")
    return None

def validate_claims(articles):
    verified = []
    for idx, art in enumerate(articles, 1):
        prompt = f"Summarize the main claim:\n{art['content'][:1000]}"
        try:
            print(f"🧐 Validating article {idx}/{len(articles)}...")
            resp = critic.generate_content(prompt)
            raw_claim = resp.text.strip().split('\n')[0]

            if not raw_claim or raw_claim.lower().startswith("please provide"):
                continue

            # Self-correction loop
            if is_weak_claim(raw_claim):
                print(f"🔁 Weak claim detected. Retrying...")
                better = retry_with_alternative(art)
                if better:
                    raw_claim = better
                else:
                    print("❌ Could not improve weak claim.")
                    continue

            verified.append({
                "claim": raw_claim.strip(),
                "subtopic": art.get('subtopic', 'General'),
                "source_url": art.get('url', 'N/A'),
                "source_text_snippet": art.get('content', '')[:250],
                "verified": True
            })

        except Exception as e:
            print(f"❌ Validation failed: {e}")
        time.sleep(1.5)

    return verified
