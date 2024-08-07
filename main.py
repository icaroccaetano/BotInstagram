from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = "icaroccaetano"
password =  "icaroccaetano1702"

def main():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https:/instagram.com")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(username)
    driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(password)
    driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button").click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/section/main/div/div/div/div/button"))).click()

    driver.get("https:/instagram.com/" + username)


main()