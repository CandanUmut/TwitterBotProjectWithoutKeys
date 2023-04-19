from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openai
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
TWITTER_EMAIL = "YOUREMAILHERE"
TWITTER_PASSWORD = "YOURPASSWORDHERE"
openai.api_key = "YOUR OPENAI API KEY HERE"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def generate_tweet(self):
        prompt = "Generate a tweet 130 characters long about important topics for our world and Languages"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=(prompt),
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        answer = response["choices"][0]["text"]
        # Correct grammar and word usage
        return answer

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)

        email = self.driver.find_element(By.XPATH, "//input[@autocomplete='username']")
        # password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        time.sleep(3)
        nextButton = self.driver.find_element(By.XPATH, "//span[text()='Next']")
        nextButton.click()

        time.sleep(3)
        password = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "password"))
        )

        password.send_keys(TWITTER_PASSWORD)

        time.sleep(3)

        password.send_keys(Keys.ENTER)

        time.sleep(2)

        tweet1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']"))
        )

        tweet_text = self.generate_tweet()
        time.sleep(10)
        tweet1.send_keys(tweet_text + " https://www.ailingual.org")

        time.sleep(10)

        tweetleButton = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Tweetle']")))

        tweetleButton.click()

        time.sleep(3)

        # time.sleep(2)
        # password.send_keys(Keys.ENTER)
        # time.sleep(5)
        # tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        # tweet = self.generate_tweet()
        # tweet_compose.send_keys(tweet)
        # time.sleep(3)
        # tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        # tweet_button.click()
        # time.sleep(2)
        # self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

while True:
    bot.tweet_at_provider()
    time.sleep(3600)  # sleep for 1 hour