"""
Proiect : Testarea unei aplicatii web
Script pentru platforma Facebook ce testeaza: autentificarea, funcția de postare.
Membrii : Avram Petru-Alin , Avram Cristian-Calin
Surse folosite : https://selenium-python.readthedocs.io/
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import sys
import os
import time
import variabile as v

login = True
var = True

start_time = time.time()
# Este creata instanța Chrome WebDriver
driver = webdriver.Chrome(v.path_driver)
# WebDriver navighează la pagina de Facebook dată de URL
driver.get(v.fb_addres)

driver.maximize_window()

# Introducere date utilizator
username_textbox = driver.find_element_by_id("email")
username_textbox.send_keys(v.username)

password_textbox = driver.find_element_by_id("pass")
password_textbox.send_keys(v.password)

# Acceptare cookies
time.sleep(1)
try:
    driver.find_element_by_xpath(v.accept_all).click()
except:
    error = sys.exc_info()[0]
    tb = sys.exc_info()[2]
    print(f"{error} line {tb.tb_lineno}")

# Testarea functiei de logare
try:
    WebDriverWait(driver, timeout=5).until(ec.presence_of_element_located((By.NAME, "login"))).click()
except:
    login = False
    error = sys.exc_info()[0]
    tb = sys.exc_info()[2]
    print(f"{error} line {tb.tb_lineno}")
    driver.quit()

if login and (v.username == "avram_ionel2001@yahoo.com" and v.password == "andreipop12"):
    print("Successful login !")
else:
    print("Unsuccessful login !")
    var = False

# Testarea functiei de postare
if var:
    try:
        time.sleep(9)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(1)
        WebDriverWait(driver, timeout=5).until(ec.presence_of_element_located((By.XPATH, v.xpath_create))).click()
        time.sleep(1)
        WebDriverWait(driver, timeout=5).until(ec.presence_of_element_located((By.XPATH, v.xpath_post))).click()
        time.sleep(1)
        WebDriverWait(driver, timeout=5).until(ec.presence_of_element_located((By.XPATH, v.xpath_comment))).send_keys(v.comment)
        time.sleep(1)
        WebDriverWait(driver, timeout=5).until(ec.presence_of_element_located((By.XPATH, v.xpath_image))).click()
        time.sleep(2)
        # Am utilizat AutoIT&SciTE pentru a incarca imaginea dorita
        os.startfile(v.upload_image)
        time.sleep(1)
        WebDriverWait(driver, timeout=5).until(ec.presence_of_element_located((By.XPATH, v.xpath_post_message))).click()
        print("Successful post !")
    except:
        error = sys.exc_info()[0]
        tb = sys.exc_info()[2]
        print(f"\n{error} line {tb.tb_lineno}")
        print("Unsuccessful post !")

# Inchidere WebDriver
if login:
    time.sleep(10)
    driver.close()

# Timpul de executie
execution_time = time.time() - start_time
print("\nTotal execution time {}".format(execution_time))
