import time
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from selenium.webdriver.common.by import By


strikethrough_start = "\u001B[9m"
strikethrough_end = "\u001B[0m"

driver = webdriver.Chrome()
driver.get('https://store.steampowered.com/search/?term=')
time.sleep(1)

last_height = driver.execute_script("return document.body.scrollHeight")
for i in range(1, 3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


time.sleep(3)
elements = driver.find_elements(By.XPATH,"//a[@class='search_result_row ds_collapse_flag  app_impression_tracked']")

for i in elements:
    title = i.find_element(By.XPATH, ".//span[@class='title']").text
    price = i.find_element(By.XPATH, ".//div[@class='discount_prices']").text
    date = i.find_element(By.XPATH, ".//div[@class='col search_released responsive_secondrow']").text
    image = i.find_element(By.XPATH, ".//img").get_attribute('src')
    print(image)
    print(title)
    print(date)
    if len(price.split()) > 1 and price is not str:
        wout_price = price.replace("$", "")
        print(strikethrough_start + '$' + wout_price.split()[0] + strikethrough_end)
        a = i.find_element(By.XPATH, ".//div[@class='discount_pct']").text
        print(a)
        print('$' + wout_price.split()[1])
    else:
        print(price)
    print('-'*60)

driver.quit()
print('Hello World')
