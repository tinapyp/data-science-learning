import numpy as np
import pandas as pd

column_names = [
    "color",
    "director_name",
    "num_critic_for_reviews",
    "duration",
    "gross",
    "movie_title",
    "num_user_for_reviews",
    "country",
    "cotent_rating",
    "budget",
    "title_year",
    "imdb_score",
    "genre",
]

movies = pd.read_csv(
    "/home/tinapyp/Downloads/FreeCodeCamp-Data Analysis WIth Python/RDP-Reading-Data-with-Python-and-Pandas-master/unit-1-reading-data-with-python-and-pandas/lesson-3-advanced-parsing-on-movies-dataset/files/movies.csv",
    header=None,
    names=column_names,
    na_values="?",
    thousands=",",
    sep="|",
    dtype={"budget": float},
    index_col="movie_title",
)

movies.loc[:, "budget"].min() == 105000000.0
"?" not in movies.country.unique()
movies.shape == (100, 12)
