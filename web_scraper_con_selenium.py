import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.latam.com/es_ec/apps/personas/booking?country=ec&vuelos_fecha_salida_ddmmaaaa=06/12/2020&auAvailability=1&language=es&nadults=1&cabina=Y&ninfants=0&ida_vuelta=ida&fecha1_dia=06&fecha1_anomes=2020-12&from_city1=UIO&flex=1&to_city1=GYE&nchildren=0#/'
agent = {'User-Agent':'Mozila/5.0'}
r = requests.get(url, headers = agent)

print(r.status_code)

s = BeautifulSoup(r.text, 'lxml')
print(s.prettify())

#Instanciar un driver del navegador
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(executable_path = '../chromedriver', options = options )

#Make the browser load the web page
driver.get(url)

#Extract info
vuelos = driver.find_elements_by_xpath('//li[@class = "flight"]')
print(vuelos)

print('**' * 5)

vuelo = vuelos[0]
print(vuelo)

duracion = vuelo.find_element_by_xpath('.//span[@class = "duration"]/time/span').get_text()
departure = vuelo.find_element_by_xpath('.//div[@class = "departure"]/time').get_attribute('datetime')
arrival = vuelo.find_element_by_xpath(('.//div[@class = "arrival"]/time').get_attribute('datetime')

#print(duracion)
#print(departure)
#print(arrival)


x = 5