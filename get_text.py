from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "email")))
# Buscar el campo Correo electrónico y rellenarlo
driver.find_element(By.ID, "email").send_keys("jorge.caceresgarcia@gmail.com")

# Buscar el campo Contraseña y rellenarlo
driver.find_element(By.ID, "password").send_keys("soph1006")

# Buscar el botón Iniciar sesión y hacer clic en él
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))
time.sleep(2)

# Buscar el botón, recuperar su texto y comprobar que el valor del texto es 'Cerrar sesión'
assert driver.find_element(By.CLASS_NAME, "header__logout").text == 'Cerrar sesión'
print(driver.find_element(By.CLASS_NAME, "header__logout").text )
time.sleep(2)
driver.quit()