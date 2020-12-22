from selenium import webdriver
from selenium.webdriver.common import keys
from time import sleep
PROMISE_DOWN = 150
PROMISE_UP = 10

TWITTER_ACCOUNT = ""
TWITTER_PASSWORD = ""
Chrome_driver_path= r"C:\Users\14014\Desktop\100 days of code course Jupiter note book files\Web development topics\Chrome driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=Chrome_driver_path)


class InternetSpeedTwitterBot:

    def __init__(self, Chrome_driver_path):
        self.driver = webdriver.Chrome(executable_path=Chrome_driver_path)
        self.up = 0
        self.down = 0


    def get_internet(self):
        self.driver.get("https://www.speedtest.net/")
        Go_botton = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        Go_botton.click()
        sleep(2)
        self.down = driver.find_element_by_class_name('')
        self.up= driver.find_element_by_class_name('result-data-large number result-data-value upload-speed')

    def twitter_at_provider(self):
        self.driver.get("https://twitter.com/?lang=es")
        sleep(3)
        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[1]/div/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[2]/div/label/div/div[2]/div/input')
        email.send_keys(TWITTER_ACCOUNT)
        password.send_keys(TWITTER_PASSWORD)
        sleep(3)
        password.send_keys(keys.ENTER)
        sleep(3)
        tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        sleep(3)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        sleep(2)
        self.driver.quit()




Bot = InternetSpeedTwitterBot(Chrome_driver_path)
Bot.get_internet()
Bot.twitter_at_provider()