import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def sea_level_predictor():
    # Load the dataset
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create a scatter plot using Year as the x-axis and CSIRO Adjusted Sea Level as the y-axis
    fig, ax = plt.subplots()  # Create the figure and axis for plotting
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Fit a line of best fit for all data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Generate predictions for the years 1880 to 2050
    years_extended = range(1880, 2051)
    sea_level_extended = [slope * year + intercept for year in years_extended]
    
    # Plot the first line of best fit (for all data)
    ax.plot(years_extended, sea_level_extended, label='Best Fit Line')
    
    # Filter data for years 2000 onward
    df_recent = df[df['Year'] >= 2000]
    
    # Fit a line of best fit for data from 2000 onward
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Generate predictions for the years 2000 to 2050
    years_recent = range(2000, 2051)
    sea_level_extended_recent = [slope_recent * year + intercept_recent for year in years_recent]
    
    # Plot the second line of best fit (from 2000 onward)
    ax.plot(years_recent, sea_level_extended_recent, label='Best Fit Line (2000 Onward)', color='orange')
    
    # Add labels and title
    ax.set_xlabel('Year')  # Set x-axis label
    ax.set_ylabel('Sea Level (inches)')  # Set y-axis label
    ax.set_title('Rise in Sea Level')
    
    # Add a legend
    ax.legend()
    
    # Save the plot as an image
    plt.savefig('sea_level_predictor.png')
    
    # Return the axis object for testing purposes
    return ax  # Return the axis to use in tests

def draw_plot():
    ax = sea_level_predictor() 
    return ax  # Ensure that draw_plot returns the axis object
