# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 22:54:54 2023

@author: anish
"""

# Importing the required packages
import pandas as pd
import matplotlib.pyplot as plt


def linePlot(df, x_axis, y_axis):
    '''
    It is a function to create a lineplot using the dataframe and given axes.
    Here we take the data from the dataframe respective to the x_axis and
    y_axis values and plot the line graph between the Age and the Resting Blood
    Pressure (in mm Hg) with respective to Male and Female.
    '''
    # Grouping the data with respective sex (Male and Female) and trestbps
    grouped_male = df[df['sex'] == 1].groupby(x_axis)[y_axis].mean() \
        .reset_index()
    grouped_female = df[df['sex'] == 0].groupby(x_axis)[y_axis].mean() \
        .reset_index()

    # Intialization of the figure with figsize
    plt.figure(figsize=(9, 6))

    # Calling the plot function to plot lineplot for the given values
    plt.plot(grouped_male[x_axis], grouped_male[y_axis],
             label="Male")
    plt.plot(grouped_female[x_axis], grouped_female[y_axis],
             label="Female")

    # Plotting a straight horizontal line for a given y value
    plt.axhline(y=130, color='red', linestyle='-',
                label='High blood pressure(>= 130)')

    # Define the title for the plot
    plt.title("Blood Pressure variation with Age")

    # Labelling the axes
    plt.xlabel("Age")
    plt.ylabel("Resting Blood Pressure (in mm Hg)")

    # Removing Empty white space around the graph using min and max functions
    plt.xlim(df["age"].min(), df["age"].max())

    # To display legend
    plt.legend()

    # To display the grids in the plot
    plt.grid()

    # Save figure as png
    plt.savefig("lineplot.png")

    # To display the plot
    plt.show()


def barPlot(df, x_axis, y_axis):
    '''
    It is a function to create a barplot using the dataframe and given axes.
    Here we take the data from the dataframe respective to the x_axis and
    y_axis values and plot the bar graph between the Chest pain type and the
    disease Frequency with respective to Positive and Negative Heart Disease.
    '''

    # Intialization of the figure with figsize
    plt.figure()

    # Create a crosstab with 'Chest Pain Type' as the index and 'Frequency of
    # Disease' as the columns
    cross_tab = pd.crosstab(df[x_axis].replace({0: 'Typical angina',
                                                1: 'Atypical angina',
                                                2: 'Non-anginal pain',
                                                3: 'Asymptomatic'}),
                            df[y_axis])

    # Calling the plot function to plot bar graph
    cross_tab.plot(kind='bar', figsize=(9, 6))

    # Define the title for the plot
    plt.title("Heart Disease Frequency per Chest Pain Type")

    # Labelling the axes
    plt.xlabel("Chest Pain Type")
    plt.ylabel("Disease Frequency")

    # To display legend
    plt.legend(["Negative", "Positive"])

    # To set the current tick locations and labels of the x-axis
    plt.xticks(rotation=0)

    # Save figure as png
    plt.savefig("barplot.png")

    # To display the plot
    plt.show()


def pieChart(df, col_name):
    '''
    It is a function to create a pieplot using the dataframe and given column
    name. Here we get the data from the dataframe using the column name and
    plot the pie plot.
    '''

    # Intialization of the figure with figsize
    plt.figure(figsize=(9, 6))

    # Intialization of the data
    data = df[col_name].replace({0: 'Normal', 1: 'ST-T Wave Abnormality',
                                 2: 'Left Ventricular Hypertrophy'})
    labels = data.unique()
    sizes = data.value_counts()

    # Calling the plot function to plot bar graph
    plt.pie(sizes, autopct='%1.1f%%', radius=0.6)

    # Customize the title
    plt.title("Resting Electrocardiographic Measurement of patients")

    # Add a legend
    plt.legend(labels)

    # Equal aspect ratio ensures that the pie chart is circular
    plt.axis('equal')

    # Save figure as png
    plt.savefig("pieplot.png")

    # To display the plot
    plt.show()


def main():
    # Creating a dataframe using pandas from CSV file
    df = pd.read_csv(r"heart-disease.csv")

    # Calling lineplot function with dataframe, x_axis and y_axis values
    linePlot(df, 'age', 'trestbps')

    # Calling barplot function with dataframe, x_axis and y_axis values
    barPlot(df, 'cp', 'target')

    # Calling pieplot function with dataframe and column name as 'restecg'
    pieChart(df, "restecg")


if __name__ == "__main__":
    # Start of the program from here by calling main()
    main()
