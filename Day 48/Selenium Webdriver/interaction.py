from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(url)

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# # print(article_count.text)
# article_count.click()

# Clicking on link
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Giving inputs in search bar
search_bar = driver.find_element(By.NAME, value="search")
search_bar.send_keys("Python", Keys.ENTER)

# driver.quit()
