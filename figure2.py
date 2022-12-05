'''
Creator: Arjoneel Dhar
Final Project Figure 2
ISTA 131, Rich Thompson, University of Arizona

Description:
Python program opens a file called housing.csv that holds housing data from the 1990's.
It then proceeds to make a Histogram from the median income for a residential block, which is then grouped into bins.
'''
# Import Statements:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Nonsense Functions:

def get_data():
    df = pd.read_csv('housing.csv')
    # data = df['median_income'].sort_values(ascending=True)
    bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    labels = ['less than 10k', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10', '10-11', '11-12', '12-13', '13-14', '14-15', 'more than 1.5 mil']
    df['bins'] = pd.cut(x = df['median_income'], bins = bins, labels = labels, include_lowest = True,)
    data = df['bins']
    somedict = {}
    for ele in data.values:
        if ele in somedict:
            somedict[ele] = somedict[ele] + 1
        else:
            somedict[ele] = 1
    s = pd.Series(data=somedict, index=somedict.keys())
    return s.reindex(index=['less than 1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10', '10-11', '11-12', '12-13', '13-14', '14-15', 'more than 15'])


def display_figure(data):
    fig = plt.figure(facecolor='#aaeeee')
    ax = fig.add_subplot(facecolor='#ccffff')
    data.plot.bar(
        ax=ax,
        width=0.5,
        rot=0,
    )
    # plt.tick_params(
    #     axis='x',          # changes apply to the x-axis
    #     which='both',      # both major and minor ticks are affected
    #     bottom=False,      # ticks along the bottom edge are off
    #     top=False,         # ticks along the top edge are off
    #     labelbottom=False # labels along the bottom edge are off
    # )
    ax.set_title("Median Incomes of Residential Blocks Surveyed", fontsize=18)
    ax.set_xlabel("Median Income of Block (Numbered in $10k Increments)", fontsize=14)
    ax.set_ylabel("Amount of Blocks", fontsize=14)
    plt.show()

# Main Function:

def main():
    display_figure(get_data())

# That Other Stuff:

if __name__ == "__main__":
    main()