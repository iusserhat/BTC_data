from selenium import webdriver
from time import sleep  

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.delete_all_cookies()

driver.get("https://tr.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT")
driver.implicitly_wait(5)

while True:

    fiyat_bilgisi = driver.find_element("xpath", ' html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]').text
   
    print(fiyat_bilgisi)
    sleep(5)

