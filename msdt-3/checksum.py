"""
В этом модуле обитают функции, необходимые
для автоматизированной проверки результатов ваших трудов.
"""

import json
import hashlib
from typing import List

# работа с cvs в dict формате
from csv import DictReader

# валидация данных
from validator import Validator

validator = Validator()

def get_list(csv: str):
    """Получить список строк где есть хотя-бы одно поле с ошибкой

    Принимаем csv как путь к файлу

    возвращаем список строк numbers_with_mistakes

    """
    numbers_with_mistakes = []

    with open(csv, newline="", encoding="utf-16") as csv_file:
        dict_reader = DictReader(csv_file, delimiter=";")
        for row_num, row in enumerate(dict_reader):
            for pattern, data in row.items():
                if not validator.validate_data(pattern, data):
                    numbers_with_mistakes.append(row_num - 1)

    return numbers_with_mistakes


def calculate_checksum(row_numbers: List[int]) -> str:
    """
    Вычисляет md5 хеш от списка целочисленных значений.

    ВНИМАНИЕ, ВАЖНО! Чтобы сумма получилась корректной, считать, что первая
    строка с данными csv-файла имеет номер 0
    Другими словами: В исходном csv 1я строка - заголовки столбцов,
    2я и остальные - данные.
    Соответственно, считаем что у 2 строки файла номер 0, у 3й - номер
    1 и так далее.

    :param row_numbers: список целочисленных номеров строк csv-файла,
    на которых были найдены ошибки валидации
    :return: md5 хеш для проверки через github action
    """
    row_numbers.sort()
    return hashlib.md5(json.dumps(row_numbers).encode("utf-8")).hexdigest()


def serialize_result(variant: int, checksum: str) -> None:
    """
    Метод для сериализации результатов лабораторной пишите сами.
    Вам нужно заполнить данными - номером варианта и контрольной суммой - файл,
    лежащий в папке с лабораторной.
    Файл называется, очевидно, result.json.

    ВНИМАНИЕ, ВАЖНО! На json натравлен github action, который проверяет
    корректность выполнения лабораторной.
    Так что не перемещайте, не переименовывайте и не изменяйте его структуру,
    если планируете успешно сдать лабу.

    :param variant: номер вашего варианта
    :param checksum: контрольная сумма, вычисленная через calculate_checksum()
    """
    result = {"variant": variant, "checksum": checksum}
    with open("result.json", "w", encoding="utf-8") as json_file:
        json.dump(result, json_file)


def main():
    numbers_with_mistakes = get_list("89.csv")
    print(len(numbers_with_mistakes))
    check_sum = calculate_checksum(numbers_with_mistakes)
    serialize_result(89, check_sum)


if __name__ == "__main__":
    main()
