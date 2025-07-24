from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/")




input_box = driver.find_element(By.ID, "userInput")
input_box.send_keys("I am really stressed today.")
input_box.send_keys(Keys.ENTER)

response = driver.find_element(By.ID, "chatlog")

time.sleep(0.5)

print("Chatbot response:", response.text)


input_box = driver.find_element(By.ID, "userInput")
input_box.send_keys("I really enjoy playing games")
input_box.send_keys(Keys.ENTER)

response = driver.find_element(By.ID, "chatlog")

time.sleep(0.5)

print("Chatbot response:", response.text)




driver.quit()
