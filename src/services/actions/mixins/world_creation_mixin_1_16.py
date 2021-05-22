from src.models.game_state import GameState
from src.services.key_presses.base_key_presser import BaseKeyPresser


class WorldCreationMixin_1_16:
    key_presser: BaseKeyPresser
    game_state: GameState

    _SELECT_DIFFICULTY_OFFSET: int = 2
    _MORE_WORLD_OPTIONS_OFFSET: int = 6

    def single_player_menu(self) -> None:
        self.key_presser.press("tab")
        self.key_presser.press("enter")

    def create_new_world_menu(self) -> None:
        self.key_presser.press("tab", times=3)
        self.key_presser.press("enter")

    def start_new_world(self) -> None:
        self.key_presser.press("tab", times=(7 - self.game_state.world_creation_screen_offset))
        self.key_presser.press("enter")
        self.game_state.world_creation_screen_offset = 0

    def select_easy_diff(self) -> None:
        self.key_presser.press("tab", times=2)
        self.key_presser.press("enter", times=3)
        self.game_state.world_creation_screen_offset = self._SELECT_DIFFICULTY_OFFSET

    def more_world_options(self) -> None:
        self.key_presser.press("tab", times=(6 - self.game_state.world_creation_screen_offset))
        self.key_presser.press("enter")

    def exit_more_world_options(self) -> None:
        self.key_presser.press("tab", times=5)
        self.key_presser.press("enter")
        self.game_state.world_creation_screen_offset = self._MORE_WORLD_OPTIONS_OFFSET

    def set_seed_field(self) -> None:
        self.key_presser.press("tab", times=3)
