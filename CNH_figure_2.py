"""
Author: Chase N. Hult
ISTA 131 Final Project
This makes a bar graph showing the prices of housing given longitudinal
  proximity to major cities.
This file is for the final project of ISTA 131
"""

import matplotlib.pyplot as plt
import pandas as pd


def get_data():
    """Return a Series comparing median house value to total rooms"""
    df = pd.read_csv('housing.csv')
    # This data is censored, so we need to take out unrecorded data
    df = df[df['median_house_value'] != 500_001]
    df['bins'] = pd.cut(df['longitude'], 100)
    s = df.groupby('bins').mean(numeric_only=True)['median_house_value'] / 1000
    s.index = s.index.map(lambda i: i.left)
    return s


def make_figure(data):
    """Make a very pretty figure with the data from get_data"""
    fig = plt.figure(facecolor='#cccccc')
    ax = fig.add_subplot(facecolor='#eeeeee')
    plt.bar(x=data.index, height=data.values, width=0.101, color='#444444')
    plt.axvline(x=-118.243683, color="orange", label="LA")
    plt.axvline(x=-122.431297, color="blue", label="San Francisco")
    plt.axvline(x=-117.161087, color="purple", label="San Diego")
    plt.legend(loc='upper right')
    ax.set_title("Mean House Value vs. Longitude", fontsize=18)
    ax.set_xlabel("Longitude", fontsize=14)
    ax.set_ylabel("Mean House Value (k$)", fontsize=14)
    plt.show()


def main():
    data = get_data()
    make_figure(data)


if __name__ == "__main__":
    main()
