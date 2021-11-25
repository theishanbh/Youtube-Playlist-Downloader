from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def linkscraper(yt_link):
    PATH = "chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(yt_link)

    #in driver.get <input> link of the playlist you want to scrape
    sleep(5)

    # page_sections finds the last video link - limited to 100 videos per max scroll by yt
    page_sections = driver.find_elements(By.CSS_SELECTOR,'.style-scope.ytd-item-section-renderer')
    # finds total number of vids to find total number of scrolls
    total_vids = driver.find_element(By.XPATH, '//*[@id="stats"]').text

    sleep(2)

    number = int(total_vids.split()[0])
    # keeps scrolling until end of yt playlist reached
    while (number > 0):
        driver.execute_script("arguments[0].scrollIntoView();", page_sections[-1])
        sleep(2)
        number -= 100

    sleep(2)
    search = driver.find_elements(By.ID,"video-title")

    # f is the txt file where all the links that are to be downloaded are put
    f = open("videolinks.txt", "w")

    # notes down each link in videolinks.txt so that they can be downloaded
    for each in search:
        f.write(each.get_attribute("href").split("&list")[0] + "\n")
    sleep(2)
    driver.close()
