from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

"""
pip freeze > requirements.txt  -> to save all the import
pip install -r requirements.txt  -> to get all the import
"""

FollowedStars = ["therock","kyliejenner","stephencurry30","jillianmercado","goodamerican","cristiano","leomessi","arianagrande","kimkardashian","beyonce","khloekardashian","justinbieber"]
chrome_driver_path = 'path/to/chromedriver'
driver = webdriver.Chrome(chrome_driver_path)
time.sleep(3)





def Rand(x=0):
    if x == 1:
        number = random.randint(4, 6)
    elif x == 2:
        number = random.randint(6, 15)
    elif x == 3:
        number = random.randint(15, 30)
    elif x == 4:
        number = random.randint(60, 120)
    else:
        number = 3
    print("Time to wait: ",number)
    return number


class Bot:

    def __init__(self):
#ofirmagen94@gmail.com

        self.username = 'add here'
        self.password = 'add here'

    def login(self):
        print("FUNC start: login")
        driver.get('https://www.instagram.com')
        time.sleep(Rand())
    # Connect to the USER
        connect = driver.find_element(By.NAME, 'username')
        connect.send_keys(self.username)
        time.sleep(Rand())
        connect = driver.find_element(By.NAME, 'password')
        connect.send_keys(self.password)
        time.sleep(Rand())
        connect.send_keys(Keys.RETURN)
        time.sleep(Rand(2))

    # Closed the pop ups
        try:
            save_info_to_log_in = driver.find_element(By.XPATH,"//div[contains(@class, 'x1i10hfl') and contains(text(), 'Not Now')]")
            save_info_to_log_in.click()
            time.sleep(Rand(1))

        except Exception:
            print("Exception on click: save_info_to_log_in")
        time.sleep(Rand())

        try:
            Turn_on_Notifications_Off= driver.find_element(By.XPATH,"//button[text()='Not Now']")
            Turn_on_Notifications_Off.click()
            time.sleep(Rand(1))

        except Exception:
            print("Exception on click: Turn_on_Notifications_Off")
        time.sleep(Rand())


    def follow(self):
        # Follow the user
        print("FUNC start: follow")
        for NameStar in FollowedStars:
            time.sleep(Rand(3))
            driver.get(f'https://www.instagram.com/{NameStar}/')
            time.sleep(Rand(2))
            try:

                click_on_follow = driver.find_element(By.XPATH, '//button[@class="_acan _acap _acas _aj1-"]')
                click_on_follow.send_keys(Keys.RETURN)
                time.sleep(Rand(1))


            except Exception:
                print("Exception on click follow")
        time.sleep(Rand(2))

    def unfollow(self):
        # Unfollow the user
        print("FUNC start: unfollow")
        for NameStar in  FollowedStars:
            time.sleep(Rand(3))
            driver.get(f'https://www.instagram.com/{NameStar}/')
            time.sleep(Rand(2))




            try:
                click_on_main_follow = driver.find_element(By.XPATH, '//button[@class="_acan _acap _acat _aj1-"]')
                click_on_main_follow.send_keys(Keys.RETURN)
            except:
                print("Exception on open the window for unfollow")
            time.sleep(Rand(2))
            try:

                click_on_follow_or_unfollow = driver.find_element(By.XPATH,
                                                               "//div[@role='dialog']//span[text()='Unfollow']/../../../../../../../..")

                click_on_follow_or_unfollow.send_keys(Keys.RETURN)
            except:
                print("Exception on click unfollow")

        time.sleep(Rand(2))







    def AutoLiker(self):
        print("FUNC start: AutoLiker")
        try:
            driver.get('https://www.instagram.com')
            time.sleep(Rand())
            open_explore = driver.find_element(By.XPATH, '//a[@href="/explore/"]')
            open_explore.click()
        except Exception:
            print("explor not works")


        for i in range(0,Rand(2)):
            try:
                time.sleep(Rand(2))
                open_the_pic = driver.find_elements(By.XPATH, '//div[@class=" _al5u"]/div/a')
                open_the_pic[i].click()
                time.sleep(Rand(1))
            except:
                print("Exception: not get in to the pic")

            try:
                click_like = driver.find_element(By.XPATH,'//span[@class="_aamw"]')
                click_like.click()
                time.sleep(Rand(1))
            except:
                print("Exception: not make like")

            try:
                closed = driver.find_element(By.XPATH,'//div[@class="x160vmok x10l6tqk x1eu8d0j x1vjfegm"]/div')
                closed.click()
                time.sleep(Rand(1))
            except:
                print("Exception: not closed the pic")
        time.sleep(Rand(2))

if __name__ == '__main__':
    x=Bot()
    x.login()





    while True:
        x.follow()
        x.AutoLiker()
        x.unfollow()




