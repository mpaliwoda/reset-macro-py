import logging

from src.services.actions.base_action import BaseAction
from src.services.actions.mixins.pause_menu_mixin_post_1_14 import PauseMenuMixinPost_1_14

logger = logging.getLogger(__name__)


class ExitWorldPost_1_14(BaseAction, PauseMenuMixinPost_1_14):
    def perform(self) -> None:
        logger.info("Exiting world")
        self.pause_game()
        self.save_and_quit_to_title()
