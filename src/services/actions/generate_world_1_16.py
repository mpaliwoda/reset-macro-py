import logging

from src.services.actions.mixins.world_creation_mixin_1_16 import WorldCreationMixin_1_16
from src.services.actions.base_action import BaseAction
from src.services.key_presses.base_key_presser import BaseKeyPresser

logger = logging.getLogger(__name__)


class GenerateRSGWorld_1_16(BaseAction, WorldCreationMixin_1_16):
    def __init__(self, key_presser: BaseKeyPresser) -> None:
        self.key_presser = key_presser
        self.current_world_creation_screen_offset = 0

    def perform(self) -> None:
        logger.info("Generating new 1.16 RSG world")
        self.single_player_menu()
        self.create_new_world_menu()
        self.select_easy_diff()
        self.start_new_world()


class GenerateSSGWorld_1_16(BaseAction, WorldCreationMixin_1_16):
    SEED: str = "2483313382402348964"

    def __init__(self, key_presser: BaseKeyPresser) -> None:
        self.key_presser = key_presser
        self.current_world_creation_screen_offset = 0

    def input_seed(self) -> None:
        self.key_presser.press("tab", times=3)
        self.key_presser.write(self.SEED)

    def perform(self) -> None:
        logger.info("Generating new 1.16 SSG world")
        self.single_player_menu()
        self.create_new_world_menu()
        self.select_easy_diff()
        self.more_world_options()
        self.input_seed()
        self.exit_more_world_options()
        self.start_new_world()
