# This script stores all the individual functions required to plot the data gathered in ScrapeWebsite.py.
# It loads the relevant excel file, cleans it up slightly, and then has a multitude of functions to create
# different types of plots.

# Last updated: 2022 - 11 - 30
# ----------------------------------------------------------------------------------------------------

# Import Libraries, Modules, etc.
import pandas as pd
import openpyxl
from bokey.plotting import figure, output_file, show

# ----------------------------------------------------------------------------------------------------

# Import the Excel Data File and save it as 'covidData'
def importData(scrapeName = '20221127'):
  "scrapeName should be a string, with the name of the excel file created during the website scrape"
  
  # Combine the scrapeName with .xlsx into one string
  excelFileName = scrapeName + '.xlsx'
  
  # Load the excel data
  covidData = pd.read_excel(excelFileName, header=0, index_col=None)
  
  # For reference, the columns of the data frame are as follows:
  # Active Cases, Country, Critical Cases, New Cases, New Deaths, New Recovered, Population, Total Cases.....
  # .... Total Cases per 1M, Total Deaths, Total Deaths per 1M, Total Recovered, Total Tests, Total Tests per 1M

# ----------------------------------------------------------------------------------------------------

# Eliminate Columns that we will not be using
# Note: This is optional, and can be commented out if we end up wanting to use this data.
covidData.drop(['Critical Cases'], axis=1)
covidData.drop(['New Cases'], axis=1)
covidData.drop(['New Deaths'], axis=1)
covidData.drop(['New Recovered'], axis=1)

# ----------------------------------------------------------------------------------------------------

# Total Covid Cases
def totalWorldCases(covidData):
  "Sums the data in the Total Cases column to calculate the total historic worldwide cases"
  
  totalCases = covidData.sum(covidData['Total Cases'])
  
  return totalCases


# Total ACTIVE Covid Cases
def totalActiveWorldCases(covidData):
  "Sums the data in the Active Cases column to calculate the total current worldwide cases"
  
  totalActiveCases = covidData.sum(covidData['Active Cases'])
  
  return totalActiveCases


# Top 5 Countries vs Total Cases per 1M Population
def mostInfectious(covidData):
  "Determines the five most infected countries by case count per 1M population"
  
  # Determine the most infected countries
  mostInfectedDF = covidData.nlargest(5, 'Total Cases per 1M Pop')
  
  # Initialize a bar plot to visually see the difference
  graph = figure(title = "Top 5 Infected Countries (Per 1M Persons)")
  graph.xaxis.axis_label = "Countries"
  graph.yaxis.axis_label = "Case Count per 1M Persons"
  
  # Data to be plotted
  x = mostInfectedDF['Country']
  y = mostInfectedDF['Total Cases per 1M Pop']
  
  # Plot the graph
  graph.vbar(x, top = y, width = 0.5)                          # The width, color, orientation, etc. can all be changed.
  show(graph)                                                  # We will likely need to change where this outputs
  
  
  
  
 # Other plots go here!
  
  



