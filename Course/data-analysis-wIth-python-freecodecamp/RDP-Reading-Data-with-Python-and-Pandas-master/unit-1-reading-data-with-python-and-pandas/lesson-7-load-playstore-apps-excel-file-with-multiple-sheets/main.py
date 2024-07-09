import numpy as np
import pandas as pd

data_url = (
    "https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx"
)

playstore_df = pd.read_excel(data_url, index_col=[0], sheet_name="Google_playstore")
content_id_df = pd.read_excel(data_url, index_col="Content_ID", sheet_name="Content_ID")


## Test Case
content_id_df.shape == (250, 1)

content_id_head = pd.DataFrame(
    {"Content_Rating": ["Everyone", "Everyone", "Everyone", "Teen", "Everyone"]},
    index=[101, 101, 101, 102, 101],
)

content_id_df.head().equals(content_id_head)

playstore_df.shape == (250, 9)

playstore_df.iloc[3]["App"] == "Sketch - Draw & Paint"
