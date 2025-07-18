import os
import importlib.util
from dotenv import load_dotenv
import wikipedia
from agents.disambiguator_agent import disambiguate_topic

# Load environment variables
load_dotenv()

# Dynamically load agent modules
def load_agent_module(name, filename):
    agents_dir = os.path.join(os.path.dirname(__file__), "agents")
    path = os.path.join(agents_dir, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Agent module not found: {path}")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Load all agents
planner = load_agent_module("planner", "planner.py")
researcher = load_agent_module("researcher", "researcher.py")
critic = load_agent_module("critic", "critic.py")
competitor = load_agent_module("competitor", "competitor_agent.py")
report_writer = load_agent_module("report_writer", "report_writer.py")

if __name__ == "__main__":
    raw_topic = input("📌 Enter your topic: ").strip()

    # Step 1: Disambiguate
    print("\n🧠 Disambiguating topic...")
    topic = disambiguate_topic(raw_topic)
    print(f"✅ Refined Topic: {topic}")

    # Step 2: Plan subtopics
    print("\n📍 Planning subtopics...")
    subtopics = planner.plan_topic(topic)
    print(f"✅ Subtopics:")
    for i, s in enumerate(subtopics, 1):
        print(f"   {i}. {s}")

    # Step 3: Get introduction
    print("\n📚 Fetching introduction from Wikipedia...")
    try:
        intro = wikipedia.summary(topic, sentences=4, auto_suggest=True, redirect=True)
    except Exception:
        try:
            intro = wikipedia.summary(f"{topic} (company)", sentences=4)
        except Exception as e:
            print(f"⚠️ Could not fetch intro from Wikipedia: {e}")
            intro = f"This report explores various aspects of {topic}."

    # Step 4: Research
    print("\n🔍 Researching articles...")
    articles = researcher.research_subtopics(subtopics)
    print(f"✅ {len(articles)} articles found.")

    # Step 5: Validate claims
    print("\n🧐 Validating claims with Gemini...")
    verified_claims = critic.validate_claims(articles)
    print(f"✅ {len(verified_claims)} claims validated.")

    # Step 6: Competitor analysis
    print("\n🏢 Finding competitors...")
    competitor_table = competitor.find_competitor_and_compare(topic)

    # Step 7: Report generation
    print("\n📝 Generating Word report...")
    report_writer.generate_report_docx(
        topic, intro, verified_claims, competitor_table
    )

    print("\n✅ All done! Report generated successfully.")
