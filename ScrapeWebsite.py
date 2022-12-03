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
        self.htmlStorage = {}
        if not os.path.exists(self.outputDir):
            os.makedirs(self.outputDir)
    
    def scrape_country(self, countryName, website):
        print("You wish to scrape COVID-19 data for", countryName, "from", website, "on", self.scrape_date, ".")
        
        if website == "worldometer":
            URL = "https://www.worldometers.info/coronavirus/"
            
            if "worldometer" in self.htmlStorage.keys():
                htmlSoup = self.htmlStorage['worldometer']
            else:
                page = requests.get(URL)
                htmlSoup = BeautifulSoup(page.content, "html.parser")
                self.htmlStorage['worldometer'] = htmlSoup
            
            countriesTable = htmlSoup.find("table", id="main_table_countries_yesterday")
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
            scrape_data['Source'] = website
            
            return scrape_data
        elif website == "who":
            URL = "https://covid19.who.int/table"
            
            if "who" in self.htmlStorage.keys():
                print("HAVE OLD DATA")
                htmlSoup = self.htmlStorage['who']
            else:
                print("GET NEW DATA")
                page = requests.get(URL)
                htmlSoup = BeautifulSoup(page.content, "html.parser")
                self.htmlStorage['who'] = htmlSoup
            
            page = requests.get(URL)
            htmlSoup = BeautifulSoup(page.content, "html.parser")
            
            countriesTable = htmlSoup.find("div", role="rowgroup")
            countryRow = countriesTable.find("div", title=countryName.strip()).parent.parent
            countryCells = countryRow.findAll("div", role="cell")
            
            scrape_data = {}
            scrape_data['Country'] = countryName
            scrape_data['Total Cases'] = countryCells[1].find("div").find("div").find("div").text.strip().replace(",","")
            scrape_data['New Cases'] = round(int(countryCells[2].find("div").text.strip().replace(",","")) / 7, 0)
            scrape_data['Total Deaths'] = countryCells[3].find("div").text.strip().replace(",","")
            scrape_data['New Deaths'] = round(int(countryCells[4].find("div").text.strip().replace(",","")) / 7, 0)
            scrape_data['Active Cases'] = ""
            scrape_data['Critical Cases'] = ""
            scrape_data['Total Cases per 1M Pop'] = ""
            scrape_data['Total Deaths per 1M Pop'] = ""
            scrape_data['Total Tests'] = ""
            scrape_data['Total Tests per 1M Pop'] = ""
            scrape_data['Population'] = ""
            scrape_data['Source'] = website
            
            return scrape_data
            
        
        
        

    
