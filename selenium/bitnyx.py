import sys
import datetime
import schedule
import pickle
import time

from selenium import webdriver

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException

LOGIN = sys.argv[1]
PASSWORD = sys.argv[2]


def job():

    driver = webdriver.Firefox()

    driver.get("https://bitnyx.com")

    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("password")

    email.send_keys(LOGIN)
    password.send_keys(PASSWORD)

    driver.find_element_by_xpath("//button[@type='submit']").click()

    try:
        driver.find_element_by_id("claim-button").click()
        t = driver.current_url
        pickle.dump(t, open('noreal', 'wb'))
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


schedule.every(0).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

'''
import ipdb; ipdb.set_trace()
driver.implicitly_wait(5)
driver.set_page_load_timeout(5)
'''
