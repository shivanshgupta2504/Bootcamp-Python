from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.python.org/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(url)

event_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .shrubbery .menu li")
event_list = [event.text for event in event_list]
event_list_directory = {
    i: {"time": event_list[i].split('\n')[0], "name": event_list[i].split('\n')[1]} for i in range(len(event_list))
}
print(event_list_directory)
driver.quit()


