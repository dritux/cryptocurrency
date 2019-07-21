import sys
import datetime

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException

LOGIN = sys.argv[1]
PASSWORD = sys.argv[2]

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://bitnyx.com")

email = driver.find_element_by_id("email")
password = driver.find_element_by_id("password")

email.send_keys(LOGIN)
password.send_keys(PASSWORD)

driver.find_element_by_xpath("//button[@type='submit']").click()

try:
    driver.find_element_by_id("claim-button").click()
    now = datetime.datetime.now()
    print("Claim em: {}".format(now))
    driver.close()
except TimeoutException:
    driver.close()
    print("Timeout")
except NoSuchElementException:
    driver.close()
    print("No such element claim")
except NoSuchWindowException:
    print("Closet window")

'''
import ipdb; ipdb.set_trace()
driver.implicitly_wait(5)
driver.set_page_load_timeout(5)
'''
