import numpy as np
import pandas as pd
import requests

fifa_df = pd.read_html(
    "/home/tinapyp/Downloads/FreeCodeCamp-Data Analysis WIth Python/RDP-Reading-Data-with-Python-and-Pandas-master/unit-1-reading-data-with-python-and-pandas/lesson-18-get-fifa-players-from-the-web/files/fifa_players.html"
)
fifa_df = fifa_df[0]
fifa_df = fifa_df.iloc[:, 2:-1]

most_hits_player = fifa_df.loc[fifa_df["Hits"] == fifa_df["Hits"].max()]
