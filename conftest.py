import pytest
from api_requests import ApiRequestsCourier, ApiRequestsOrder, ApiRequestsCourierOrder


@pytest.fixture
def new_courier():
    try:
        new_courier = ApiRequestsCourier()

        yield new_courier

    finally:
        new_courier.delete_courier_by_courier_id()
        del new_courier

@pytest.fixture
def new_order():
    try:
        new_order = ApiRequestsOrder()

        yield new_order

    finally:
        new_order.cancel_order()
        del new_order

@pytest.fixture
def courier_order():
    try:
        courier_order = ApiRequestsCourierOrder()

        yield courier_order

    finally:
        courier_order.delete_courier_by_courier_id()
        courier_order.cancel_order()
        del courier_order
