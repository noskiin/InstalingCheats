from base64 import encode
from copy import copy
from posixpath import split
from tarfile import ENCODING
import time
from tkinter import W
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from translate import Translator
from datetime import date, datetime
import json

from random import randint
from random import seed


#podaj link do swojego instalingu Mój profil prawy górny róg
link = "https://instaling.pl/student/pages/mainPage.php?student_id=1817418"

browser = webdriver.Chrome()
browser.get(link)

badWordlist = {}

#Po send keys wpisz swoją nazwe potem hasło
Button = browser.find_element(By.ID,"log_email").send_keys("Oskar1898")
Button = browser.find_element(By.ID,"log_password").send_keys("ytecx")
Button = browser.find_element(By.XPATH ,"//button[@type='submit']").click()
Button = browser.find_element(By.CLASS_NAME,"big_button").click()


#sprawdza sesje czy jest kontynuowana czy rozpoczynasz
if browser.find_element(By.XPATH,"//*[@id='continue_session_button']/h4"):
    Button = browser.find_element(By.XPATH,"//*[@id='continue_session_button']/h4").click()
else:
    browser.find_element(By.XPATH,"//*[@id='start_session_button']/h4")
    
    
    
#Tłumaczeniew   
time.sleep(5)
Txt = browser.find_element(By.XPATH,"/html/body/div/div[8]/div[1]/div[2]/div[2]").get_attribute('textContent')
Txt = Txt.replace(" ","")

translator = Translator(from_lang="pl",to_lang="en")
translator = translator.translate(Txt)
print("Tłumaczę")
#tłumaczenie
FoundWord = False


with open("Slowka.txt","r",encoding="utf-8") as f:
        for line in f:
            if Txt in line:
                Split = line.split(":",1)
                Split[0] = Split[0].replace(" ","")
                badWord = {Split[0]:Split[1]}
                badWordlist.update(badWord)
                translator = badWordlist[Txt] 
                break
            else:
                print("KURDE NIE MA")
                translator = Translator(from_lang="pl",to_lang="en")
                translator = translator.translate(Txt)

time.sleep(randint(5,15))
Button = browser.find_element(By.XPATH,"//*[@id='answer']").send_keys(translator)
Button = browser.find_element(By.XPATH,"//*[@id='check']/h4")

time.sleep(3)
print("SPRAWDZAM CZY BŁĄD")
if browser.find_element(By.XPATH,"//*[@id='answer_result']/div").get_attribute('textContent') == "Niepoprawnie":
    print("KURDE BŁĄD")
    GoodWord = browser.find_element(By.XPATH,"//*[@id='word']").get_attribute('textContent')
    with open('Slowka.txt','a',encoding='utf-8') as f:
            f.write(Txt + " : " + GoodWord)
            f.write("\n")
            f.close()
    print("DODAŁEM SŁOWO")
    
time.sleep(2)
Button = browser.find_element(By.ID,"next_word").click()


while browser.find_element(By.ID,"next_word"):
    
    time.sleep(5)
    Txt = browser.find_element(By.XPATH,"/html/body/div/div[8]/div[1]/div[2]/div[2]").get_attribute('textContent')
    Txt = Txt.replace(" ","")
    print(Txt)
    with open("Slowka.txt","r",encoding="utf-8") as f:
        for line in f:
            if Txt in line:
                Split = line.split(":",1)
                Split[0] = Split[0].replace(" ","")
                badWord = {Split[0]:Split[1]}
                badWordlist.update(badWord)
                translator = badWordlist[Txt] 
                break
            else:
                print("KURDE NIE MA")
                translator = Translator(from_lang="pl",to_lang="en")
                translator = translator.translate(Txt)
                

    time.sleep(randint(5,15))
    Button = browser.find_element(By.XPATH,"//*[@id='answer']").send_keys(translator)
    Button = browser.find_element(By.XPATH,"//*[@id='check']/h4")
    time.sleep(3)

    time.sleep(3)
    print("SPRAWDZAM CZY BŁĄD")
    if browser.find_element(By.XPATH,"//*[@id='answer_result']/div").get_attribute('textContent') == "Niepoprawnie":
        print("KURDE BŁĄD")
        GoodWord = browser.find_element(By.XPATH,"//*[@id='word']").get_attribute('textContent')
        with open('Slowka.txt','a',encoding='utf-8') as f:
            f.write(Txt + " : " + GoodWord)
            f.write("\n")
            f.close()
        print("DODAŁEM SŁOWO")
        
    Button = browser.find_element(By.ID,"next_word").click()   
    time.sleep(10)

    
    




input()

time.sleep(5)