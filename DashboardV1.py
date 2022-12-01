#Basic Layout to COVID Dashboard 
#Version 1          11.30.2022

# Import Libraries
from bokeh.io import output_file, show
from bokeh.layouts import column, row, layout
from bokeh.plotting import figure
from bokeh.models import Div, CustomJS, DateRangeSlider, Select, Toggle
from datetime import date


output_file("layout.html")

#Place Holder Data
countries = ["USA" , "India", "France", "Germany", "Brazil"]
data = ["Active Cases", "Fatal Cases", "Foo" , "Bar"]
x = list(range(11))
y0 = x


# Interchangable figure with plot in it 
graph = figure(width=750, height=500, background_fill_color="black",x_axis_label = "Date",y_axis_label = "Number")
graph.circle(x, y0, size=12, color="white", alpha=0.8)


#Header used as webpage title Bar
Header = Div(text = """ This is the header title for the webpage""",width=750, height = 50,background = 'white')

#Data slider to select data time range on plot
dateSlider = DateRangeSlider(value=(date(2016, 1, 1), date(2016, 12, 31)),
                                    start=date(2015, 1, 1), end=date(2017, 12, 31))
dateSlider.js_on_change("value", CustomJS(code="""
    console.log('date_range_slider: value=' + this.value, this.toString())
"""))

#Drop down menu widgets
selectCountry1 = Select(title="Select a Country", value="placeHolder1", options=countries)
selectCountry2 = Select(title="Select a Country to compare", value="placeHolder2", options=countries)
selectData = Select(title="Select data", value="placeHolder3", options=data)

#Toggle Widget to plot multiple data on single plot
compareToggle = Toggle(label="Compare with another country",button_type="success")

#HTML Layout
interactions = column(selectCountry1,selectData,dateSlider,compareToggle,selectCountry2)
interactions.sizing_mode = "stretch_both"
Layout = layout([
    [Header],
    [interactions,graph],
])

#Displays Webpage
show(Layout)