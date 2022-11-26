from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

navegador = webdriver.Edge()
navegador.get('https://www.proway.com.br')
navegador.find_element('name', 'termoBuscaCurso').send_keys('python' + Keys.ENTER)
cursos = navegador.find_elements('tag', 'h2')
input()