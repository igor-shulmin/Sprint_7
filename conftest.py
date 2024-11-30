import pytest
from helpers import GenerateNewCourier, GenerateNewOrder, CourierOrder

@pytest.fixture
def new_courier():
    new_courier = GenerateNewCourier()

    return new_courier

@pytest.fixture
def new_order():
    new_order = GenerateNewOrder()

    return new_order

@pytest.fixture
def courier_order():
    courier_order = CourierOrder()

    return courier_order
