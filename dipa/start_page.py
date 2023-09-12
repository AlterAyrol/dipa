import allure
from selene import browser
from selene import be, have


class StartPage:

    def __init__(self):
        self.browser = browser

    '''locators'''

    ru_locator = '//a[@href="/"]'
    eng_locator = '//a[@href="/eng.html"]'
    our_product_locator = '//a[@href="#about"]'
    contacts_button_locator = '//a[@href="#contacts"]'
    contacts_info_locator = '#contacts'
    demo_container_locator = '//div[@id="demo"]//button[@type="submit"]'
    find_price_button_locator = '//a[@href="#price"]'
    calculate_cost_button_locator = '//a[@href="#price"]'
    price_container_locator = '#price'
    calculate_cost_form_submit_locator = '//button[@type="submit"]'
    calculate_cost_confirm_text_locator = 'h1'




    '''Actions'''

    @allure.step('Открывает страницу')
    def open_page(self, url):
        self.browser.open(url)

    @allure.step('Нажимает на переключение на русский язык')
    def click_on_ru(self):
        browser.element(self.ru_locator).click()

    @allure.step('Нажимает на переключение на английский язык')
    def click_on_eng(self):
        browser.element(self.eng_locator).click()

    @allure.step('Проверяет правильность в названии кнопки "О продукте"')
    def check_our_product_text(self, text):
        browser.element(self.our_product_locator).should(have.text(text))

    @allure.step('Нажимает кнопку "Контакты"')
    def click_on_contacts_button(self):
        browser.element(self.contacts_button_locator).click()

    @allure.step('Проверяет инофрмацию в контактах')
    def check_contacts_info(self, text):
        browser.element(self.contacts_info_locator).should(have.text(text))

    @allure.step('Нажимает на кнопку подтвердить в контактах')
    def click_send_message_button(self):
        browser.element(self.demo_container_locator).click()

    @allure.step('Проверяет текст после отправки сообщения')
    def check_send_message_is_true(self, text):
        browser.element('body').should(have.text(text))

    @allure.step('Нажимает кнопку "Узнать цену"')
    def click_find_price_button(self):
        browser.element(self.find_price_button_locator).click()

    @allure.step('Нажимает кнопку "Расчитать стоимость"')
    def click_calculate_price_submit_button(self):
        browser.element(self.price_container_locator).element(self.calculate_cost_form_submit_locator).click()

    @allure.step('Проверяет текст подтверждение расчёта стоимости')
    def check_calculate_cost_confirm_text(self, text):
        browser.element(self.calculate_cost_confirm_text_locator).should(have.text(text))
