import requests
import json
from helpers import Generate
from data import Url
import allure


class ApiRequests:

    def __init__(self):
        self.response = None


class ApiRequestsCourier(ApiRequests):

    @allure.step('Регистрируем нового курьера и возвращаем его логин, пароль, имя')
    def register_new_courier_and_return_login_password(self):
        login_pass = []

        login = Generate.generate_random_string()
        password = Generate.generate_random_string()
        first_name = Generate.generate_random_string()

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        self.response = requests.post(f'{Url.url}/{Url.api_courier}', data=payload)

        if self.response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

            return login_pass

    @allure.step('Регистрируем нового курьера с произвольными данными')
    def register_new_courier_with_data(self, login=None, password=None, first_name=None):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        self.response = requests.post(f'{Url.url}/{Url.api_courier}', data=payload)

    @allure.step('Авторизуем курьера и возвращаем его ID')
    def login_courier_and_return_courier_id(self):
        login, password, first_name = self.register_new_courier_and_return_login_password()
        payload = {
            "login": login,
            "password": password
        }
        self.response = requests.post(f'{Url.url}/{Url.api_courier}/login', data=payload)
        courier_id = self.response.json()["id"]

        return courier_id

    @allure.step('Авторизуем курьера с произвольными данными')
    def login_courier_with_data(self, login=None, password=None):
        payload = {
            "login": login,
            "password": password
        }
        self.response = requests.post(f'{Url.url}/{Url.api_courier}/login', data=payload)

    @allure.step('Получаем список заказов по ID курьера')
    def get_order_list_by_courier_id(self):
        courier_id = self.login_courier_and_return_courier_id()
        self.response = requests.get(f'{Url.url}/{Url.api_orders}?courierId={courier_id}')

    @allure.step('Удаляем аккаунт курьера по его ID')
    def delete_courier_by_courier_id(self):
        courier_id = self.login_courier_and_return_courier_id()
        self.response = requests.delete(f'{Url.url}/{Url.api_courier}/{courier_id}')

    @allure.step('Удаляем аккаунт курьера с произвольными данными')
    def delete_courier_with_data(self, id=None):
        payload = {'courierId': id}
        self.response = requests.delete(f'{Url.url}/{Url.api_courier}', data=payload)


class ApiRequestsOrder(ApiRequests):

    @allure.step('Создаём новый заказ')
    def create_new_order(self, color=None):
        payload = Generate.generate_order_data(color)
        payload_string = json.dumps(payload)
        self.response = requests.post(f'{Url.url}/{Url.api_orders}', data=payload_string)

    @allure.step('Создаём новый заказ и получаем его ID по трек-номеру')
    def get_order_id(self, color=None):
        payload = self.create_new_order(color)
        payload_string = json.dumps(payload)
        self.response = requests.post(f'{Url.url}/{Url.api_orders}', data=payload_string)
        track_num = self.response.json()["track"]

        self.response = requests.get(f'{Url.url}/{Url.api_orders}/track?t={track_num}')
        order_id = self.response.json()["order"]["id"]

        return order_id

    @allure.step('Получаем ID заказа по трек-номеру с произвольными данными')
    def get_order_with_data(self, track_num=""):
        self.response = requests.get(f'{Url.url}/{Url.api_orders}/track?t={track_num}')


class ApiRequestsCourierOrder(ApiRequestsCourier, ApiRequestsOrder):

    @allure.step('Принимаем заказ по его ID и ID курьера')
    def courier_take_order(self):
        courier_id = self.login_courier_and_return_courier_id()
        order_id = self.get_order_id()

        self.response = requests.put(f'{Url.url}/{Url.api_orders}/accept/{order_id}?courierId={courier_id}')

        return order_id

    @allure.step('Принимаем заказ по его ID и ID курьера с произвольными данными')
    def courier_take_order_with_data(self, order_id=None, courier_id=""):
        if order_id:
            self.response = requests.put(f'{Url.url}/{Url.api_orders}/accept/{order_id}?courierId={courier_id}')
        else:
            self.response = requests.put(f'{Url.url}/{Url.api_orders}/accept/courierId={courier_id}')
