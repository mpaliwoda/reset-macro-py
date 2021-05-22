import sys

from src.models.game_state import GameState
from src.services.key_presses.base_key_presser import BaseKeyPresser
from src.services.world_name_generators.base_world_name_generator import BaseWorldNameGenerator


class WorldCreationMixin_1_14:
    key_presser: BaseKeyPresser
    world_name_generator: BaseWorldNameGenerator
    game_state: GameState

    _NAME_WORLD_OFFSET: int = 1

    def name_world(self) -> None:
        self.key_presser.press("tab")
        select_all_hotkey = ("ctrl", "a") if sys.platform != "darwin" else ("command", "a")
        self.key_presser.press_key_combination(*select_all_hotkey)
        self.key_presser.press("backspace")
        self.key_presser.write(self.world_name_generator.generate_new_world_name(major_version=1.14))
        self.game_state.world_creation_screen_offset = self._NAME_WORLD_OFFSET

    def single_player_menu(self) -> None:
        self.key_presser.press("tab")
        self.key_presser.press("enter")

    def create_new_world_menu(self) -> None:
        self.key_presser.press("tab", times=4)
        self.key_presser.press("enter")

    def start_new_world(self) -> None:
        self.key_presser.press("tab", times=(4 - self.game_state.world_creation_screen_offset))
        self.key_presser.press("enter")
        self.game_state.world_creation_screen_offset = 0
