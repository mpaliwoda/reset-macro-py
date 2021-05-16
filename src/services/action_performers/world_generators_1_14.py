import logging

from simpleconf import config
from src.services.action_performers.base_world_generator import BaseWorldGenerator
from src.services.key_presses.keyboard_key_presser import KeyboardKeyPresser

logger = logging.getLogger(__name__)


class RSGGenerator(BaseWorldGenerator):
    def __init__(self) -> None:
        self.key_presser = KeyboardKeyPresser(delay_in_miliseconds=config.key_delay_in_miliseconds)

    def single_player_menu(self) -> None:
        self.key_presser.press("tab")
        self.key_presser.press("enter")

    def create_new_world_menu(self) -> None:
        self.key_presser.press("tab", times=4)
        self.key_presser.press("enter")

    def start_new_world(self) -> None:
        self.key_presser.press("tab", times=4)
        self.key_presser.press("enter")

    def perform_action(self) -> None:
        logger.info("Generating new 1.14 RSG world")
        self.single_player_menu()
        self.create_new_world_menu()
        self.start_new_world()
