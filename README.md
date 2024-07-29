# WebScraping

## Introduction
This project focuses on web scraping using Selenium to extract data from the Otomoto website. The goal is to automate the process of searching for SUVs with specific criteria and download the first three car images that match the search criteria.

## Project Description
The script utilizes Selenium WebDriver to interact with the Otomoto website. It automates the process of accepting cookies, setting search filters, and downloading images of cars that match the search criteria. Below is a detailed breakdown of the code functionality.

## Used technologies
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
<img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white" />




## Key Steps in the Code
### Setup and Initialization
- Import necessary libraries: Selenium WebDriver, WebDriverWait, By, Keys, etc.
- Initialize the Firefox WebDriver.
- Open the Otomoto website and wait implicitly for elements to load.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import *
import os
import urllib

browser = webdriver.Firefox()
browser.get("https://www.otomoto.pl/")
browser.implicitly_wait(5)

```

### Accept Cookies
Locate and click the "Accept" button for cookies.

```python
cookies_button = browser.find_element(By.XPATH, '//button[text()="Akceptuję"]')
cookies_button.click()
sleep(2)

```

### Navigate to Search Filters
Locate and click the button to show search filters.

```python
show_button = browser.find_element(By.CLASS_NAME, 'e1nolozt4')
show_button.click()
sleep(3)
browser.implicitly_wait(5)

```

### Set Vehicle Type
Click the button to select the vehicle type and choose "SUV".

```python
type_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ooa-1mk5374')))
type_button.click()
suv_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@data-testid="label"]/p[text()="SUV"]')))
suv_button.click()
close_type_button = browser.find_element(By.CLASS_NAME, 'ooa-143dufj')
close_type_button.click()
sleep(2)

```

### Set Price and Production Year
Input maximum price and minimum production year for the search.

```python
maxPrice_input = browser.find_element(By.XPATH, '//input[@placeholder="Cena do"]')
maxPrice_input.send_keys('80000')
sleep(2)
production_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Rok produkcji od"]')))
production_input.send_keys('2018')
production_input.send_keys(Keys.ENTER)
sleep(3)

```

### Set Mileage and Damage Condition
Input maximum mileage and select the non-damaged condition.

```python
km_input = browser.find_element(By.XPATH, '//input[@placeholder="Przebieg do"]')
km_input.send_keys('75000')
sleep(2)
damage_click = browser.find_element(By.XPATH, '//div[@data-testid="filter_enum_damaged"]/div/div/input[@placeholder="Stan uszkodzeń"]')
damage_click.send_keys('Nieuszkodzony')
damage_check = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="filter_enum_damaged"]/div/ul/li')))
damage_check.click()
sleep(2)

```

### Select Car Brand
Input and select the car brand "BMW".

```python
model_click = browser.find_element(By.XPATH, '//div[@data-testid="filter_enum_make"]/div/div/input[@placeholder="Marka pojazdu"]')
model_click.click()
model_click.send_keys('BMW')
sleep(2)
model_check = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="filter_enum_make"]/div/ul/li')))
model_check.click()
close_model_button = browser.find_element(By.XPATH, '//div[@data-testid="filter_enum_make"]/div/div/span/button[@data-testid="arrow"]')
close_model_button.click()
sleep(4)

```

### Retrieve and Save Images
Locate image elements, retrieve their URLs, and download the first three images.

```python
search_img_elements = browser.find_elements(By.XPATH, "//img[contains(@class, 'ooa-2zzg2s')]")
image_urls = [search_img_elements[i].get_attribute('src') for i in range(min(3, len(search_img_elements)))]

if not os.path.exists("C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\WebScraping\\car_images"):
    os.makedirs("C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\WebScraping\\car_images")

for i, url in enumerate(image_urls):
    urllib.request.urlretrieve(url, f"car_images/car{i}.jpg")

print('DONE')
browser.close()

```

## Usage
To use this script, ensure you have the necessary dependencies installed:
- Selenium
- Firefox WebDriver

Run the script in a Python environment, and it will perform the automated web scraping as described.


## Conclusion
This web scraping project demonstrates how to use Selenium for automating interactions with a web page, applying search filters, and downloading images. It can be extended to scrape more data or handle different websites based on similar principles.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://www.mit.edu/~amini/LICENSE.md).

art. 74 ust. 1 Ustawa o prawie autorskim i prawach pokrewnych, [Zakres ochrony programów komputerowych](https://lexlege.pl/ustawa-o-prawie-autorskim-i-prawach-pokrewnych/a







