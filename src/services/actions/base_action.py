import abc


class BaseAction(abc.ABC):
    @abc.abstractmethod
    def perform(self) -> None:
        pass
