from contextlib import nullcontext
from telnetlib import EC
import time, os
from typing import Self
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from tkinter import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from tkinter import *  
email = "uor2fr56wc@maildax.me"
password = "Youcefbada2004"
sujet  = "logo design "
comment  = "hello world"
def start(email , password,sujet ,comment):
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    time.sleep(4)
    driver.get("https://www.tumblr.com/login")
    time.sleep(4)
    driver.find_element(By.XPATH,'//input[@placeholder="Email"]').send_keys(str(email))
    time.sleep(1)
    driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys(str(password))
    time.sleep(1)
    driver.find_element(By.XPATH,'//button[@class="TRX6J CxLjL qjTo7 CguuB yC5pj" or aria-label="Log in"]').click()
    time.sleep(10)
    driver.find_element(By.XPATH,'//input[@placeholder="Password" or @class="NaqPB"]').send_keys(str(sujet))
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR,'#base-container > div.D5eCV > div > div._3xgk.ZN00W > div > div.e1knl > aside > div.N5wJr > div > span > div > div > div > div:nth-child(1) > a:nth-child(1)').click()
    time.sleep(20)
    i = 1
    while True : 
                time.sleep(3)
                print(i)
                driver.find_element(By.XPATH,'//*[@id="base-container"]/div[2]/div/div[2]/div/div[1]/main/div[2]/div[2]/div[{}]/div[1]/div/div/div/article/div[2]/footer/div[2]/div[2]/div[2]/span/span/button'.format(str(i))).click()
                time.sleep(5)
                driver.find_element(By.CLASS_NAME,"N8H25").send_keys(str(comment))
                time.sleep(4)
                driver.find_element(By.XPATH,'//button[@class="TRX6J v6i4P" or @aria-label="Reply" or @type="submit"]').click()
                time.sleep(5)
                driver.find_element(By.XPATH,'//*[@id="base-container"]/div[2]/div/div[2]/div/div[1]/main/div[2]/div[2]/div[{}]/div[1]/div/div/div/article/div[2]/footer/div[2]/div[2]/div[2]/span/span/button'.format(str(i+1))).click()
                time.sleep(5)
                driver.find_element(By.CLASS_NAME,"N8H25").send_keys(str(comment))
                time.sleep(4)
                driver.find_element(By.XPATH,'//button[@class="TRX6J v6i4P" or @aria-label="Reply" or @type="submit"]').click()
                time.sleep(5)
                driver.execute_script("window.scrollBy(0, 1500);")
                time.sleep(4)
                i = i + 1
                print("sucesss")
    time.sleep(5)
start(email,password,sujet,comment)
#driver.find_element(By.CLASS_NAME,"N8H25").send_keys("hello world")
#time.sleep(4)
#driver.find_element(By.XPATH,'//button[@class="TRX6J v6i4P" or @aria-label="Reply" or @type="submit"]').click()
#time.sleep(5)