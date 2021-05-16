import abc

from src.services.action_performers.base_action_performer import BaseActionPerformer


class BaseWorldExiter(BaseActionPerformer):
    @abc.abstractmethod
    def pause_game(self) -> None:
        pass

    @abc.abstractmethod
    def save_and_quit_to_title(self) -> None:
        pass
