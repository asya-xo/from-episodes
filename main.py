#file that runs everything

from fetcher import fetch_episodes
from exporter import export_episodes

data = fetch_episodes()
export_episodes(data)
