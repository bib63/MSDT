import asyncio
from product import Product
from exceptions import (
    ProductNotFoundError, InvalidQuantityError,
    ShelfNotFoundError, OutOfStockError
)
from loguru import logger

async def create_order(product_id, quantity):
    if quantity <= 0:
        raise InvalidQuantityError("Указано некорректное количество продукции.")
    order_id = 1  # Заглушка для простоты примера
    logger.info(f"Создан заказ {order_id} на {product_id} в количестве {quantity}.")
    return order_id


async def process_order(order_id):
    shelf_ids = [1, 2]  # Заглушка для простоты примера
    logger.info(f"Заказ {order_id} обработан и распределен на лавки {shelf_ids}.")
    return shelf_ids


async def place_product(shelf_id, product_id, quantity):
    if shelf_id not in [1, 2]:
        raise ShelfNotFoundError("Лавка с указанным идентификатором не найдена.")
    logger.info(f"Продукция {product_id} в количестве {quantity} размещена на лавке {shelf_id}.")


async def purchase_product(shelf_id, product_id, quantity):
    if shelf_id not in [1, 2]:
        raise ShelfNotFoundError("Лавка с указанным идентификатором не найдена.")
    if quantity > 10:  # Заглушка для простоты примера
        raise OutOfStockError("Продукция отсутствует в наличии на данной лавке.")
    logger.info(f"Продукция {product_id} в количестве {quantity} куплена с лавки {shelf_id}.")


async def get_product_info(product_id):
    products = [
        Product(1, "Товар 1", 100),
        Product(2, "Товар 2", 200),
        Product(3, "Товар 3", 300),
    ]
    product = next((p for p in products if p.id == product_id), None)
    if product is None:
        raise ProductNotFoundError("Продукция с указанным идентификатором не найдена.")
    logger.info(f"Получена информация о продукции {product_id}: {product}")
    return product


async def main():
    logger.add(
        'logs/log.txt',
        format='{time}---{level}---{message}',
        rotation='10:00',
        retention='3 day',
        compression='zip',
        level='DEBUG'
    )
    try:
        order_id = await create_order(1, 10)
        shelf_ids = await process_order(order_id)
        for shelf_id in shelf_ids:
            await place_product(shelf_id, 1, 5)
        await purchase_product(1, 1, 3)
        await get_product_info(1)

    except (ProductNotFoundError, InvalidQuantityError, ShelfNotFoundError, OutOfStockError) as e:
        logger.exception(f"Произошла ошибка: {e}")
    except Exception as e:
        logger.exception(f"Произошла внезапная ошибка: {e}")


if __name__ == '__main__':
    asyncio.run(main())