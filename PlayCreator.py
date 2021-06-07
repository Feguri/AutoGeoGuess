from selenium import webdriver
import time
import os


class PlayCreator:
    def __init__(self):
        self.path = r'C:\Users\Acer\Desktop\Development\chromedriver.exe'

        self.email = os.environ['EMAIL']  # Your Email/Username goes here
        self.password = os.environ['PASSWORD']  # Your password goes here

    def go_play(self):
        driver = webdriver.Chrome(executable_path=self.path)

        driver.get('https://www.geoguessr.com/')

        login = driver.find_element_by_css_selector('.header__item.header__item--no-margin.header__item--sign-in a')
        login.click()

        time.sleep(5)
        email_entry = driver.find_element_by_css_selector('.form-field__field input')
        email_entry.send_keys(self.email)

        password_entry = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div/div/'
                                                      'div/form/div/div[2]/div[2]/input')
        password_entry.send_keys(self.password)

        login_button = driver.find_element_by_css_selector('.button.button--medium.button--primary')
        login_button.click()

        time.sleep(5)
        play_btn = driver.find_element_by_css_selector('.button.button--medium.button--primary')
        play_btn.click()
        time.sleep(5)
        play_again = driver.find_element_by_css_selector('.button.button--medium.button--primary'
                                                         '.confirmation-dialog__action')
        play_again.click()
        time.sleep(5)
        start_game = driver.find_element_by_css_selector('.button.button--medium.button--primary')
        start_game.click()
        time.sleep(5)
