from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json

chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")

chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.demoblaze.com/")

time.sleep(3)

btn = driver.find_element(By.LINK_TEXT, 'Laptops')
btn.click()

btn = driver.find_element(By.ID, 'next2')
btn.click()
time.sleep(3)

computer = driver.find_elements(By.CLASS_NAME, 'card')

laptop_data = []
for product in computer:
    name = product.find_element(By.CLASS_NAME, 'hrefch')
    price = product.find_element(By.TAG_NAME, 'h5')
    description = product.find_element(By.ID, 'article')

    laptop_data.append({
        'name': name.text,
        'price': price.text,
        'description': description.text
    })

with open('laptops.json', 'w', encoding='utf-8') as file:
    json.dump(laptop_data, file,  indent=2)

print('completed')
