from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import sleep

driver_path = "C:\\Users\\sss\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

s = Service( driver_path )
options = webdriver.ChromeOptions()
options.binary_location = brave_path

browser = webdriver.Chrome(service = s, options=options)
browser.get("https://www.instagram.com")

def start():
    wait = WebDriverWait(browser,10)
    
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
    username_field.send_keys(username)
    sleep(1)
    
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
    password_field.send_keys(pasw)
    sleep(1)
    
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()
    sleep(2)

def out():
    browser.find_element(By.XPATH,'//*[@id="mount_0_0_z0"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/span/div/a/div/div[1]/div/div/svg').click()
    browser.find_element(By.XPATH,'//*[@id="mount_0_0_z0"]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[6]/div[1]/div/div/div/div/div/span/span').click()
    
username ="Username"
pasw ="Password"
start()

sleep(7)

out()


