#Basic Layout to COVID Dashboard 
#Version 1          11.30.2022

# Import Libraries
from bokeh.layouts import column, layout
from bokeh.plotting import figure, curdoc
from bokeh.models import Div, Select, Button, Plot, ColumnDataSource
from datetime import date
import pandas as pd 

#Global Variables for Graph 
selectedCountry1 = ""
selectedCountry2 = ""
selectedData = "Active Cases"
rowValue1 = 0
rowValue2 = 0

#Drop Down Menu Data
with open("Countries.txt") as file:
    countriesDropList = []
    for line in file:
        line = line.strip()
        countriesDropList.append(line)

data = ["Active Cases", "Critical Cases", "New Cases" , "New Deaths","New Recovered","Population",
"Total Cases","Cases per 1M people","Total Deaths","Deaths per 1M people","Total Recovered","Total Test","Tests per 1M People"]
dateDropDown = ['20221127', '20221128', '20221129', '20221130', '20221201', '20221203', '20221204',
                '20221205', '20221206', '20221207', '20221208', '20221209']

# Import Data
filepath = '20221208.xlsx'
covidData = pd.read_excel(filepath)
covidData.drop(['Critical Cases'], axis=1)
covidData.drop(['New Cases'], axis=1)
covidData.drop(['New Deaths'], axis=1)
covidData.drop(['New Recovered'], axis=1)
countries = list(covidData['Country'])
countriesPlaceHolder = ['']
yPlaceHolder = [0]
data_dict = {'x':countriesPlaceHolder,'y':yPlaceHolder}
source_table_hist = ColumnDataSource(data=data_dict)

# Interchangable figure with plot in it 
graph = figure(width=400, height=500, background_fill_color="black",x_axis_label = "Country",
y_axis_label = "Number",x_range=countries)
#graph.y_range = Range1d(0,10)
graph.background_fill_color = "black"
graph.border_fill_color = 'white'
graph.outline_line_color = 'white'
graph.circle(size = 1, color = 'white', alpha = 0.8,source=source_table_hist)


def countryDropHandler(attr,old,new):
    global selectedCountry1, rowValue1
    selectedCountry1 = new
    j = 0
    for i in countries:
        if i == new:
            break
        else:
            j = j + 1
    rowValue1 = j
    

def dataDropHandler(attr,old,new):
    global selectedData
    selectedData = new
    

def dateDropHandler(attr,old,new):
    global filepath,covidData

    filepath= new + ".xlsx"
    covidData = pd.read_excel(str(filepath))

    print(filepath)

def countryCompareDropHandler(attr,old,new):
    global selectedCountry2, rowValue2
    selectedCountry2 = new
    j = 0
    for i in countries:
        if i == new:
            break
        else:
            j = j + 1
    rowValue2 = j 


def plotButtonHandler():
    global selectCountry1,selectCountry2,rowValue1,rowValue2,selectedData
    graph.renderers = []

    # Create plotting variables
    data = [selectedCountry1, selectedCountry2]
    y0 = [covidData.at[rowValue1,selectedData], covidData.at[rowValue2,selectedData]]   
   
    data_dict = {'x':data,'y':y0}
    graph.x_range.factors=data_dict['x']
    source_table_hist.data=data_dict
    # Interchangable figure with plot in it 
    print(data,y0)
    graph.left[0].formatter.use_scientific = False
    #graph.x_range=data
    graph.circle(data,y0,size = 30)
    
    
 # Total Covid Cases
def totalWorldCases(covidData):
  "Sums the data in the Total Cases column to calculate the total historic worldwide cases"

  totalCasesList = covidData['Total Cases'].values.tolist()

  total = sum(totalCasesList)

  return total


totalCases = totalWorldCases(covidData)
#print('The total number of worldwide cases is:', totalCases)



# Total ACTIVE Covid Cases
def totalActiveWorldCases(covidData):
  "Sums the data in the Active Cases column to calculate the total current worldwide cases"

  totalActiveCasesList = covidData['Active Cases']

  total = sum(totalActiveCasesList)

  return total


totalActive = totalActiveWorldCases(covidData)
#print('The current number of active cases is:', totalActive)

# Top 5 Countries vs Total Cases (per 1M Population)
def mostInfectious(covidData):
    global mostX,mostY
    "Determines the five most infected countries by case count per 1M population"

    # Determine the most infected countries
    mostInfectedDF = covidData.nlargest(5, 'Total Cases per 1M Pop')

    # Data to be plotted
    mostX = mostInfectedDF['Country'].values.tolist()
    mostY = mostInfectedDF['Total Cases per 1M Pop'].values.tolist()

    #print(x,y)

mostInfectious(covidData)
graph2 = figure(title = 'Top 5 Most Infectious Countries',x_range=mostX,width=325,height=325)
graph2.vbar(x= mostX, top = mostY, width=0.5)


#Headers used as webpage title Bar
Header = Div(text = """ COVID Dashboard """,width=200, height = 50,background = 'white')
totalCasesText = Div(text = str(totalCases), width=200, height = 50,background = 'white')
currentCasesText = Div(text = str(totalActive), width=200, height = 50,background = 'white')

#Drop down menu widgets
selectCountry1 = Select(title="Select a Country", value="placeHolder1", options=countriesDropList)
selectCountry1.on_change("value",countryDropHandler)
selectCountry2 = Select(title="Select a Second Country", value="placeHolder2", options=countriesDropList)
selectCountry2.on_change("value",countryCompareDropHandler)
selectData = Select(title="Select data", value="placeHolder3", options=data)
selectData.on_change("value",dataDropHandler)
selectDate = Select(title="Select date", value="placeHolder4", options= dateDropDown)
selectDate.on_change("value",dateDropHandler)


# add a button widget and configure with the call back
plotButton = Button(label="Plot")
plotButton.on_event('button_click', plotButtonHandler)

#HTML Layout
interactions = column(selectCountry1,selectData,selectDate,selectCountry2,plotButton)
interactions.sizing_mode = "stretch_both"
Layout = layout([
    [Header,totalCasesText,currentCasesText],
    [interactions,graph,graph2],
])



#Displays Webpage
curdoc().add_root(Layout)