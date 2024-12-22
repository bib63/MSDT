from product import Product
from exceptions import (
    ProductNotFoundError, InvalidQuantityError,
    ShelfNotFoundError, OutOfStockError
)


def create_order(product_id, quantity):
    # Проверка корректности количества продукции
    if quantity <= 0:
        raise InvalidQuantityError("Указано некорректное количество продукции.")

    # Создание заказа
    order_id = 1  # Заглушка для простоты примера
    print(f"Создан заказ {order_id} на продукцию {product_id} в количестве {quantity}.")
    return order_id


def process_order(order_id):
    # Обработка заказа
    shelf_ids = [1, 2]  # Заглушка для простоты примера
    print(f"Заказ {order_id} обработан и распределен на лавки {shelf_ids}.")
    return shelf_ids


def place_product(shelf_id, product_id, quantity):
    # Проверка наличия лавки
    if shelf_id not in [1, 2]:
        raise ShelfNotFoundError("Лавка с указанным идентификатором не найдена.")

    # Размещение продукции на лавке
    print(f"Продукция {product_id} в количестве {quantity} размещена на лавке {shelf_id}.")


def purchase_product(shelf_id, product_id, quantity):
    # Проверка наличия лавки
    if shelf_id not in [1, 2]:
        raise ShelfNotFoundError("Лавка с указанным идентификатором не найдена.")

    # Проверка наличия продукции на лавке
    if quantity > 10:  # Заглушка для простоты примера
        raise OutOfStockError("Продукция отсутствует в наличии на данной лавке.")

    # Покупка продукции
    print(f"Продукция {product_id} в количестве {quantity} куплена с лавки {shelf_id}.")


def get_product_info(product_id):
    # Получение информации о продукции
    products = [
        Product(1, "Товар 1", 100),
        Product(2, "Товар 2", 200),
        Product(3, "Товар 3", 300),
    ]
    product = next((p for p in products if p.id == product_id), None)
    if product is None:
        raise ProductNotFoundError("Продукция с указанным идентификатором не найдена.")
    print(f"Получена информация о продукции {product_id}: {product}")
    return product

def main():
    try:
        # Создание заказа
        order_id = create_order(1, 10)

        # Обработка заказа
        shelf_ids = process_order(order_id)

        # Размещение продукции на лавках
        for shelf_id in shelf_ids:
            place_product(shelf_id, 1, 5)

        # Покупка продукции с лавки
        purchase_product(1, 1, 3)

    except ProductNotFoundError as e:
        print("Произошла ошибка:", e)
    except InvalidQuantityError as e:
        print("Произошла ошибка:", e)
    except ShelfNotFoundError as e:
        print("Произошла ошибка:", e)
    except OutOfStockError as e:
        print("Произошла ошибка:", e)


if __name__ == '__main__':
    main()