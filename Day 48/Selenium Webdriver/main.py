from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open even after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.in/gp/product/B092DDWT5F/ref=ox_sc_act_title_12?smid=A2C5GGIOO41BBI&psc=1")
driver.get("https://www.python.org/")

# To find an element

# price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# print(price.text)

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

search_button = driver.find_element(By.ID, value="submit")
print(search_button.tag_name)
print(search_button.size)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# driver.close()
driver.quit()
