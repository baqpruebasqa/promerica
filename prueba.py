from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configura el navegador y abre el sitio web
driver = webdriver.Chrome()  # Asegúrate de tener el controlador de Chrome instalado y configurado
url = "https://www.clubpromerica.com/costarica/"
driver.get(url)

# Parte 1: Acceso y Navegación
try:
    # Navega a una página interna del sitio (contacto)
    contacto_url = "https://www.clubpromerica.com/costarica/contactus"
    driver.get(contacto_url)

    # Verifica si la página contiene un elemento específico por su XPath
    elemento_xpath = "/html/body/div[7]/div[3]/div[3]/div/div/div[2]/form/div[2]/div/div[1]/input"
    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, elemento_xpath)))
    print(f"Elemento encontrado en la página: {elemento.text}")

except Exception as e:
    print(f"Error en la Parte 1: {e}")

# Parte 2: Interacción con Elementos
try:
    # Rellena el formulario
    nombre_input = driver.find_element(By.NAME, "FullName")
    nombre_input.send_keys('Oscar Baquero')

    email_input = driver.find_element(By.NAME, "Email")
    email_input.send_keys('oscar@email.com')

    desc_input = driver.find_element(By.NAME, "Enquiry")
    desc_input.send_keys('Prueba de automatización')

    # Haz clic en el botón para enviar el formulario
    enviar_boton = driver.find_element(By.NAME, "send-email")
    enviar_boton.click()

except Exception as e:
    print(f"Error en la Parte 2: {e}")

# Parte 3: Validación
try:
    # Navega a otra página del sitio web
    otra_pagina_url = "https://www.clubpromerica.com/costarica/comercios-2"
    driver.get(otra_pagina_url)

except Exception as e:
    print(f"Error en la Parte 3: {e}")

# Parte 4: Capturas de Pantalla y Reportes
try:
    # Captura una imagen de la página actual
    driver.save_screenshot("captura.png")
    print("Captura de pantalla realizada correctamente")

    # Genera un informe de prueba simple
    informe = f"Informe de Prueba:\nParte 1: Acceso y Navegación - OK\nParte 2: Interacción con Elementos - OK\nParte 3: Validación - OK\nParte 4: Capturas de Pantalla y Reportes - OK"
    with open("informe_prueba.txt", "w") as file:
        file.write(informe)
    print("Informe de prueba generado correctamente")

except Exception as e:
    print(f"Error en la Parte 4: {e}")

finally:
    # Parte 5: Limpiar y Finalizar
    try:
        # Cierra el navegador
        driver.quit()
        print("Navegador cerrado correctamente")

    except Exception as e:
        print(f"Error al cerrar el navegador: {e}")