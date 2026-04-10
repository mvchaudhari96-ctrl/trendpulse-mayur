Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# task4_visualization.py
# trendpulse: make charts from analysed data
# Author: Mayur
# Date: 10-04-2026



import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------------
# Step 1: Setup
# -------------------------------------
file_path = "data/trends_analysed.csv"

try:
    df = pd.read_csv(file_path)
    print("Data loaded successfully")
except Exception as e:
    print("Error loading file:", e)
    exit()

# Create outputs folder
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# -------------------------------------
# Step 2: Chart 1 - Top 10 Stories by Score
# -------------------------------------
top10 = df.sort_values(by="score", ascending=False).head(10)

# Shorten long titles
top10["short_title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

plt.figure()
plt.barh(top10["short_title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()

plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# -------------------------------------
# Step 3: Chart 2 - Stories per Category
# -------------------------------------
category_counts = df["category"].value_counts()

plt.figure()
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.close()

# -------------------------------------
# Step 4: Chart 3 - Score vs Comments
# -------------------------------------
plt.figure()

popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
... plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
... 
... plt.xlabel("Score")
... plt.ylabel("Number of Comments")
... plt.title("Score vs Comments")
... plt.legend()
... 
... plt.tight_layout()
... plt.savefig("outputs/chart3_scatter.png")
... plt.close()
... 
... # -------------------------------------
... # Step 5: Bonus Dashboard
... # -------------------------------------
... fig, axs = plt.subplots(2, 2)
... 
... # Chart 1
... axs[0, 0].barh(top10["short_title"], top10["score"])
... axs[0, 0].set_title("Top Stories")
... 
... # Chart 2
... axs[0, 1].bar(category_counts.index, category_counts.values)
... axs[0, 1].set_title("Categories")
... 
... # Chart 3
... axs[1, 0].scatter(popular["score"], popular["num_comments"])
... axs[1, 0].set_title("Score vs Comments")
... 
... # Empty subplot
... axs[1, 1].axis("off")
... 
... fig.suptitle("TrendPulse Dashboard")
... 
... plt.tight_layout()
... plt.savefig("outputs/dashboard.png")
... plt.close()
... 
... print("All charts saved in outputs/ folder")
