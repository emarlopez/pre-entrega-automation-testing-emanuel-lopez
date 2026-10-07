from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#se importara  para acceder a la funcion by
import time

def test_navegacion_exitoso():
    
    #Iniciar el navegador
    driver = webdriver.Chrome()

    #Abrir pagina
    driver.get("https://www.saucedemo.com/")

    
    #Localizar elementos
    usuario= driver.find_element(By.ID,"user-name")
    password= driver.find_element(By.ID,"password")
    boton_login = driver.find_element(By.ID,"login-button")

    #Completar formulario
    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")

    
    #Hacer login
    boton_login.click()



    #validar titulo de la pagina
    assert driver.title =="Swag Labs"
    print(driver.title)


    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    #Validar existencia de productos
    assert  len(productos)>0

    primer_producto = productos[0]

    nombre_producto = primer_producto.find_element(By. CLASS_NAME, "inventory_item_name").text
    precio_producto = primer_producto.find_element(By. CLASS_NAME, "inventory_item_price").text

    #Validar nombre y precio
    assert nombre_producto =="Sauce Labs Backpack"
    assert precio_producto =="$29.99"


    #Validar boton hamburguesa
    boton_burger = driver.find_element(By.ID,"react-burger-menu-btn")
    assert boton_burger.is_displayed()

    #Validar filtro
    filtro= driver.find_element(By.CLASS_NAME,"product_sort_container")
    assert filtro.is_displayed()


    #Validar carrito
    carrito = driver.find_element(By.CSS_SELECTOR,"[data-test='shopping-cart-link']")
    assert carrito.is_displayed()

    driver.quit()

    