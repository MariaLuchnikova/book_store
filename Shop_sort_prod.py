from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_id("username").send_keys("tiledi5421@ezgiant.com")
driver.find_element_by_id("password").send_keys("GalaktikaG2023+")
driver.find_element_by_name("login").click()
driver.find_element_by_link_text("Shop").click()
sort_fld = driver.find_element_by_class_name("orderby")
sort_value = sort_fld.get_attribute("value")
if sort_value != "menu_order":
    print(f'Ошибка: ожидается вариант сортировки по умолчанию')
select_upd = Select(sort_fld).select_by_value("price-desc")
sort_fld = driver.find_element_by_class_name("orderby")
sort_value = sort_fld.get_attribute("value")
if sort_value != "price-desc":
    print(f'Ошибка: ожидается вариант сортировки по цене от большей к меньшей')
driver.quit()