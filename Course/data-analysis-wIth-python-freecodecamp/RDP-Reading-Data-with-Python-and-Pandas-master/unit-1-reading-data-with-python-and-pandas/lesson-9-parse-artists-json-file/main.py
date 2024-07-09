import numpy as np
import pandas as pd

artists = pd.read_json(
    "/home/tinapyp/Downloads/FreeCodeCamp-Data Analysis WIth Python/RDP-Reading-Data-with-Python-and-Pandas-master/unit-1-reading-data-with-python-and-pandas/lesson-9-parse-artists-json-file/files/artists.json"
)
artists.pop("bio")
artists.set_index("name", inplace=True)
artists.to_csv("artists.csv")

## test case
artists.iloc[3]["genre"] == "Impressionism"

i = pd.Index(
    [
        "Amedeo Modigliani",
        "Vasiliy Kandinskiy",
        "Diego Rivera",
        "Claude Monet",
        "Rene Magritte",
    ]
)
artists.index.equals(i)

artists.shape == (5, 3)
