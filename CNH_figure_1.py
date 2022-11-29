"""
Author: Chase N. Hult
ISTA 131 Final Project
This makes a bar graph correlating housing value to proximity to the ocean
This file is for the final project of ISTA 131
"""

import matplotlib.pyplot as plt
import pandas as pd

ORDER = ['ISLAND', 'NEAR BAY', 'NEAR OCEAN', '<1H OCEAN', 'INLAND']


def get_data():
    """Return a Series of the means of each ocean proximity value"""
    df = pd.read_csv('housing.csv')
    data = df.groupby('ocean_proximity').mean()['median_house_value']
    data /= 1000
    return data.sort_index(key=lambda idx: idx.map(lambda x: ORDER.index(x)))


def make_figure(data):
    """Make a very pretty figure with the data from get_data"""
    fig = plt.figure(facecolor='#aaeeee')
    ax = fig.add_subplot(facecolor='#ccffff')
    data.plot.bar(
        ax=ax,
        color=['#22ddbb', '#2299dd', '#2233dd', '#44aa77', '#aa9944'],
        rot=0,
    )
    ax.set_title("Mean House Value vs. Distance from Water", fontsize=18)
    ax.set_xlabel("Distance from Water", fontsize=14)
    # We can call this the mean because we're working with
    #   the mean of a LOT of medians
    ax.set_ylabel("Mean House Value (k$)", fontsize=14)
    plt.show()


def main():
    data = get_data()
    make_figure(data)


if __name__ == "__main__":
    main()
