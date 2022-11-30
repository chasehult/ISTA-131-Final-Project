'''
Amad Arshad
Final Project
Rich Thompson
ISTA 131
'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_data():
    df = pd.read_csv('housing.csv')
    return df

def fig1(df):
    x = df['longitude'].tolist()
    y = df['latitude'].tolist()
    img = plt.imread("California-Satellite-Map.jpeg")
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('xkcd:light blue grey')
    ax.imshow(img, extent=[-125.8, -113, 32.45, 42])
    ax.scatter(x, y, s = 10, color = 'red', facecolor = 'green')
    plt.xlabel('Longitude', fontsize =12.5)
    plt.ylabel('Latitude', fontsize = 12.5)
    plt.title('Position of households based on longitude and latitude', fontsize = 13, fontweight = 'bold')
    plt.show()

    



def fig2(data):
    x = data['population'].tolist()
    y = data['households'].tolist()
    x = np.array(x)
    y = np.array(y)
    plt.figure(facecolor='palegreen')
    plt.scatter(x,y)
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*x+b, color = 'red')
    plt.xlabel('Population', fontsize = 12.5)
    plt.ylabel('Households', fontsize = 12.5)
    l = []
    for i in range(10):
        l.append(i*4000)
    plt.xticks(l)
    equation = 'y = ' + str(round(m,3))+'x+'+str(round(b,3))

    plt.text(19000, 10000, equation, fontsize = 12)
    plt.text(0, 8500, 'For every 100 people there are approximately 31 households', fontsize = 8)
    plt.title('Relationship between population and number of households', fontsize = 13, fontweight = 'bold')
    plt.show()


def fig3(data):
    x = data['ocean_proximity'].tolist()
    y = data['households'].tolist()
    plt.figure(facecolor='darkturquoise')
    plt.bar(x,y, color ='slategray')
    plt.xlabel('Proximity from ocean', fontsize = 13)
    plt.ylabel('Households', fontsize = 13)
    plt.title('Number of households based on proximity to ocean', fontsize = 15, fontweight = 'bold')
    plt.show()

def main():
    data = get_data()
    fig1(data)
    fig2(data)
    fig3(data)

if __name__ == "__main__":
    main()

