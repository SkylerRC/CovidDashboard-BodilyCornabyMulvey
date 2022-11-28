# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 23:28:40 2022

@author: skyle
"""

import ScrapeWebsite
import pandas as pd
import os
import datetime

scraper = ScrapeWebsite.ScrapeWebsite()
currentDate = datetime.date.today()
currentDate = currentDate.strftime("%Y%m%d")
currentDir = os.path.dirname(os.path.abspath(__file__))
outputDir = currentDir + '\\Covid_Data'
excelPath = outputDir + '\\' + currentDate + '.xlsx'
jsonPath = outputDir + '\\' + currentDate+ '.json'


covid_df = pd.DataFrame()


with open("scrapecountries.txt") as inputFile:
    lines = inputFile.readlines()

inputFile.close()
countriesToScrape = []

for line in lines:
    
    try:
        d = {}
        print(line.strip())
        d = scraper.scrape_country(line.strip(), "worldometer")
        #print(d)
        covid_df = covid_df.append(d, ignore_index=True)
    except:
        print("We had an issue gathering data on", line.strip(), "from", "worldometer")

covid_df.to_excel(excelPath, encoding = 'utf-8', index=False)
covid_df.to_json(jsonPath)
print(covid_df)