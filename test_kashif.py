import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import  time

def setup_function():
    global driver
    driver = webdriver.Firefox(service=Service("geckodriver.exe"))
    driver.get('https://alnafi.com/auth/sign-in')
    driver.maximize_window()
    driver.implicitly_wait(10)

def teardown_function():
    driver.quit()

def my_cred():
    return [
        ('abdeali@gmail.com', 'abdeali@123'),
        ('ali@gmail.com', 'ali@123'),
        ('abd@gmail.com', 'abd@123')
    ]
@pytest.mark.parametrize("username,password",my_cred())
def test_login(username,password):
    print("My pytest login")
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/form/div[1]/div/div/input').send_keys(username)
    time.sleep(1.5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/form/div[2]/div/div/input').send_keys(password)
