import random
import string
from data import Url, OrderData


class Generate:

    @staticmethod
    def generate_random_string(length=10):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))

        return random_string

    @staticmethod
    def generate_order_data(color):

        return {
                "firstName": Generate.generate_random_string(),
                "lastName": Generate.generate_random_string(),
                "address": 'г. Москва, ' + random.choice(OrderData.streets),
                "metroStation": random.choice(OrderData.stations),
                "phone": int('89' + ''.join([random.choice(list('1234567890')) for _ in range(9)])),
                "rentTime": random.choice(OrderData.rental_periods),
                "deliveryDate": OrderData.order_date,
                "comment": random.choice(OrderData.comments),
                "color": color
        }
