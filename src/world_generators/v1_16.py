import logging

from simpleconf import config
from src.services.key_presses.keyboard_key_presser import KeyboardKeyPresser
from src.world_generators.base_world_generator import BaseWorldGenerator

logger = logging.getLogger(__name__)


class WorldGenerator_1_16(BaseWorldGenerator):
    _SELECT_DIFFICULTY_OFFSET: int = 2
    _MORE_WORLD_OPTIONS_OFFSET = 6
    _GAMEMODE_SELECTION_OFFSET = 1
    _ALLOW_CHEATS_OFFSET = 3

    def __init__(self) -> None:
        self._world_creation_screen_offset: int = 0
        self.key_presser = KeyboardKeyPresser(delay_in_miliseconds=config.key_delay_in_miliseconds)

    def single_player_menu(self) -> None:
        self.key_presser.press("tab")
        self.key_presser.press("enter")

    def create_new_world_menu(self) -> None:
        self.key_presser.press("tab", times=3)
        self.key_presser.press("enter")

    def start_new_world(self) -> None:
        self.key_presser.press("tab", times=(7 - self._world_creation_screen_offset))
        self.key_presser.press("enter")

    def select_easy_diff(self) -> None:
        self.key_presser.press("tab", times=2)
        self.key_presser.press("enter", times=3)
        self._world_creation_screen_offset = self._SELECT_DIFFICULTY_OFFSET

    def more_world_options(self) -> None:
        self.key_presser.press("tab", times=(6 - self._world_creation_screen_offset))
        self.key_presser.press("enter")

    def exit_more_world_options(self) -> None:
        self.key_presser.press("tab", times=5)
        self.key_presser.press("enter")
        self._world_creation_screen_offset = self._MORE_WORLD_OPTIONS_OFFSET


class RSGGenerator(WorldGenerator_1_16):
    def generate_world(self) -> None:
        logger.info("Generating new 1.16 RSG world")
        self.single_player_menu()
        self.create_new_world_menu()
        self.select_easy_diff()
        self.start_new_world()


class SSGGenerator(WorldGenerator_1_16):
    SEED: str = "2483313382402348964"

    def input_seed(self) -> None:
        self.key_presser.press("tab", times=3)
        self.key_presser.write(self.SEED)

    def generate_world(self) -> None:
        logger.info("Generating new 1.16 SSG world")
        self.single_player_menu()
        self.create_new_world_menu()
        self.select_easy_diff()
        self.more_world_options()
        self.input_seed()
        self.exit_more_world_options()
        self.start_new_world()
