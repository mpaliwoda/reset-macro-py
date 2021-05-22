import logging
import sys
from typing import Tuple

from src.services.actions.base_action import BaseAction
from src.services.actions.mixins.world_creation_mixin_1_16 import WorldCreationMixin_1_16

logger = logging.getLogger(__name__)


class GenerateRSGWorld_1_16(BaseAction, WorldCreationMixin_1_16):
    def perform(self) -> None:
        logger.info("Generating new 1.16 RSG world")
        self.single_player_menu()
        self.create_new_world_menu()
        self.select_easy_diff()
        self.start_new_world()


class GenerateSSGWorld_1_16(BaseAction, WorldCreationMixin_1_16):
    SSG_SEED: str = "2483313382402348964"

    def input_seed(self) -> None:
        self.key_presser.write(self.SSG_SEED, delay_in_ms=0)

    def perform(self) -> None:
        logger.info("Generating new 1.16 SSG world")
        self.single_player_menu()
        self.create_new_world_menu()
        self.select_easy_diff()
        self.more_world_options()
        self.set_seed_field()
        self.input_seed()
        self.exit_more_world_options()
        self.start_new_world()


class GenerateFSGWorld_1_16(BaseAction, WorldCreationMixin_1_16):
    def input_seed(self) -> None:
        self.key_presser.press_key_combination(*self._paste_from_clipboard_hotkey())

    def perform(self) -> None:
        logger.info("Generating new 1.16 FSG world using seed from clipboard")
        self.single_player_menu()
        self.create_new_world_menu()
        self.select_easy_diff()
        self.more_world_options()
        self.set_seed_field()
        self.input_seed()
        self.exit_more_world_options()
        self.start_new_world()

    def _paste_from_clipboard_hotkey(self) -> Tuple[str, ...]:
        base = "ctrl" if sys.platform != "darwin" else "command"
        return base, "v"
