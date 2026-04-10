Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# task3_analysis.py
# trendpulse:Analyse cleaned data with pandas + numpy
# Author: Mayur
# Date: 10-04-2026


import pandas as pd
import numpy as np
import os

# -------------------------------------
# Step 1: Load and Explore Data
# -------------------------------------
file_path = "data/trends_clean.csv"

try:
    df = pd.read_csv(file_path)
    print(f"Loaded data: {df.shape}")
except Exception as e:
    print("Error loading file:", e)
    exit()

# First 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Average values
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print(f"\nAverage score: {avg_score:.0f}")
print(f"Average comments: {avg_comments:.0f}")

# -------------------------------------
# Step 2: NumPy Analysis
# -------------------------------------
scores = df["score"].values

mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)
max_score = np.max(scores)
min_score = np.min(scores)

... print("\n--- NumPy Stats ---")
... print(f"Mean score: {mean_score:.0f}")
... print(f"Median score: {median_score:.0f}")
... print(f"Std deviation: {std_score:.0f}")
... print(f"Max score: {max_score}")
... print(f"Min score: {min_score}")
... 
... # Category with most stories
... top_category = df["category"].value_counts().idxmax()
... top_category_count = df["category"].value_counts().max()
... 
... print(f"\nMost stories in: {top_category} ({top_category_count} stories)")
... 
... # Most commented story
... top_commented = df.loc[df["num_comments"].idxmax()]
... print(f'Most commented story: "{top_commented["title"]}" - {top_commented["num_comments"]} comments')
... 
... # -------------------------------------
... # Step 3: Add New Columns
... # -------------------------------------
... 
... # Engagement = comments per upvote
... df["engagement"] = df["num_comments"] / (df["score"] + 1)
... 
... # is_popular = score > average score
... df["is_popular"] = df["score"] > avg_score
... 
... # -------------------------------------
... # Step 4: Save Result
... # -------------------------------------
... if not os.path.exists("data"):
...     os.makedirs("data")
... 
... output_file = "data/trends_analysed.csv"
... df.to_csv(output_file, index=False)
... 
... print(f"\nSaved to {output_file}")
... 
