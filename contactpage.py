from BaseApp import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
import logging
import time


class ContactPageLocators:
    LOCATOR_TITLE_PAGE = (By.XPATH, '//*[@id="app"]/main/div/div/h1')
    LOCATOR_YOUR_NAME = (By.XPATH, '//*[@id="contact"]/div[1]/label/input')
    LOCATOR_YOUR_EMAIL = (By.XPATH, '//*[@id="contact"]/div[2]/label/input')
    LOCATOR_CONTENT = (By.XPATH, '//*[@id="contact"]/div[3]/label/span/textarea')
    LOCATOR_BTN = (By.XPATH, '//*[@id="contact"]/div[4]/button')
    LOCATOR_EMAIL_LABEL = (By.XPATH, '//*[@id="contact"]/div[2]/label/span')


class OperationsContactUsHelper(BasePage):
    def open_contact_us_page(self):
        self.go_to_site('https://test-stand.gb.ru/contact')

    def fill_contact_us(self, your_name=None, your_email=None, content=None):
        logging.info(f'Fill contact us form : {your_name} {your_email} {content}')

        if your_name:
            time.sleep(1)
            your_name_elem = self.find_element(ContactPageLocators.LOCATOR_YOUR_NAME)
            logging.info(f'Fill your name {your_name}')
            your_name_elem.send_keys(your_name)

        if your_email:
            time.sleep(1)
            your_email_elem = self.find_element(ContactPageLocators.LOCATOR_YOUR_EMAIL)
            logging.info(f'Fill your email {your_email}')
            your_email_elem.send_keys(your_email)

        if content:
            time.sleep(1)
            content_elem = self.find_element(ContactPageLocators.LOCATOR_CONTENT)
            logging.info(f'Fill content {content}')
            content_elem.send_keys(content)

        time.sleep(1)
        self.find_element(ContactPageLocators.LOCATOR_BTN).click()

    def get_alert_msg(self, wait_time):
        alert = WebDriverWait(self.driver, wait_time).until(EC.alert_is_present(), message=f"Can't find alert")
        msg = alert.text
        alert.accept()
        return msg

    def check_alert_not_present(self, wait_time):
        try:
            WebDriverWait(self.driver, wait_time).until(EC.alert_is_present(), message=f"Can't find alert")
            return False
        except (NoAlertPresentException, TimeoutException):
            return True

    def check_email_label_red(self):
        email_label_color = self.get_element_property(ContactPageLocators.LOCATOR_EMAIL_LABEL, "color")
        return "rgba(183, 28, 28, 1)" == email_label_color
