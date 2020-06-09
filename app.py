from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox(executable_path = '/Users/tigranmuradyan/downloads/geckodriver')

    def login(self):
        bot = self.bot
        bot.get('https://instagram.com/')
        time.sleep(3)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(10)
        bot.find_element_by_class_name('y3zKF').click()

    def search(self, input):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/'+input+'/')
        time.sleep(3)
        posts = bot.find_elements_by_class_name("eLAPa")
        for post in posts:
            post.click()
            follow = bot.find_element_by_class_name('bY2yH')
            follow.click()
            time.sleep(4)
            bot.find_element_by_class_name('TxciK').click()

tigran = InstaBot('usr', 'pwd')
tigran.login()
tigran.search('hayastan')