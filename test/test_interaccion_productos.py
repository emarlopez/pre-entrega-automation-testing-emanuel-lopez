from selenium import webdriver
#Importar By para localizar elementos
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_interaccion_exitosa():
    
    #Iniciar el navegador
    driver = webdriver.Chrome()

    #Abrir pagina
    driver.get("https://www.saucedemo.com/")

    
    #login
    usuario= driver.find_element(By.ID,"user-name")
    password= driver.find_element(By.ID,"password")
    boton_login = driver.find_element(By.ID,"login-button")

    #Completar formulario
    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")
    

    boton_login.click()
    


   # Esperar a que cargue el catálogo
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )
    print("URL:", driver.current_url)
    print("Título:", driver.title)


      
    
   #Agregar mochila 
    boton_agregar=driver.find_element(By.CSS_SELECTOR,"[data-test='add-to-cart-sauce-labs-backpack']")
    boton_agregar.click()




    # Esperar contador del carrito
    contador = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
        )
    )

    # Verificar que el contador sea 1
    assert contador.text == "1"
    print(contador)


    #Verificar que se puede navegar al carrito
    carrito= driver.find_element(By.CSS_SELECTOR,"[data-test='shopping-cart-link']")
    carrito.click()
    time.sleep(2)


    #Comprobar que aparezca el producto en el carrito
    producto_agregado = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='item-quantity']")
        )
    )
 
    assert producto_agregado.text=="1"
    print("Producto agregado correctamente")


    