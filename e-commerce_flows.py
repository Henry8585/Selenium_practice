from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select

service = Service(executable_path="C:/Webdrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
# the wait command will poll the HTML DOM for 10 seconds maximum if any element is not immediately actionable

driver.get("https://magento.softwaretestingboard.com/")
driver.find_element(By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/a").click()
driver.find_element(By.NAME, "login[username]").send_keys("henry.ocheche@tum.de")
driver.find_element(By.NAME, "login[password]").send_keys("Seleniumtest1")
driver.find_element(By.CSS_SELECTOR, "button[id=send2]").click()

category = driver.find_element(By.ID, "ui-id-6")
# This is a hoverable element - upon hover, a sub-category named "Watches" will be clicked on
ActionChains(driver) \
    .move_to_element(category) \
    .perform()
time.sleep(2)
driver.find_element(By.ID, "ui-id-27").click()

# Add one of the category items to cart
driver.find_element(By.XPATH,
                    "/html/body/div[2]/main/div[3]/div[1]/div[3]/ol/li[2]/div/div/strong/a").click()
driver.find_element(By.ID, "product-addtocart-button").click()
time.sleep(3)

# checkout flows
# click on the cart
cart = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[2]/header/div[2]/div[1]")))
cart.click()
time.sleep(2)
driver.find_element(By.XPATH,
                    "/html/body/div[2]/header/div[2]/div[1]/div/div/div/div[2]/div[3]/div").click()
time.sleep(3)

# fill out shipping address
address = driver.find_element(By.ID, "U6JPTAC")
address.click()
address.send_keys("TestAddress 1")

# to be completed ASAP



