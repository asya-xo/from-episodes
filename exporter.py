# file that handles CSV export with Pandas

import pandas as pd
import time
from fetcher import fetch_episode_details

def get_season(title):
  data = fetch_episode_details(title)
  pages = data["query"]["pages"]
  page = list(pages.values())[0]
  categories = page.get("categories", [])
  

  for cat in categories:
        if "Season 1" in cat["title"]:
            return 1
        elif "Season 2" in cat["title"]:
            return 2
        elif "Season 3" in cat["title"]:
            return 3
        elif "Season 4" in cat["title"]:
            return 4
        return 0

def export_episodes(data):
    episodes = data["query"]["categorymembers"]
    df = pd.DataFrame(episodes)
    
    df = df[~df['title'].str.contains("Category:|MediaWiki:")]
    df = df.drop(columns=["pageid", "ns"])
    df = df.reset_index(drop=True)
    
    # get season for each episode
    print("Fetching season info....")
    df["season"] = df["title"].apply(lambda t: (time.sleep(0.5) or get_season(t)))
    
    df = df.sort_values(["season", "title"]).reset_index(drop=True)
    df.to_csv("episodes.csv", index=False)
    print("Done, episodes.csv has been created")
