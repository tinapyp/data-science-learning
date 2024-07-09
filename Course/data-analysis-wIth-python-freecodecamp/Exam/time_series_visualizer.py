import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("data/fcc-forum-pageviews.csv", index_col="date")

# Clean data
df = df.loc[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
    fig = df.plot(
        color="red",
        figsize=(20, 9),
        title="Daily freeCodeCamp Forum Page Views 5/206-12/2019",
        ylabel="Page Views",
        xlabel="Date",
    )
    # Save image and return fig (don't change this part)
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df.index = pd.to_datetime(df.index)
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar["year"] = [d.year for d in df_bar.date]
    df_bar["month"] = [d.strftime("%b") for d in df_bar.date]
    df_bar = pd.pivot_table(
        df_bar, values="value", index="year", columns="month", aggfunc="mean"
    )
    # Draw bar plot
    fig = df_bar.plot(kind="bar", ylabel="Average Page Views")
    # Save image and return fig (don't change this part)
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df.index = pd.to_datetime(df.index)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime("%b") for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 9))

    # Year Trend Diagram
    sns.boxplot(data=df_box, x="year", y="value", hue="year", palette="Set1", ax=ax[0])
    ax[0].set_title("Year wise Box Plot (Trend)")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")

    # Month Trend Diagram
    sns.boxplot(data=df_box, x="month", y="value", hue="month", ax=ax[1])
    ax[1].set_title("Month wise Box Plot (Seasonality)")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")

    plt.tight_layout()
    # Save image and return fig (don't change this part)
    fig.savefig("box_plot.png")
    return fig
