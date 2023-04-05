# -*- coding: utf-8 -*-

"""

@author: Kashir Waseem
 Assignment-2 Stats and trends
Student id : 22031825
Course : Applied Data Science 1 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def read_data(filename):
    """
    This function read the dataset from the 
    filename and manipulate, transpose the dataset
    and then return two dataset one is column as country name
    and the other one is column as years
    """
    # read the data 
    df = pd.read_csv(filename)
    # drop that column which is not in use
    df.drop(['Indicator Name', 'Indicator Code',"Country Code"]
            , axis=1, inplace=True)
    # clean the dataset by dropping the NA values
    df.dropna(inplace=True)
    # Transpose the dataframe
    df_y = df.T
    # set the columns in transpose dataset
    df_y.columns = df_y.iloc[0]
    # deleting duplicate rows in the dataset
    df_y = df_y.iloc[1:]
    # set the column name Year
    df_y.columns.name = "Year"
    #set index of column by country name
    df = df.set_index("Country Name")
    
    return df, df_y

def get_summary_stats(df, indicator_name):
    """
    get the filename and indicator name in the
    parameter and evaluate the stastic then show the 
    summary statistic result of the dataset
    """
    # list of countries in which we perform summary dataset
    countries = ['United States', 'China', 'India', 'Russia', 'Brazil'
                 , 'Japan', 'Germany', 'South Africa']
    # filter the dataset by by the countries list which we provide
    df_countries = df[df.index.isin(countries)]
    # Compute the summary statistics
    summary_stats = df_countries['2010'].describe()
    
    # Print the results
    print(f'Summary statistics for {indicator_name} at year 2010:')
    print(summary_stats)

def create_bar_chart(df):
    """
    Creates a bar chart for the
    selected countries on different years
    
    """
    # list of countries
    countries = ['United States', 'China', 'India', 'Brazil'
                 , 'Japan', 'Germany', 'South Africa']
    # list for the years
    years = ["1990", "1995", "2000", "2005", "2010", "2015"]
    # Filter the dataframe to include only the selected countries and years
    df_plot = df.loc[countries, years]
    # defining the variable for plot the figure
    fig = plt.figure(figsize=(50, 25))
    # set the axes for the plot 
    ax = fig.add_axes([0,0,1,1])
    #set the width
    width = 0.1
    # Create a bar chart for each country
    for i,year in enumerate(years):
        x = np.arange(len(countries))
        #plot the bar chart for each country
        ax.bar(x + (i - 2.5) * width, df_plot[year], label=year, width=width)

    # Set the x and y axis labels and the title
    plt.xlabel('Country')
    plt.ylabel('CO2 Emissions (metric tons per capita)')
    plt.title('CO2 Emissions by Country and Year')
    
    # Set the x-tick labels to the country names
    ax.set_xticks(x)
    ax.set_xticklabels(countries)
    
    # Show the legend
    plt.legend()
    
    # Display the plot
    plt.show()
    
    
if __name__=="__main__":
    # getting file name for the co emission
    co_emission = 'co_emission.csv'
    #calling the function for read and  manipulate and transpose the dataset
    dataset_by_country, dataset_by_year = read_data(co_emission)
    #calling function for the summary stats function of the co 2 emission
    get_summary_stats(dataset_by_country, "Co 2 emission")
    # calling the function for the plot of bar plot
    create_bar_chart(dataset_by_country)




