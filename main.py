import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from plyer import notification

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.zonakids.com/productos/pack-x-25-sobres-de-figuritas-fifa-world-cup-qatar-2022/")

def comprar():
    element = driver.find_element(By.CLASS_NAME, "js-prod-submit-form")
    element.click()

while True:
    time.sleep(10)
    try:
        element = driver.find_element(By.CSS_SELECTOR, "input.nostock")

        if not element.is_displayed():
            notification.notify(
                title="Zona Kids",
                message="Hay stock!",
            )
            comprar()
            break

        driver.refresh()
    except:
        notification.notify(
            title="Zona Kids",
            message="Hay stock!",
        )
        comprar()
        break
