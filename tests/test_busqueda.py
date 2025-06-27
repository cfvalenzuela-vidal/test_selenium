from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)  # Espera máxima de 10 segundos

driver.get("https://duckduckgo.com/")

# Buscar campo de texto usando espera explícita
buscador = wait.until(EC.presence_of_element_located((By.NAME, "q")))
buscador.send_keys("inmuebles en Bogotá")
buscador.send_keys(Keys.RETURN)

# Esperar resultados usando espera explícita
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='result']")))

# Buscar y hacer clic en enlace deseado
url_deseada = "https://arriendo.com/co/bogota/"
enlaces = driver.find_elements(By.CSS_SELECTOR, "[data-testid='result'] a")

for enlace in enlaces:
    href = enlace.get_attribute("href")
    if href and url_deseada in href:
        enlace.click()
        break
else:
    raise Exception(f"No se encontró el enlace a {url_deseada}")

# Esperar que la nueva página cargue usando espera explícita
wait.until(EC.url_contains(url_deseada))

# Tomar screenshot (manteniendo tu lógica original)
driver.save_screenshot("screenshot.png")

driver.quit()

"""
#LUPA
try:
    # Localizar el botón lupa por su atributo 'aria-label'
    boton_lupa = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
    )
    print("Botón de búsqueda (lupa) encontrado correctamente")

except Exception as e:
    print(f"Error: {e}")"""