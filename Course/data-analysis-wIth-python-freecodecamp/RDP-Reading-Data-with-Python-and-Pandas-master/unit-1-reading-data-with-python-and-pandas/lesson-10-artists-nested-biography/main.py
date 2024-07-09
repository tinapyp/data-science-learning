import numpy as np
import pandas as pd
import json
from pandas.io.json import json_normalize


path = "/home/tinapyp/Downloads/FreeCodeCamp-Data Analysis WIth Python/RDP-Reading-Data-with-Python-and-Pandas-master/unit-1-reading-data-with-python-and-pandas/lesson-10-artists-nested-biography/files/artists.json"
with open(path, "r") as file:
    artists_json = json.load(file)
    file.close()

artists = json_normalize(artists_json)

biography = json_normalize(artists_json, record_path="bio", meta="name")


# test case
artists.shape == (5, 5)
artists.iloc[2]["name"] == "Diego Rivera"
biography.shape == (5, 7)
biography.iloc[4]["paintings"] == 194
biography.iloc[3]["name"] == "Claude Monet"
