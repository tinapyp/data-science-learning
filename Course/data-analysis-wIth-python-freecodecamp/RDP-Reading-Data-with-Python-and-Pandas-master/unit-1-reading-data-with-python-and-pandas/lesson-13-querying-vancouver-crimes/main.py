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
        "/home/tinapyp/Downloads/FreeCodeCamp-Data Analysis WIth Python/RDP-Reading-Data-with-Python-and-Pandas-master/unit-1-reading-data-with-python-and-pandas/lesson-13-querying-vancouver-crimes/files/van_crime_2003.sql",
        "r",
    ).read()
)

# your code goes here
query = """
SELECT *
FROM van_crimes
-- WHERE NEIGHBOURHOOD IN ('Stanley Park', 'West End')
"""
van_crimes_df = pd.read_sql_query(query, conn)

crime_types_count = van_crimes_df.loc[:, "TYPE"].value_counts()
