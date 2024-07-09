import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("data/epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 9))
    plt.scatter(data=df, x="Year", y="CSIRO Adjusted Sea Level")

    # Create first line of best fit
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    plt.plot(
        df["Year"],
        res.intercept + res.slope * df["Year"],
        color="red",
        label="fitted line all data",
    )

    # Create second line of best fit
    recent_data = df.loc[df["Year"] >= 2000]
    years_future = range(2000, 2051)
    res_2000 = linregress(recent_data["Year"], recent_data["CSIRO Adjusted Sea Level"])

    plt.plot(
        years_future,
        res_2000.intercept + res_2000.slope * years_future,
        color="green",
        linestyle="--",
        label="fitted line 2000-2050",
    )

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    # Show plot
    plt.show()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
