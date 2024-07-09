import numpy as np
import pandas as pd
import requests

url = "https://swapi.co/api/people/?format=json"
starwars_people_df = pd.read_json(requests.get(url).json()["results"])

blue_eyed_people_df = starwars_people_df.loc[starwars_people_df["eye_color"] == "blue"]
