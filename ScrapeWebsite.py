# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 22:51:19 2022

@author: Skyler Cornaby

This module is used for scraping websites for COVID-19
related data. Data will be scraped both raw and normalized
by population for statistics relating to number of cases
and number of deaths. This data will be scraped from the
web using the BeautifulSoup package, stored in a Pandas
DataFrame, and then exported as a JSON file for use with
other modules for data display.
"""

import datetime
import requests
import os
from bs4 import BeautifulSoup

class ScrapeWebsite:

    def __init__(self):
        today_date = datetime.date.today()
        self.scrape_date = today_date.strftime("%Y%m%d")
        self.outputDir = os.path.dirname(os.path.abspath(__file__)) + '\\Covid_Data'
        if not os.path.exists(self.outputDir):
            os.makedirs(self.outputDir)
    
    def scrape_country(self, countryName, website):
        print("You wish to scrape COVID-19 data for", countryName, "from", website, "on", self.scrape_date, ".")
        
        if website == "worldometer":
            URL = "https://www.worldometers.info/coronavirus/"
            page = requests.get(URL)
            htmlSoup = BeautifulSoup(page.content, "html.parser")
            
            countriesTable = htmlSoup.find("table", id="main_table_countries_today")
            countriesTableBody = countriesTable.find("tbody")
            countryRow = countriesTableBody.find("td", text=countryName).parent
            
            countryCells = countryRow.findAll("td")
            
            scrape_data = {}
            scrape_data['Country'] = countryName
            scrape_data['Total Cases'] = countryCells[2].text.replace(",","")
            scrape_data['New Cases'] = countryCells[3].text.strip("+").strip().replace(",","")
            scrape_data['Total Deaths'] = countryCells[4].text.strip().replace(",","")
            scrape_data['New Deaths'] = countryCells[5].text.strip("+").strip().replace(",","")
            scrape_data['Total Recovered'] = countryCells[6].text.strip().replace(",","")
            scrape_data['New Recovered'] = countryCells[7].text.strip("+").strip().replace(",","")
            scrape_data['Active Cases'] = countryCells[8].text.strip().replace(",","")
            scrape_data['Critical Cases'] = countryCells[9].text.strip().replace(",","")
            scrape_data['Total Cases per 1M Pop'] = countryCells[10].text.strip().replace(",","")
            scrape_data['Total Deaths per 1M Pop'] = countryCells[11].text.strip().replace(",","")
            scrape_data['Total Tests'] = countryCells[12].text.strip().replace(",","")
            scrape_data['Total Tests per 1M Pop'] = countryCells[13].text.strip().replace(",","")
            scrape_data['Population'] = countryCells[14].text.strip().replace(",","")
            
            return scrape_data
            
        
        
        

    
