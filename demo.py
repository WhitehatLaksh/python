from operator import truediv
import time
from tkinter import BROWSE
from selenium import webdriver
import json

# Initialize a webdriver instance
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# chromeOptions = webdriver.ChromeOptions()
# prefs = {"download.default_directory" : "C:/Users/Jai Kishan Saini/Desktop/Lakshay/har file/exactspace.har"}
# options.add_experimental_option("prefs",prefs)
# chromedriver = "C:/Users/Jai Kishan Saini/Desktop/Lakshay/python-local-main/chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)

driver.get("https://exactspace.co/")
time.sleep(4)
# Read the contents of the HAR file
with open(r'C:/Users/Jai Kishan Saini/Desktop/Lakshay/har file/exactspace.har', encoding="utf8") as f:
    har_data = json.load(f)
time.sleep(2)
# Get the list of all HTTP requests made by the webdriver
entries = har_data['log']['entries']
time.sleep(2)
# Initialize counters for the different status code groups
total_count = 0
two_xx_count = 0
four_xx_count = 0
five_xx_count = 0

# Iterate over the list of entries and update the counters
for entry in entries:
    status = entry['response']['status']
    total_count += 1
 
    if 200 <= status < 300:
        two_xx_count += 1
    elif 400 <= status < 500:
        four_xx_count += 1
    elif 500 <= status < 600:
        five_xx_count += 1

# Print the results
print(f'Total status code count: {total_count}')
print(f'Total count for 2XX status codes: {two_xx_count}')
print(f'Total count for 4XX status codes: {four_xx_count}')
print(f'Total count for 5XX status codes: {five_xx_count}')

print("Quitting Selenium WebDriver")
driver.quit()