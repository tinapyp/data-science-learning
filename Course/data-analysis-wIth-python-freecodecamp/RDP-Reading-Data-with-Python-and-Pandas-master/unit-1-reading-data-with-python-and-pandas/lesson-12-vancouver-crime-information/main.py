import numpy as np
import pandas as pd
import sqlite3

# create a new connection to a db in memory
conn = sqlite3.connect(":memory:")

# create a cursor
c = conn.cursor()

# restore the given van_crime_2003.sql dump
c.executescript(
    open(
        "/home/tinapyp/Downloads/FreeCodeCamp-Data Analysis WIth Python/RDP-Reading-Data-with-Python-and-Pandas-master/unit-1-reading-data-with-python-and-pandas/lesson-12-vancouver-crime-information/files/van_crime_2003.sql",
        "r",
    ).read()
)

query = "SELECT * FROM van_crimes"
# your code goes here
df = pd.read_sql_query(query, con=conn)

late_crimes = df.loc[df["HOUR"] > 18]

dangerous_month_crimes = df.loc[:, "MONTH"].value_counts().head(1)
