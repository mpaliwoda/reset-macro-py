import abc
from typing import Optional

MILISECONDS_IN_SECOND: int = 1000


class BaseKeyPresser(abc.ABC):
    def __init__(self, delay_in_ms: int = 0) -> None:
        self.standard_delay = delay_in_ms / MILISECONDS_IN_SECOND

    @abc.abstractmethod
    def press(self, key: str, times: int = 1, delay_in_ms: Optional[int] = None) -> None:
        pass

    @abc.abstractmethod
    def write(self, sequence: str, delay_in_ms: Optional[int] = None) -> None:
        pass

    @abc.abstractmethod
    def press_key_combination(self, *keys: str) -> None:
        pass

    def set_standard_delay(self, delay_in_ms: int) -> None:
        self.standard_delay = delay_in_ms / MILISECONDS_IN_SECOND
