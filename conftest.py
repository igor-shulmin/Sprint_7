import pytest
from api_requests import ApiRequestsCourier, ApiRequestsOrder, ApiRequestsCourierOrder


@pytest.fixture
def new_courier():
    try:
        new_courier = ApiRequestsCourier()

        yield new_courier

    finally:
        del new_courier

@pytest.fixture
def new_order():
    try:
        new_order = ApiRequestsOrder()

        yield new_order

    finally:
        del new_order

@pytest.fixture
def courier_order():
    try:
        courier_order = ApiRequestsCourierOrder()

        yield courier_order

    finally:
        del courier_order
