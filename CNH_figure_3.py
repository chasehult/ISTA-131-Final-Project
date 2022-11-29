"""
Author: Chase N. Hult
ISTA 131 Final Project
This makes a scatter plot to figure out how many California rooms are bedrooms
This file is for the final project of ISTA 131
"""

import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm


def get_data():
    """Return a Series comparing median house value to total rooms"""
    df = pd.read_csv('housing.csv')
    # This data is censored, so we need to take out unrecorded data
    df = df[df['total_bedrooms'].notna()]
    return pd.Series(df['total_bedrooms'].values, df['total_rooms'])


def get_ols_parameters(data):
    """Get the ols parameters from a series"""
    x = data.index.values
    X = sm.add_constant(x)
    model = sm.OLS(data, X)
    results = model.fit()
    return results.params['x1'], results.params['const'], results.rsquared, results.pvalues['x1']


def make_figure(data, m, b):
    """Make a very pretty figure with the data from get_data"""
    fig = plt.figure(facecolor='#ff88ee')
    ax = fig.add_subplot(facecolor='#eeccee')
    data.plot(style='m.')
    plt.plot(data.index, m * data.index + b, color='tab:pink', label=f"{m:.4f}x + {b:.4f}")
    plt.legend(loc='upper right')
    ax.set_title("Rooms vs. Bedrooms", fontsize=18)
    ax.set_xlabel("# of Rooms per Block", fontsize=14)
    ax.set_ylabel("# of Bedrooms per Block", fontsize=14)
    ax.annotate(f'{m*100:.2f}% of rooms are bedrooms in California', xy=(-500, 6950))
    plt.tight_layout()
    plt.show()


def main():
    data = get_data()
    m, b, *_ = get_ols_parameters(data)
    make_figure(data, m, b)


if __name__ == "__main__":
    main()
