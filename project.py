from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver_win32/chromedriver.exe")
browser.get(START_URL)
stars_data = []

headers = ["Name", "Distance", "Mass", "Radius"]

def scrape():
    
        time.sleep(2)

        soup = BeautifulSoup(browser.page_source, "html.parser")

        for tr_tag in soup.find_all("tr"):
            td_tags = tr_tag.find_all("td")
            temp_list = []
            for index, td_tag in enumerate(td_tags):
               if index == 1:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
               else:
                        temp_list.append("")
               if index == 3:
                     temp_list.append(td_tag.contents[0])
               else:
                        temp_list.append("")
               if index == 5:
                     temp_list.append(td_tag.contents[0])
               else:
                        temp_list.append("")
               if index == 6:
                     temp_list.append(td_tag.contents[0])
               else:
                        temp_list.append("")
            # Get Hyperlink Tag
          
            
            stars_data.append(temp_list)

       

        print(f"Page scraping completed")
with open("scrapper.csv", "w") as f:
     csvwriter = csv.writer(f)
     csvwriter.writerow(headers)
     csvwriter.writerows(stars_data)

# Calling Method
scrape()
