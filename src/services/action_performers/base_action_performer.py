import abc


class BaseActionPerformer(abc.ABC):
    @abc.abstractmethod
    def perform_action(self) -> None:
        pass
