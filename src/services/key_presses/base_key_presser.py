import abc

MILISECONDS_IN_SECOND: int = 1000


class BaseKeyPresser(abc.ABC):
    def __init__(self, delay_in_miliseconds: int) -> None:
        self.delay = delay_in_miliseconds / MILISECONDS_IN_SECOND

    @abc.abstractmethod
    def press(self, key: str, times: int = 1) -> None:
        pass

    @abc.abstractmethod
    def write(self, sequence: str, instant: bool = True) -> None:
        pass
