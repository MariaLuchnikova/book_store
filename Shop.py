from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_id("username").send_keys("tiledi5421@ezgiant.com")
driver.find_element_by_id("password").send_keys("GalaktikaG2023+")
driver.find_element_by_name("login").click()
driver.find_element_by_link_text("Shop").click()
driver.find_element_by_xpath("//h3[text()='HTML5 Forms']").click()
element = driver.find_element_by_class_name("entry-title").text
# assert element == "HTML5 Forms"
if element != "HTML5 Forms":
    print(f'Ошибка: заголовок книги {element}. Ожидается "HTML5 Forms"')
driver.quit()