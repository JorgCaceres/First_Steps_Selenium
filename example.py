from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
# Buscar el botón y hacer clic en él
# visibility_of_element_located El elemento esta prensete y es visible
# WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[@class='auth-form__button']")))
driver.implicitly_wait(3)
driver.find_element(By.XPATH, ".//button[@class='auth-form__button']").click()
time.sleep(2)
email = driver.find_element(By.ID, "email").send_keys("alejandrita.tepienso@todoeldia.com")
time.sleep(5)
driver.quit()