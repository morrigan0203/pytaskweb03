from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import time


class AddPostLocators:
    LOCATOR_ADD_POST = (By.XPATH, '//*[@id="create-btn"]')
    '//*[@id="create-btn"]'
    LOCATOR_POST_TITLE = (By.XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label/input')
    LOCATOR_POST_DESCR = (By.XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea')
    LOCATOR_POST_CONTENT = (By.XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea')
    LOCATOR_POST_CREATE_BTN = (By.XPATH, '//*[@id="create-item"]/div/div/div[7]/div/button')
    LOCATOR_TITLE_NEW_POST = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')


class OperationsAddPost(BasePage):
    def add_post(self):
        logging.info("Add post")
        time.sleep(1)
        add_pos_btn = self.find_element(AddPostLocators.LOCATOR_ADD_POST)
        add_pos_btn.click()

    def post_content(self, title=None, description=None, content=None):
        logging.info(f'Fill post {title} {description} {content}')

        if title:
            time.sleep(1)
            title_elem = self.find_element(AddPostLocators.LOCATOR_POST_TITLE)
            logging.info(f'Fill title {title}')
            title_elem.send_keys(title)

        if description:
            time.sleep(1)
            description_elem = self.find_element(AddPostLocators.LOCATOR_POST_DESCR)
            logging.info(f'Fill description {description}')
            description_elem.send_keys(description)

        if content:
            time.sleep(1)
            content_elem = self.find_element(AddPostLocators.LOCATOR_POST_CONTENT)
            logging.info(f'Fill content {content}')
            content_elem.send_keys(content)

        time.sleep(1)
        self.find_element(AddPostLocators.LOCATOR_POST_CREATE_BTN).click()

    def find_post(self):
        logging.info("Checking new post")
        time.sleep(1)
        return self.find_element(AddPostLocators.LOCATOR_TITLE_NEW_POST).text

