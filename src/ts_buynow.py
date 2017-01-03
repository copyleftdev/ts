from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as WT
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select as S
from selenium.webdriver.common.by import By
import random

from faker import Factory

fake = Factory.create()



driver = webdriver.Chrome()
driver.delete_all_cookies()


driver.get("https://qaorigin.metrofax.com/buy-now/fax-numbers")
countryddl = driver.find_element_by_class_name('numberchooser-country')
stateddl = driver.find_element_by_class_name('numberchooser-state')
areacodeddl = driver.find_element_by_class_name('numberchooser-city')
ess_month = driver.find_element_by_id('essential-month')
next_btn = driver.find_element_by_class_name('btnessential')





country_sel = S(countryddl)
state_sel = S(stateddl)
area_sel = S(areacodeddl)


country_sel.select_by_index(1)
state_count = state_sel.options
state_sel.select_by_index(random.randint(0, len(state_count)-1))

try:
    areaw = WT(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "numberchooser-city")))
    area_count = area_sel.options
    area_sel.select_by_index(random.randint(1, len(area_count)-1))
except Exception as e:
    print "AREA CODE TRIGGER: {}".format(e)

try:
    ess_monthw = WT(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "essential-month")))
    ess_month.click()
except Exception as e:
    print "ESSENTIAL MONTH TRIGGER {}".format(e)

try:
    nextstp = WT(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btnessential")))
    next_btn.click()
except Exception as e:
    print "NEXT BUTTON TRIGGER {}".format(e)



try:
    driver.get("https://qaorigin.metrofax.com/buy-now/account-setup")
    wfe = WT(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "email")))
    email_input = driver.find_element_by_class_name('email')
    email_input.send_keys(fake.email())
    to_biling_btn = driver.find_element_by_id('sf_dyno-2')
    to_biling_btn.click()
except Exception as e:
    print "EMAIL INPUT ISSUE {}".format(e)


try:
    driver.get("https://qaorigin.metrofax.com/Buy-Now/Billing-Info")
    fname = driver.find_element_by_class_name("firstname")
    lname = driver.find_element_by_class_name('lastname')
    cname = driver.find_element_by_class_name('companyName')
except Exception as e:
    print "BILLING ERROR: {}".format(e)
