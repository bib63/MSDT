import pytest
from main import (
    create_order, process_order,
    place_product, purchase_product,
    get_product_info
)
from exceptions import (
    ProductNotFoundError,
    InvalidQuantityError,
    ShelfNotFoundError,
    OutOfStockError
)


@pytest.mark.parametrize(
    "quantity, expected_exception",
    [
        (0, InvalidQuantityError),
        (-1, InvalidQuantityError),
        (1, None),
        (10, None)
    ]
)
def test_create_order_invalid_quantity(quantity, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            create_order(1, quantity)
    else:
        order_id = create_order(1, quantity)
        assert isinstance(order_id, int)


@pytest.mark.parametrize(
    "shelf_id, product_id, quantity, expected_exception",
    [
        (1, 1, 5, None),
        (2, 1, 5, None),
        (3, 1, 5, ShelfNotFoundError),
    ]
)
def test_place_product(shelf_id, product_id, quantity, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            place_product(shelf_id, product_id, quantity)
    else:
        place_product(shelf_id, product_id, quantity)


def test_get_product_info():
    product = get_product_info(1)
    assert product.id == 1
    assert product.name == "Товар 1"
    assert product.price == 100

    with pytest.raises(ProductNotFoundError):
        get_product_info(4)

def test_process_order():
    order_id = 1
    shelf_ids = process_order(order_id)
    assert isinstance(shelf_ids, list)
    assert len(shelf_ids) == 2
    assert shelf_ids == [1, 2]

@pytest.mark.parametrize(
    "shelf_id, product_id, quantity, expected_exception",
    [
        (1, 1, 3, None),
        (1, 1, 11, OutOfStockError),
        (3, 1, 3, ShelfNotFoundError)
    ]
)
def test_purchase_product(shelf_id, product_id, quantity, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            purchase_product(shelf_id, product_id, quantity)
    else:
        purchase_product(shelf_id, product_id, quantity)