from flask import Flask, render_template
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
class selBs4: 
        def __init__(self, bc, hURL):
                self.bc = bc
                self.hURL = hURL
        
        def  returnsoup(self):
            PATH = "C:\Program Files (x86)\chromedriver.exe" 
            chrome_options = Options()
            ua = UserAgent(use_cache_server = False, verify_ssl=False)
            userAgent = ua.random
            print(userAgent)
            chrome_options.add_argument(f'user-agent={userAgent}')
            # chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(PATH, options=chrome_options)
            URL = self.hURL + self.bc
            driver.get(URL)
            timeout = .1
            try:
                time.sleep(0.25)
                element_present = EC.presence_of_element_located((By.ID, 'global-search-input'))
                WebDriverWait(driver, timeout).until(element_present)
            except TimeoutException:
                print("Timed out")
            soup = BeautifulSoup(driver.page_source,"html.parser")
            return soup
      
def main():
    pass
if __name__ == "__main__":
    main()
        
    