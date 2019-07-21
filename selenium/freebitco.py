import re, csv, sys
from time import sleep, time
from random import uniform, randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from webdriver_manager.chrome import ChromeDriverManager

LOGIN = sys.argv[1]
PASSWORD = sys.argv[2]


def write_stat(loops, time):
    with open('stat.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([loops, time])       
    
def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
    
def wait_between(a,b):
    rand=uniform(a, b) 
    sleep(rand)
 
def dimention(driver): 
    d = int(driver.find_element_by_xpath('//div[@id="rc-imageselect-target"]/table').get_attribute("class")[-1]);
    return d if d else 3  # dimention is 3 by default
    
# ***** main procedure to identify and submit picture solution  
def solve_images(driver):   
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID ,"rc-imageselect-target"))
        )       
    dim = dimention(driver) 
    # ****************** check if there is a clicked tile ******************
    if check_exists_by_xpath('//div[@id="rc-imageselect-target"]/table/tbody/tr/td[@class="rc-imageselect-tileselected"]'):
        rand2 = 0
    else:  
        rand2 = 1 

    # wait before click on tiles    
    wait_between(0.5, 1.0)       
    # ****************** click on a tile ****************** 
    tile1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH ,   '//div[@id="rc-imageselect-target"]/table/tbody/tr[{0}]/td[{1}]'.format(randint(1, dim), randint(1, dim )))) 
        )   
    tile1.click() 
    if (rand2):
        try:
            driver.find_element_by_xpath('//div[@id="rc-imageselect-target"]/table/tbody/tr[{0}]/td[{1}]'.format(randint(1, dim), randint(1, dim))).click()
        except NoSuchElementException:                  
            print('\n\r No Such Element Exception for finding 2nd tile')
   
     
    #****************** click on submit buttion ****************** 
    driver.find_element_by_id("recaptcha-verify-button").click()

start = time()
url='https://freebitco.in/?op=signup_page'
driver = webdriver.Firefox()
driver.get(url)

driver.find_element_by_css_selector(".login_menu_button").click()

sleep(1)

driver.find_element_by_css_selector(".pushpad_deny_button").click()

email = driver.find_element_by_id("login_form_btc_address")
password = driver.find_element_by_id("login_form_password")

email.send_keys(LOGIN)
password.send_keys(PASSWORD)

driver.find_element_by_id("login_button").click()

sleep(5)
mainWin = driver.current_window_handle

# move the driver to the first iFrame 
driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])

# *************  locate CheckBox  **************
CheckBox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID ,"recaptcha-anchor"))
        ) 

# *************  click CheckBox  ***************
wait_between(0.5, 0.7)  
# making click on captcha CheckBox 
CheckBox.click() 
sleep(2)
#***************** back to main window **************************************
driver.switch_to_window(mainWin)

wait_between(2.0, 2.5) 
#import ipdb; ipdb.set_trace()
# ************ switch to the second iframe by tag name ******************
driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[1])
i=1
while i<130:
    print('\n\r{0}-th loop'.format(i))
    # ******** check if checkbox is checked at the 1st frame ***********
    driver.switch_to_window(mainWin)   
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME , 'iframe'))
        )  
    wait_between(1.0, 2.0)
    if check_exists_by_xpath('//span[@aria-checked="true"]'): 
        import winsound
        winsound.Beep(400,1500)
        write_stat(i, round(time()-start) - 1 ) # saving results into stat file
        break 
        
    driver.switch_to_window(mainWin)   
    # ********** To the second frame to solve pictures *************
    wait_between(0.3, 1.5) 
    driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[1]) 
    solve_images(driver)
    i=i+1

'''
https://stackoverflow.com/questions/44187909/python-selenium-and-captcha
import ipdb; ipdb.set_trace()
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
'''
