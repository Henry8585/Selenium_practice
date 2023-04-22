from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select

service = Service(executable_path="C:/Webdrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)
# the wait command will poll the HTML DOM for 5 seconds maximum if any element is not immediately actionable

driver.get("https://www.eurowings.com/en/information/at-the-airport/flight-status.html")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                            "/html/body/div[1]/div/div/footer/div[2]/button[3]"))).click()
driver.find_element(By.XPATH,
                    '//*[@id="site"]/main/div[3]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/div[1]/div/div/button').click()
driver.find_element(By.ID, "station-select-198-input")
actions = ActionChains(driver)
actions.send_keys("Cologne-Bonn")
actions.send_keys(Keys.ENTER)
actions.perform()

driver.find_element(By.XPATH,
                    '//*[@id="site"]/main/div[3]/div[3]/div/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div/button').click()
driver.find_element(By.ID, "station-select-199-input")
actions = ActionChains(driver)
actions.send_keys("Berlin Brandenburg")
actions.send_keys(Keys.ENTER)
actions.perform()

driver.find_element(By.XPATH,
                    '//*[@id="site"]/main/div[3]/div[3]/div/div[1]/div/div[2]/div[1]/form/div[1]/div/div[1]').click()
driver.find_element(By.CSS_SELECTOR, "input[value='2023-04-23']").click()

driver.find_element(By.XPATH,
                    '//*[@id="site"]/main/div[3]/div[3]/div/div[1]/div/div[2]/div[1]/form/div[2]/button/span[2]').click()
time.sleep(5)

if 'Departure gate' in driver.page_source:
    print('Flight search successful')

elif 'Unfortunately, we could not find any results for your search.' in driver.page_source:
    print('Flight search not successful')

driver.quit()
