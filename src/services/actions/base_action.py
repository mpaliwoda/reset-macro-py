import abc

from src.models.game_state import GameState


class BaseAction(abc.ABC):
    def __init__(self, game_state: GameState) -> None:
        self.game_state = game_state

    @abc.abstractmethod
    def perform(self) -> None:
        pass
