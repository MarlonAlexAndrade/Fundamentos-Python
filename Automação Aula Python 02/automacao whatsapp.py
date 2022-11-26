from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

navegador = webdriver.Edge()
navegador.get('https://web.whatsapp.com')
sleep(30)
navegador.find_element('xpath','/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]').send_keys('Engenheiro Bruno'+Keys.ENTER)
input()