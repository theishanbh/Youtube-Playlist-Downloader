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

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(f"https://www.youtube.com/playlist?list=PLs8fgrGfxenIv9YudSvj046n_INuldCa2")

# page_sections finds the last video link - limited to 100 videos per max scroll by yt
page_sections = driver.find_elements_by_css_selector('.style-scope.ytd-item-section-renderer')
# finds total number of vids to find total number of scrolls
total_vids = int(driver.find_element_by_xpath('//*[@id="stats"]/yt-formatted-string[1]/span[1]').text)



