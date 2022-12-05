'''
Creator: Arjoneel Dhar
Final Project Figure 3
ISTA 131, Rich Thompson, University of Arizona

Description:
Python program opens a file called housing.csv that holds housing data from the 1990's.
It then proceeds to make a Scatterplot of the median income for a housing block and the
median value for their property.

Notes:
An extra special thanks is due to chase who explained to me his scatter plot code and 
explained the thought pattern in order to make my own scatter plot.
'''

# Import Statements:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Nonsense Functions

def get_data():
    df = pd.read_csv('housing.csv')
    return pd.Series(data=df['median_house_value'].values, index=df['median_income'])


def get_ols_parameters(data):
    """Get the ols parameters from a series"""
    x = data.index.values
    X = sm.add_constant(x)
    model = sm.OLS(data, X)
    results = model.fit()
    return results.params['x1'], results.params['const'], results.rsquared, results.pvalues['x1']


def make_figure(data, m, b):
    """Make a very pretty figure with the data from get_data"""
    fig = plt.figure(facecolor='#aaeeee')
    ax = fig.add_subplot(facecolor='#ccffff')
    data.plot(style='m.', label='Median Income and Associated Value of House')
    plt.plot(data.index, m * data.index + b, color='tab:red', label=f"{m:.4f}x + {b:.4f}")
    plt.legend(loc='upper right')
    ax.set_title('Median Income Vs. Median Housing Value (per Block)', fontsize=18)
    ax.set_xlabel('Incomes (Scaled down by factor of $10k)', fontsize=14)
    ax.set_ylabel('Values of Houses', fontsize=14)
    ax.annotate(f'{m*100:.2f}% of rooms are bedrooms in California', xy=(-500, 6950))
    plt.tight_layout()
    plt.show()

# Main Function

def main():
    data = get_data()
    m, b, *_ = get_ols_parameters(data)
    make_figure(data, m, b)

# That Other Stuff:

if __name__ == "__main__":
    main()
