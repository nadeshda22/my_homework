"""pеализуйте класс для главной страницы Гугл,
в который впишите:
локаторы: поле ввода, кнопки "Google search" и "I'm feeling lucky" (зависят от языка - "Поиск в Гугл" и "Мне повезёт!")
метод для перехода на главную страницу поисковика Гугл
методы для клика по кнопкам "Google search" и "I'm feeling lucky"
метод для ввода значения "yahoo search"
метод для проверки, что текущая страница == главная страница поисковика гугл"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageGoogle:

    button_google_search = (By.NAME,"btnK")
    button_lucky = (By.NAME,"btnI")
    input_label = (By.NAME, "q")


    def __init__(self,driver: WebDriver):
        self.driver = driver

    def load_page_google(self):
        self.driver.get("https://www.google.com/?hl=ru")

    def click_button_google_search(self):
        self.driver.find_element(*self.button_google_search).click()

    def click_button_lucky(self):
        self.driver.find_element(*self.button_lucky).click()

    def input_text_in_label(self):
        self.driver.find_element(*self.input_label).send_keys('yahoo search')

    def is_on_google_main_page(self):
        return self.driver.current_url.startswith("https://www.google.com")