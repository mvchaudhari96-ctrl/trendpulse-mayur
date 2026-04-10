Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # task1_data_collection.py
... # trendpulse:Fetch trending HackerNews stories categorize them
... # Author: Mayur
... # Date: 10-04-2026
... 
... import requests
... import time
... import json
... import os
... from datetime import datetime
... 
... # -------------------------------------
... # Step 1: Define API URLs
... # -------------------------------------
... TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
... ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"
... 
... headers = {
...     "User-Agent": "TrendPulse/1.0"
... }
... 
... # -------------------------------------
... # Step 2: Define Categories & Keywords
... # -------------------------------------
... categories = {
...     "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
...     "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
...     "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
...     "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
...     "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
... }
... 
... # -------------------------------------
... # Step 3: Function to Assign Category
... # -------------------------------------
... def assign_category(title):
...     title = title.lower()
...     for category, keywords in categories.items():
...         for keyword in keywords:
...             if keyword.lower() in title:
...                 return category
...     return "other"
... 
... # -------------------------------------
... # Step 4: Fetch Top Story IDs
# -------------------------------------
try:
    response = requests.get(TOP_STORIES_URL, headers=headers)
    story_ids = response.json()[:500]  # first 500
except Exception as e:
    print("Error fetching top stories:", e)
    story_ids = []

# -------------------------------------
# Step 5: Collect Stories
# -------------------------------------
collected_stories = []
category_count = {cat: 0 for cat in categories}

for story_id in story_ids:
    try:
        res = requests.get(ITEM_URL.format(story_id), headers=headers)
        story = res.json()

        if story is None or "title" not in story:
            continue

        title = story.get("title", "")
        category = assign_category(title)

        # Only collect defined categories
        if category not in categories:
            continue

        # Limit 25 per category
        if category_count[category] >= 25:
            continue

        # Extract fields
        data = {
            "post_id": story.get("id"),
            "title": title,
            "category": category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by", "unknown"),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        collected_stories.append(data)
        category_count[category] += 1

        # Stop if all categories full
        if all(count >= 25 for count in category_count.values()):
            break

    except Exception as e:
        print(f"Error fetching story {story_id}: {e}")
        continue

# -------------------------------------
# Step 6: Create Data Folder
# -------------------------------------
if not os.path.exists("data"):
    os.makedirs("data")

# -------------------------------------
# Step 7: Save JSON File
# -------------------------------------
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w", encoding="utf-8") as f:
    json.dump(collected_stories, f, indent=4)

# -------------------------------------
# Step 8: Final Output
# -------------------------------------
print(f"Collected {len(collected_stories)} stories.")
