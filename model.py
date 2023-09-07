import time
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
with open('./config.yaml') as f:
        data = yaml.safe_load(f)
        address = data['address']
        driver_path = data['driver_path']
        browser = data['browser']
class Site:
        def __init__(self, address):
                if browser == 'chrome':
                        service = Service(executable_path=driver_path)
                        options = webdriver.ChromeOptions()
                        self.driver = webdriver.Chrome(service=service, options=options)
                self.driver.maximize_window()
                self.driver.get(address)
                time.sleep(config['sleep_time'])
                
        def find_element(self, mode, path):
                if mode == "css":
                        element = self.driver.find_element(By.CSS_SELECTOR, path)
                elif mode == "xpath":
                        element = self.driver.find_element(By.XPATH, path)
                return element