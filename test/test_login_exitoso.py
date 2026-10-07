from selenium import webdriver
from selenium.webdriver.common.by import By
#se importara  para acceder a la funcion by
import time


#Automatización de Login

def test_login_exitoso():   
    #Iniciar el navegador
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)

    try:
        #Abrir pagina
        driver.get("https://www.saucedemo.com/")


        #Localizar elementos
        usuario= driver.find_element(By.ID,"user-name")
        password= driver.find_element(By.ID,"password")
        boton_login = driver.find_element(By.ID,"login-button")

        #Completar formulario
        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")

        time.sleep(2)
        
        #Hacer login
        boton_login.click()

        #variable correspondiente al titulo swag
        logo=driver.find_element(By.CLASS_NAME,"app_logo") 

        #variable correspondiente a products
        products = driver.find_element(By.CSS_SELECTOR,"[data-test='title']")

        #Validar url de inventory.html
        assert driver.current_url == "https://www.saucedemo.com/inventory.html" 

        #validar texto swag   
        assert logo.text== "Swag Labs"

        #validar products
        assert products.text=="Products"

    finally:   
        driver.quit()


        