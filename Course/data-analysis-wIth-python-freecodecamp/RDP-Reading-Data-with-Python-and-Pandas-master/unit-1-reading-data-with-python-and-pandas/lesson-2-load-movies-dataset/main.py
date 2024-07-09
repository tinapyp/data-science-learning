import numpy as np
import pandas as pd
from tests.test_score import test_score
from tests.test_shape import test_shape

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
    "/home/tinapyp/Downloads/FreeCodeCamp-Data Analysis WIth Python/RDP-Reading-Data-with-Python-and-Pandas-master/unit-1-reading-data-with-python-and-pandas/lesson-2-load-movies-dataset/files/movies.csv",
    header=None,
    names=column_names,
    sep="|",
    skiprows=3,
)

movies.loc[:, "imdb_score"].max() == 9
movies.shape == (97, 13)
