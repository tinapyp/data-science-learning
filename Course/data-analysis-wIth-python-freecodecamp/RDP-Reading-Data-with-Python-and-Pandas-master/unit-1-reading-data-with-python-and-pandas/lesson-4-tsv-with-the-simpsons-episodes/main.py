import numpy as np
import pandas as pd

col_names = [
    "Title",
    "Air date",
    "Production code",
    "Season",
    "Number in season",
    "Number in series",
    "US viewers (million)",
    "Views",
    "IMDB rating",
]

simpsons = pd.read_csv(
    "/home/tinapyp/Downloads/FreeCodeCamp-Data Analysis WIth Python/RDP-Reading-Data-with-Python-and-Pandas-master/unit-1-reading-data-with-python-and-pandas/lesson-4-tsv-with-the-simpsons-episodes/files/simpsons-episodes.tsv",
    header=None,
    names=col_names,
    usecols=["Title", "Air date", "IMDB rating", "Production code"],
    index_col="Production code",
    na_values="no_val",
    skiprows=4,
    parse_dates=["Air date"],
    sep="\t",
)

list(simpsons.columns) == ["Title", "Air date", "IMDB rating"]
simpsons.iloc[234, 2] == 6.6
simpsons.shape == (597, 3)
