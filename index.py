from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.service import Service
import time

def scrapStore(driver):
  driver.implicitly_wait(20)
  storeData = {}
  storeData['name'] = driver.find_element(By.XPATH, '//*[@id="dokan-content"]/div[1]/div[1]/div/div/div/div[1]/h1').text
  storeData['phone'] = driver.find_element(By.XPATH, '//*[@id="dokan-content"]/div[1]/div[1]/div/div/div/div[2]/ul/li[2]/a').text
  return storeData

driverPath = '/usr/bin/chromedriver'
# options = Options()
# options.headless = True

s = Service(driverPath)

# driver = webdriver.Chrome(service = s, options = options, executable_path=driverPath)
driver = webdriver.Chrome(executable_path=driverPath)

website = 'https://shop.nipah.id/store-listing/'
driver.get(website)

# GET IPHONE
time.sleep(3)
driver.implicitly_wait(30)

# wrapper = driver.find_element(By.CLASS_NAME, 'dokan-seller-wrap')
# print(wrapper)
# iphone.click()

pageSource = bs(driver.page_source, 'lxml')

wrapper = pageSource.find('ul', class_="dokan-seller-wrap")
stores = wrapper.findAll('li')

data = []

for idx, d in enumerate(stores, 1):
  print('Scraping store', idx)
  urlXpath = '//*[@id="dokan-seller-listing-wrap"]/div/ul/li['+ str(idx) +']/div/div[3]/a'
  storeDetail = driver.find_element(By.XPATH, urlXpath)
  storeDetail.click()
  time.sleep(1)
  result = scrapStore(driver)
  data.append(result)
  driver.back()

print("total scraped stores = ", str(len(data)))
print(data)

