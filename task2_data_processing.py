Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # task2_clean_data.py
... # Trendpulse: clean raw JSON into tidy csv
... # Author: Mayur
... # Date: 10-04-2026
... 
... 
... 
... import pandas as pd
... import os
... 
... # -------------------------------------
... # Step 1: Load JSON File
... # -------------------------------------
... file_path = "data/trends_20260409.json"   # change date if needed
... 
... try:
...     df = pd.read_json(file_path)
...     print(f"Loaded {len(df)} stories from {file_path}")
... except Exception as e:
...     print("Error loading file:", e)
...     exit()
... 
... # -------------------------------------
... # Step 2: Clean the Data
... # -------------------------------------
... 
... # 1. Remove duplicates (based on post_id)
... df = df.drop_duplicates(subset="post_id")
... print(f"After removing duplicates: {len(df)}")
... 
... # 2. Remove missing values
... df = df.dropna(subset=["post_id", "title", "score"])
... print(f"After removing nulls: {len(df)}")
... 
... # 3. Fix data types
... df["score"] = pd.to_numeric(df["score"], errors="coerce")
... df["num_comments"] = pd.to_numeric(df["num_comments"], errors="coerce")
... 
... # Drop rows where conversion failed
... df = df.dropna(subset=["score", "num_comments"])
... 
... # Convert to integer
... df["score"] = df["score"].astype(int)
... df["num_comments"] = df["num_comments"].astype(int)
... 
# 4. Remove low quality (score < 5)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# 5. Clean whitespace in title
df["title"] = df["title"].str.strip()

# -------------------------------------
# Step 3: Save as CSV
# -------------------------------------
if not os.path.exists("data"):
    os.makedirs("data")

output_file = "data/trends_clean.csv"

df.to_csv(output_file, index=False)

print(f"Saved {len(df)} rows to {output_file}")

# -------------------------------------
# Step 4: Category Summary
# -------------------------------------
print("\nStories per category:")

category_counts = df["category"].value_counts()

for category, count in category_counts.items():
