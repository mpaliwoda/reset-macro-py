import logging

from src.models.game_state import GameState
from src.services.actions.base_action import BaseAction
from src.services.actions.mixins.pause_menu_mixin_post_1_14 import PauseMenuMixinPost_1_14
from src.services.key_presses.base_key_presser import BaseKeyPresser

logger = logging.getLogger(__name__)


class ExitWorldPost_1_14(BaseAction, PauseMenuMixinPost_1_14):
    def __init__(self, game_state: GameState, key_presser: BaseKeyPresser) -> None:
        self.game_state = game_state
        self.key_presser = key_presser

    def perform(self) -> None:
        logger.info("Exiting world")
        self.pause_game()
        self.save_and_quit_to_title()
