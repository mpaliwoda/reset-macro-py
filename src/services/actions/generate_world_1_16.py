import logging
import sys
from typing import Tuple

from simpleconf import config

from src.services.actions.base_action import BaseAction
from src.services.actions.mixins.world_creation_mixin_1_16 import WorldCreationMixin_1_16
from src.services.world_name_generator_selector import WorldNameGeneratorSelector

logger = logging.getLogger(__name__)


class GenerateRSGWorld_1_16(BaseAction, WorldCreationMixin_1_16):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.world_name_generator = WorldNameGeneratorSelector().select_world_name_generator()

    def perform(self) -> None:
        logger.info("Generating new 1.16 RSG world")
        self.single_player_menu()
        self.create_new_world_menu()
        if config.name_worlds:
            self.name_world()
        self.select_difficulty()
        self.start_new_world()


class GenerateSSGWorld_1_16(BaseAction, WorldCreationMixin_1_16):
    SSG_SEED: str = "2483313382402348964"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.world_name_generator = WorldNameGeneratorSelector().select_world_name_generator()

    def input_seed(self) -> None:
        self.key_presser.write(self.SSG_SEED, delay_in_ms=0)

    def perform(self) -> None:
        logger.info("Generating new 1.16 SSG world")
        self.single_player_menu()
        self.create_new_world_menu()
        self.select_difficulty()
        self.more_world_options()
        self.set_seed_field()
        self.input_seed()
        self.exit_more_world_options()
        self.start_new_world()


class GenerateFSGWorld_1_16(BaseAction, WorldCreationMixin_1_16):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.world_name_generator = WorldNameGeneratorSelector().select_world_name_generator()

    def input_seed(self) -> None:
        self.key_presser.press_key_combination(*self._paste_from_clipboard_hotkey())

    def perform(self) -> None:
        logger.info("Generating new 1.16 FSG world using seed from clipboard")
        self.single_player_menu()
        self.create_new_world_menu()
        self.select_difficulty()
        self.more_world_options()
        self.set_seed_field()
        self.input_seed()
        self.exit_more_world_options()
        self.start_new_world()

    def _paste_from_clipboard_hotkey(self) -> Tuple[str, ...]:
        base = "ctrl" if sys.platform != "darwin" else "command"
        return base, "v"
