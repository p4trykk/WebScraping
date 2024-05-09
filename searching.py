from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import *



browser=webdriver.Firefox()
browser.get("https://www.otomoto.pl/")
browser.implicitly_wait(5)

wait = WebDriverWait(browser, 6)

cookies_button=browser.find_element(By.XPATH, '//button[text()="Akceptuję"]')
cookies_button.click()

sleep(2)


show_button = browser.find_element(By.CLASS_NAME, 'e1nolozt4')
show_button.click()

sleep(3)
browser.implicitly_wait(5)

#show_buttons = browser.find_element(By.CLASS_NAME, 'ooa-j7trgb')
#type_button = browser.find_element(By.CLASS_NAME, 'ooa-1mk5374')
try:
    type_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ooa-1mk5374')))
    type_button.click()
except StaleElementReferenceException:
    type_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ooa-1mk5374')))
    type_button.click()

sleep(2)

suv_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@data-testid="label"]/p[text()="SUV"]')))
suv_button.click()

close_type_button=browser.find_element(By.CLASS_NAME, 'ooa-143dufj')
close_type_button.click()

sleep(2)

maxPrice_input=browser.find_element(By.XPATH, '//input[@placeholder="Cena do"]')
maxPrice_input.send_keys('80000')

sleep(2)

production_input=wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Rok produkcji od"]')))
production_input.send_keys('2018')
production_input.send_keys(Keys.ENTER)

sleep(3)

km_input=browser.find_element(By.XPATH, '//input[@placeholder="Przebieg do"]')
km_input.send_keys('75000')

sleep(2)

damage_click=browser.find_element(By.XPATH, '//div[@data-testid="filter_enum_damaged"]/div/div/input[@placeholder="Stan uszkodzeń"]')
damage_click.send_keys('Nieuszkodzony')

# sleep(2)

damage_check=wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="filter_enum_damaged"]/div/ul/li')))
damage_check.click()

sleep(4)

browser.close()