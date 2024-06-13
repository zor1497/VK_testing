from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import NoSuchElementException


class BasePage:
    # LOCATORS
    BASKET_LINK = ("xpath", "//a[@data-test='shopping-cart-link']")
    BURGER_OPEN_MENU_BUTTON = ("id", "react-burger-menu-btn")
    BURGER_CLOSED_MENU_BUTTON = ("id", "react-burger-cross-btn")
    INVENTORY_SIDEBAR_LINK = ("id", "inventory_sidebar_link")
    ABOUT_SIDEBAR_LINK = ("id", "about_sidebar_link")
    LOGOUT_SIDEBAR_LINK = ("id", "logout_sidebar_link")
    RESET_SIDEBAR_LINK = ("id", "reset_sidebar_link")
    TITLE = ("xpath", "//span[@data-test='title']")

    # CONSTRUCTOR
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 5)
        self.action = ActionChains(browser)
        self.base_url = "https://www.saucedemo.com/"

    # BASE_ACTIONS
    def find_element(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            return "Элемент не найден"

    def find_elements(self, locator):
        try:
            elements = self.wait.until(EC.visibility_of_all_elements_located(locator))
            return elements
        except TimeoutException:
            return []

    def get_current_url(self):
        return self.browser.current_url

    # ACTIONS
    @allure.step("Открытие страницы корзины")
    def open_basket(self):
        basket_link = self.find_element(self.BASKET_LINK)
        basket_link.click()
        assert self.get_current_url() == "https://www.saucedemo.com/cart.html"

    @allure.step("Открытие бокового меню")
    def open_sidebar(self):
        self.find_element(self.BURGER_OPEN_MENU_BUTTON).click()
        assert self.find_element(self.BURGER_CLOSED_MENU_BUTTON).get_attribute("tabindex") == "0"

    @allure.step("Закрытие бокового меню")
    def close_sidebar(self):
        self.find_element(self.BURGER_CLOSED_MENU_BUTTON).click()
        assert self.find_element(self.BURGER_CLOSED_MENU_BUTTON).get_attribute("tabindex") == "-1"

    @allure.step("Нажатие на ссылку 'Logout'")
    def click_on_logout_link(self):
        self.find_element(self.LOGOUT_SIDEBAR_LINK).click()
        with allure.step("Проверка открытия страницы авторизации"):
            assert self.get_current_url() == "https://www.saucedemo.com/"





