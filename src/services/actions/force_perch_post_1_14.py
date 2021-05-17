import logging

from simpleconf import config
from src.services.actions.base_action import BaseAction
from src.services.actions.mixins.pause_menu_mixin_post_1_14 import PauseMenuMixinPost_1_14


logger = logging.getLogger(__name__)


class ForcePerchPost_1_14(BaseAction, PauseMenuMixinPost_1_14):
    FORCE_PERCH_COMMAND: str = r"/data merge entity @e[type=ender_dragon,limit=1] {DragonPhase:2}"

    def enter_force_perch_command(self) -> None:
        self.key_presser.press(config.enter_chat_key)
        self.key_presser.write(self.FORCE_PERCH_COMMAND, delay_in_ms=(0 if config.write_text_instantly else None))
        self.key_presser.press("enter")

    def perform(self) -> None:
        logger.info("Forcing perch")
        self.pause_game()
        self.open_to_lan(allow_cheats=True)
        self.enter_force_perch_command()
