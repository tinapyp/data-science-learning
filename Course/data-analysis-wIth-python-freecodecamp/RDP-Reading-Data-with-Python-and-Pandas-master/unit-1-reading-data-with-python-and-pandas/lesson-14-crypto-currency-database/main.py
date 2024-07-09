import numpy as np
import pandas as pd
import sqlite3

# create a new connection to a db in memory
conn = sqlite3.connect(":memory:")

# create a cursor
c = conn.cursor()

# restore the given cryptos.sql dump
c.executescript(
    open(
        "/home/tinapyp/Downloads/FreeCodeCamp-Data Analysis WIth Python/RDP-Reading-Data-with-Python-and-Pandas-master/unit-1-reading-data-with-python-and-pandas/lesson-14-crypto-currency-database/files/cryptos.sql",
        "r",
    ).read()
)

# your code goes here
query = """
SELECT  cc.name AS coin_name, 
        ce.name AS exchange, 
        symbol, 
        price_usd, 
        percent_change_7d
FROM cryptocoins_cryptocurrency cc
    LEFT JOIN cryptocoins_exchange ce ON cc.exchange_id = ce.id
"""

crypto_df = pd.read_sql(query, conn)

weekly_change_df = crypto_df.sort_values(by="percent_change_7d", ascending=False)
