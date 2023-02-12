from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_id("username").send_keys("tiledi5421@ezgiant.com")
driver.find_element_by_id("password").send_keys("GalaktikaG2023+")
driver.find_element_by_name("login").click()
driver.find_element_by_link_text("Shop").click()
driver.find_element_by_xpath("//h3[text()='Android Quick Start Guide']").click()
old_price = driver.find_element_by_xpath("//del").text
assert old_price == "₹600.00"
new_price = driver.find_element_by_xpath("//ins /span").text
assert new_price == "₹450.00"
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "wp-post-image")))
driver.find_element_by_class_name("wp-post-image").click()
wait.until(EC.visibility_of_element_located((By.ID, "fullResImage")))
driver.find_element_by_class_name("pp_close")
driver.quit()

