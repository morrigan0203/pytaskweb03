from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_USERNAME = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    LOCATOR_PASS = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    LOCATOR_BTN_LOGIN = (By.CSS_SELECTOR, 'button')
    LOCATOR_ERR_MSG = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')
    LOCATOR_AUTH_MSG = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[3]/a')


class OperationsHelper(BasePage):
    def enter_username(self, username):
        logging.info(f'Send {username} to element {TestSearchLocators.LOCATOR_USERNAME[1]}')
        username_elem = self.find_element(TestSearchLocators.LOCATOR_USERNAME)
        username_elem.clear()
        username_elem.send_keys(username)

    def enter_pass(self, password):
        logging.info(f'Send {password} to element {TestSearchLocators.LOCATOR_PASS[1]}')
        pass_elem = self.find_element(TestSearchLocators.LOCATOR_PASS)
        pass_elem.clear()
        pass_elem.send_keys(password)

    def click_login_btn(self):
        logging.info(f'Click login button')
        self.find_element(TestSearchLocators.LOCATOR_BTN_LOGIN).click()

    def get_msg(self):
        error_elem = self.find_element(TestSearchLocators.LOCATOR_ERR_MSG, time=3)
        text = error_elem.text
        logging.info(f'We found test {text} in error field {TestSearchLocators.LOCATOR_ERR_MSG[1]}')
        return text

    def get_auth_text(self):
        auth_msg = self.find_element(TestSearchLocators.LOCATOR_AUTH_MSG, time=3)
        text = auth_msg.text
        logging.info(f'We found text {text} in auth field {TestSearchLocators.LOCATOR_AUTH_MSG[1]}')
        return text


