import allure
from allure_commons.types import Severity

from dipa.start_page import StartPage


@allure.tag('StartPage')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AlterAyrol")
@allure.epic('Тестирование стартовой страницы')
@allure.story("Проверяет переключение текста на английский")
def test_check_english_switch():

    ru_text = 'О продукте'
    eng_text = 'Our product'

    start = StartPage()
    start.open_page('')
    start.check_our_product_text(ru_text)
    start.click_on_eng()
    start.check_our_product_text(eng_text)


@allure.tag('StartPage')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AlterAyrol")
@allure.epic('Тестирование стартовой страницы')
@allure.story("Проверяет переключение текста на русский после английского")
def test_check_ru_switch_test():

    ru_text = 'О продукте'
    eng_text = 'Our product'

    start = StartPage()
    start.open_page('')
    start.check_our_product_text(ru_text)
    start.click_on_eng()
    start.check_our_product_text(eng_text)
    start.click_on_ru()
    start.check_our_product_text(ru_text)


@allure.tag('StartPage')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AlterAyrol")
@allure.epic('Тестирование стартовой страницы')
@allure.story("Проверяет правильность указанного адреса")
def test_check_contact_information():
    info = 'Москва, ул.Тверская, д.18, корп.1, офис 615'

    start = StartPage()
    start.open_page('')
    start.click_on_contacts_button()
    start.check_contacts_info(info)


@allure.tag('StartPage')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AlterAyrol")
@allure.epic('Тестирование стартовой страницы')
@allure.story("Проверяет подтверждающий текст после отправки сообщения из контактов")
def test_send_empty_message():
    text = 'Вы отправили нам пустое сообщение. Пожалуйста заполните форму полностью'

    start = StartPage()
    start.open_page('')
    start.click_on_contacts_button()
    start.click_send_message_button()
    start.check_our_product_text(text)


@allure.tag('StartPage')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AlterAyrol")
@allure.epic('Тестирование стартовой страницы')
@allure.story("Проверяет подтверждающий текст после отправки заявки на расчёт стоимости")
def test_check_cost_calculator():
    text = 'Спасибо Вам за сообщение'

    start = StartPage()
    start.open_page('')
    start.click_find_price_button()
    start.click_calculate_price_submit_button()
    start.check_calculate_cost_confirm_text(text)


