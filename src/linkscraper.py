from time import sleep, time
import re
from selenium.webdriver.common import keys

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as soup
import soupsieve



yt_link = f"https://www.youtube.com/playlist?list=PLs8fgrGfxenIv9YudSvj046n_INuldCa2"
def linkscraper(yt_link):
    PATH = "chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(yt_link)

    #in driver.get <input> link of the playlist you want to scrape
    sleep(10)

    # page_sections finds the last video link - limited to 100 videos per max scroll by yt
    page_sections = driver.find_elements_by_css_selector('.style-scope.ytd-item-section-renderer')
    # finds total number of vids to find total number of scrolls
    total_vids = int(driver.find_element_by_xpath('//*[@id="stats"]/yt-formatted-string[1]/span[1]').text)

    sleep(10)

    # keeps scrolling until end of yt playlist reached
    while (total_vids > 0):
        driver.execute_script("arguments[0].scrollIntoView();", page_sections[-1])
        sleep(3)
        total_vids -= 100

    sleep(10)
    search = driver.find_elements_by_id("video-title")

    # f is the txt file where all the links that are to be downloaded are put
    f = open("videolinks.txt", "w")

    # notes down each link in videolinks.txt so that they can be downloaded
    for each in search:
        f.write(each.get_attribute("href").split("&list")[0] + "\n")

    sleep(3)
    driver.close()    

linkscraper(yt_link)

