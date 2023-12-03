from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class demo_element_by_id:
    def loc_by_id(self):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        element = driver.find_element(By.ID, "login-input")
        element.send_keys("test@test.com")
        time.sleep(4)

findbyid = demo_element_by_id()

findbyid.loc_by_id()
