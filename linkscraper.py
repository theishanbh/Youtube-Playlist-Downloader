from time import sleep
import re
from selenium.webdriver.common import keys

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as soup
import soupsieve

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(f"https://www.youtube.com/playlist?list=PLs8fgrGfxenIv9YudSvj046n_INuldCa2")
#in driver.get <input> link of the playlist you want to scrape


sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
search = driver.find_elements_by_id("video-title")

f = open("videolinks.txt", "w")
# f is the txt file where all the links that are to be downloaded are put
for each in search:
    f.write(each.get_attribute("href").split("&list")[0] + "\n")
    print("hello")
sleep(3)

driver.close()


