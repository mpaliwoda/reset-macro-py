import abc

from src.services.action_performers.base_action_performer import BaseActionPerformer


class BaseWorldGenerator(BaseActionPerformer):
    @abc.abstractmethod
    def single_player_menu(self) -> None:
        pass

    @abc.abstractmethod
    def create_new_world_menu(self) -> None:
        pass

    @abc.abstractmethod
    def start_new_world(self) -> None:
        pass
