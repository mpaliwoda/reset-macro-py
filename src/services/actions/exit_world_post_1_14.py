import logging

from src.services.actions.mixins.pause_menu_mixin_post_1_14 import PauseMenuMixinPost_1_14
from src.services.actions.base_action import BaseAction
from src.services.key_presses.base_key_presser import BaseKeyPresser

logger = logging.getLogger(__name__)


class ExitWorldPost_1_14(BaseAction, PauseMenuMixinPost_1_14):
    _DELAY_UNTIL_ESC_IS_PRESSED_ON_WINDOWS: float = 0.5

    def __init__(self, key_presser: BaseKeyPresser) -> None:
        self.key_presser = key_presser

    def perform(self) -> None:
        logger.info("Exiting world")
        self.pause_game()
        self.save_and_quit_to_title()
