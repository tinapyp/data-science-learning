import numpy as np
import pandas as pd

data_url = (
    "https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx"
)

playstore_df = pd.read_excel(
    data_url,
    usecols=["App", "Rating", "Installs", "Rating", "Genres", "Last_Updated"],
    parse_dates=["Last_Updated"],
)

playstore_df = playstore_df.sort_values(by="Rating", ascending=False).head(25)

playstore_df["Last_Updated"].dtype == np.dtype("<datetime64[ns]")
playstore_df.iloc[1]["App"] == "CDL Practice Test 2018 Edition"
playstore_df.iloc[23]["App"] == "Ulta Beauty"
playstore_df.shape == (25, 5)
