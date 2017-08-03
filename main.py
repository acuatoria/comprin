from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import re
driver=webdriver.Firefox(executable_path='./geckodriver')
articulo='https://www.amazon.es/Trixie-Activity-Board-%C3%B823x3-nivelo/dp/B0054Q9TMA/ref=sr_1_1?ie=UTF8&qid=1501697928&sr=8-1&keywords=trixie'

current_price=1000000000000
desired_price=10.5
user="xxx@xxx.xxx"
password="xxx"

def wait(web,time):
	try:
		element=WebDriverWait(web,time).until(EC.presence_of_element_located((By.ID,"no_existe")))
	except:
		pass

def comprar(web):
	print ('shopping..')
	add_to_cart=web.find_element_by_id('add-to-cart-button')
	add_to_cart.click()
	wait(web,3)
	tramitar=web.find_element_by_id('hlb-ptc-btn-native')
	tramitar.click()
	wait(web,3)
	email=web.find_element_by_name('email')
	email.send_keys(user)
	clave=web.find_element_by_name('password')
	clave.send_keys(password)
	enviar=web.find_element_by_class_name('a-button-input')
	enviar.click()
	wait(web,7)
	shiping= web.find_element_by_id('orderSummaryPrimaryActionBtn')
	shiping.click()
	wait(web,5)
	pago=web.find_element_by_id('useThisPaymentMethodButtonId')
	pago.click()
	wait(web,5)
	comprar=web.find_element_by_id('submitOrderButtonId')
	comprar.click()


while current_price>desired_price:
	driver.get(articulo)
	fuente=driver.page_source
	texto_r=re.findall('{"asin":.+?}',fuente)
	texto_precio=''
	for texto in texto_r:
		codigos=re.findall(r'("asin":")(\w+)',texto)
		
		for codigo in codigos:
			
			if codigo[1] in articulo and 'price' in texto:

				texto_precio=texto

	
	precio=re.findall(r'("price":)[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?',texto_precio)
	current_price=float(precio[0][1])
	print("price:"+str(current_price))
	
	

comprar(driver)

