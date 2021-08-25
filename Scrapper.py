from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

option1 = Options()
option1.add_argument("--disable-notifications")

############ edit on only this part ################


#email = "Your Email" 
#password = "Your Password"
#url = "https://www.facebook.com/"
#categories = "[List of categories]"
#cities = "[List of cities]"



driver = webdriver.Chrome('D:/fb scrap/Web scrapping PYTHON/chromedriver',options=option1)
####################################################


driver.maximize_window()
driver.get(url)


driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_name("login").click()
time.sleep(3)


for category in categories:

    for city in cities:
        driver.get(f"https://www.facebook.com/search/pages?q={category}&filters=e30%3D")
        time.sleep(2)

        driver.find_element_by_xpath("//span[text()='Location']").click()
        time.sleep(1)


        driver.find_element_by_xpath("//input[@placeholder='Choose a town or city...']").send_keys(city)
        time.sleep(2)



        if(driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/ul/li[1]/div/div[1]/div/div/div/div/div[2]/div/span/span').text == city):
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/ul/li[1]/div/div[1]/div/div/div/div/div[2]/div/span/span').click()
            time.sleep(2)


            SCROLL_PAUSE_TIME = 3

            # Get scroll height
            last_height = driver.execute_script("return document.body.scrollHeight")

            while True:
                # Scroll down to bottom
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                # Wait to load page
                time.sleep(SCROLL_PAUSE_TIME)

                # Calculate new scroll height and compare with last scroll height
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            links = driver.find_elements_by_xpath('//*[@href]')
            for i in links:
                if(i.get_attribute('href').__contains__('?__tn__=%3C')):
                    print(i.get_attribute('href').replace('?__tn__=%3C','/about').replace('//about','/about'))