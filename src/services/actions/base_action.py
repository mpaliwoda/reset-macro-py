import abc

from src.models.game_state import GameState
from src.services.key_presses.base_key_presser import BaseKeyPresser


class BaseAction(abc.ABC):
    def __init__(self, key_presser: BaseKeyPresser, game_state: GameState) -> None:
        self.key_presser = key_presser
        self.game_state = game_state

    @abc.abstractmethod
    def perform(self) -> None:
        pass
