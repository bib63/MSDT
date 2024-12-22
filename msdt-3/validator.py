"""
Валидация данных
"""

# Проверка регулярки
from re import match


patterns = {
    "http_status_message" : r"^[1-5]\d{2}\s[A-Za-z]",
    "email"               : r"^\w+@\w+(\.\w+)+$",
    "passport"            : r"^\d{2}\s\d{2}\s\d{6}$",
    "snils"               : r"^\d{11}$",
    "ipv4"                : (
                                (r"^(([0-9]|[1-9][0-9]|1[0-9]"
                                r"{2}|2[0-4][0-9]|25[0-5])\.){3}"
                                r"([09]|[1-9][0-9]|1[0-9]{2}|2[0-4]"
                                r"[0-9]|25[0-5])$")
                            ),
    "hex_color"           : r"^#[\dA-Fa-f]{6}$",
    "isbn"                : r"(^\d{3}-)?\d-\d{5}-\d{3}-\d$",
    "time"                : (r"^([0-1][0-9]|[2][0-3]):[0-5][0-9]"
                            r":[0-5][0-9]\.[0-9]{6}$"),
    "longitude"           : r"^[(\-\d)\d]\d*\.\d*$",
    "locale_code"         : r"^[A-Za-z]+(\-[A-Za-z]+)*$",
}

class Validator:
    """
    Класс для сопоставления паттерна и регулярного варажения
    """

    def __init__(self):
        pass

    def validate_data(self, regex_pattern: str, input_data: str) -> bool:
        if regex_pattern not in patterns:
            return False

        return match(patterns[regex_pattern], input_data) is not None
