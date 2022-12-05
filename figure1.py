'''
Creator: Arjoneel Dhar
Final Project Figure 1
ISTA 131, Rich Thompson, University of Arizona

Description:
Python program opens a file called housing.csv that holds housing data from the 1990's.
It then proceeds to make a Histogram from a slice of the data (taken from column of data frame) 
that shows the median age of the housing blocks surveyed in the data set.
'''
# Import Statements:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Nonsense Functions:

def get_data():
    df = pd.read_csv('housing.csv')
    data = df['housing_median_age'].sort_values(ascending=True).astype(int)
    somedict = {}
    for ele in data.values:
        if ele in somedict:
            somedict[ele] = somedict[ele] + 1
        else:
            somedict[ele] = 1
    indexarr = []
    for i in range(52):
        indexarr.append(i+1)
    return pd.Series(data=somedict, index=indexarr)

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
    ax.set_title("Amount of Houses by Age within Data Set", fontsize=18)
    ax.set_xlabel("Age of Houses (In Years)", fontsize=14)
    ax.set_ylabel("Amount of Houses Per Age", fontsize=14)
    plt.show()

# Main Function:

def main():
    display_figure(get_data())

# That Other Stuff:

if __name__ == "__main__":
    main()