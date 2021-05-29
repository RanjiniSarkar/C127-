from selenium import webdriver
from bs4 import BeautifulSoup 
import time
import csv

starturl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("C:/Users/AILN-Pun3/Desktop/127")
browser.get(starturl)
time.sleep(10)
def script ():
    headers = ["name","lightyears","planetmass","stellarmagnitude","Discoverydate"]
    planet_data = [ ]
    for i in range (0,438):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul",attrs= {"class":"exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index,li_tag in enumerate(li_tags):
                if index == 0:
                  temp_list.append(li_tag.find_all("a")[0].contents[0])
               
                else: 
                    try:
                        temp_list.append(li_tags.contenst[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click
    with open("planets_data.csv", "w")as f :
        csvwritter = csv.writer(f)
        csvwritter.writerow(headers)
        csvwritter.writerows(planet_data)
script()
                
            


