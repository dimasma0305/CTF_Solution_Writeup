# import chrome_driver
from selenium import webdriver

#open url
driver = webdriver.Chrome()
var_value = ['Gunting', 'Batu', 'Kertas']
driver.get("https://web.ctf.rasyidmf.com/chal25/")
True_var=[]
#click batu button by value
driver.find_element_by_xpath("//input[@value='Batu']").click()
driver.find_element_by_xpath("//input[@value='Batu']").click()
driver.find_element_by_xpath("//input[@value='Kertas']").click()
driver.find_element_by_xpath("//input[@value='Batu']").click()
driver.find_element_by_xpath("//input[@value='Kertas']").click()
driver.find_element_by_xpath("//input[@value='Batu']").click()
driver.find_element_by_xpath("//input[@value='Kertas']").click()
driver.find_element_by_xpath("//input[@value='Kertas']").click()
driver.find_element_by_xpath("//input[@value='Gunting']").click()
driver.find_element_by_xpath("//input[@value='Kertas']").click()
driver.find_element_by_xpath("//input[@value='Kertas']").click()
driver.find_element_by_xpath("//input[@value='Gunting']").click()
driver.find_element_by_xpath("//input[@value='Gunting']").click()
driver.find_element_by_xpath("//input[@value='Batu']").click()
driver.find_element_by_xpath("//input[@value='Gunting']").click()
driver.find_element_by_xpath("//input[@value='Batu']").click()
driver.find_element_by_xpath("//input[@value='Kertas']").click()
driver.find_element_by_xpath("//input[@value='Batu']").click()
driver.find_element_by_xpath("//input[@value='Gunting']").click()