from typing import NamedTuple, Union

class Settings(NamedTuple):
    token: str
    chat_id: Union[int, str]