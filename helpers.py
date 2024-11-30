import requests
import random
import string
import json
from data import Url


class Generate:

    def __init__(self):
        self.response = None

    def generate_random_string(self, length=10):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))

        return random_string


class GenerateNewCourier(Generate):

    def register_new_courier_and_return_login_password(self):
        login_pass = []

        login = self.generate_random_string()
        password = self.generate_random_string()
        first_name = self.generate_random_string()

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        self.response = requests.post(f'{Url.url}/api/v1/courier', data=payload)

        if self.response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

            return login_pass

    def register_new_courier_with_data(self, login=None, password=None, first_name=None):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        self.response = requests.post(f'{Url.url}/api/v1/courier', data=payload)

    def login_courier_and_return_courier_id(self):
        login, password, first_name = self.register_new_courier_and_return_login_password()
        payload = {
            "login": login,
            "password": password
        }
        self.response = requests.post(f'{Url.url}/api/v1/courier/login', data=payload)
        courier_id = self.response.json()["id"]

        return courier_id

    def login_courier_with_data(self, login=None, password=None):
        payload = {
            "login": login,
            "password": password
        }
        self.response = requests.post(f'{Url.url}/api/v1/courier/login', data=payload)

    def get_order_list_by_courier_id(self):
        courier_id = self.login_courier_and_return_courier_id()
        self.response = requests.get(f'{Url.url}/api/v1/orders?courierId={courier_id}')

    def delete_courier_by_courier_id(self):
        courier_id = self.login_courier_and_return_courier_id()
        self.response = requests.delete(f'{Url.url}/api/v1/courier/{courier_id}')

    def delete_courier_with_data(self, id=None):
        payload = {'courierId': id}
        self.response = requests.delete(f'{Url.url}/api/v1/courier', data=payload)


class GenerateNewOrder(Generate):

    def __init__(self):
        self.name = self.generate_random_string()
        self.surname = self.generate_random_string()
        self.address = 'г. Москва, ' + random.choice(
            ['ул. Тверская, 44, кв. 100', 'ул. Арбат, 100, кв. 44', 'ул. Варварка, 200, кв. 144'])
        self.station = random.choice(['Лужники', 'Митино', 'ВДНХ', 'Лихоборы', 'Театральная'])
        self.telephone = int('89' + ''.join([random.choice(list('1234567890')) for num in range(9)]))
        self.date = '2020-06-06'
        self.rental_period = random.choice(
            ['сутки', 'двое суток', 'трое суток', 'четверо суток', 'пятеро суток', 'шестеро суток', 'семеро суток'])
        self.comment = random.choice(['Код домофона: 123', 'Домофон не работает', 'Просьба доставить после 18:00'])

    def create_new_order(self, color=None):
        payload = {
            "firstName": self.name,
            "lastName": self.surname,
            "address": self.address,
            "metroStation": self.station,
            "phone": self.telephone,
            "rentTime": self.rental_period,
            "deliveryDate": self.date,
            "comment": self.comment,
            "color": color
        }
        payload_string = json.dumps(payload)
        self.response = requests.post(f'{Url.url}/api/v1/orders', data=payload_string)

    def get_order_id(self, color=None):
        payload = self.create_new_order(color)
        payload_string = json.dumps(payload)
        self.response = requests.post(f'{Url.url}/api/v1/orders', data=payload_string)
        track_num = self.response.json()["track"]

        self.response = requests.get(f'{Url.url}/api/v1/orders/track?t={track_num}')
        order_id = self.response.json()["order"]["id"]

        return order_id

    def get_order_with_data(self, track_num=""):
        self.response = requests.get(f'{Url.url}/api/v1/orders/track?t={track_num}')

class CourierOrder(GenerateNewCourier, GenerateNewOrder):

    def courier_take_order(self):
        courier_id = self.login_courier_and_return_courier_id()
        order_id = self.get_order_id()

        self.response = requests.put(f'{Url.url}/api/v1/orders/accept/{order_id}?courierId={courier_id}')

        return order_id

    def courier_take_order_with_data(self, order_id=None, courier_id=""):
        if order_id:
            self.response = requests.put(f'{Url.url}/api/v1/orders/accept/{order_id}?courierId={courier_id}')
        else:
            self.response = requests.put(f'{Url.url}/api/v1/orders/accept/courierId={courier_id}')
