from datetime import time
from operator import itemgetter


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    if 22 > current_time.hour > 6:
        is_dark_theme = False
    else:
        is_dark_theme = True

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True

    if dark_theme_enabled_by_user:
        is_dark_theme = True
    elif not dark_theme_enabled_by_user:
        is_dark_theme = False
    elif dark_theme_enabled_by_user is None:
        if 22 > current_time.hour > 6:
            is_dark_theme = False
        else:
            is_dark_theme = True

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    def get_Olga_from_ginen_list(given_list):
        for user in given_list:
            if user["name"] == "Olga":
                return user

    suitable_users = get_Olga_from_ginen_list(users)
    assert suitable_users == {"name": "Olga", "age": 45}

    def get_all_users_under_20_years_old(given_list):
        result = list()
        for user in given_list:
            if user['age'] < 20:
                result.append(user)
        result.sort(key=lambda user: user["age"])
        return result

    suitable_users = get_all_users_under_20_years_old(users)
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def print_given_func_name_and_attributes(given_func, *args):
    given_func_name = given_func.__name__
    result_func_name = given_func_name.replace('_', ' ').title()
    result_arg_list = list()

    for arg in args:
        result_arg_list.append(arg)

    result = f"{result_func_name} [{', '.join(result_arg_list)}]"
    return result


def open_browser(browser_name):
    actual_result = print_given_func_name_and_attributes(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"
    print(actual_result)


def go_to_companyname_homepage(page_url):
    actual_result = print_given_func_name_and_attributes(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"
    print(actual_result)


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_given_func_name_and_attributes(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
    print(actual_result)
