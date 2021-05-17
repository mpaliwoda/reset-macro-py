from src.services.key_presses.base_key_presser import BaseKeyPresser


class WorldCreationMixin_1_16:
    key_presser: BaseKeyPresser
    current_world_creation_screen_offset: int

    _SELECT_DIFFICULTY_OFFSET: int = 2
    _MORE_WORLD_OPTIONS_OFFSET: int = 6
    _GAMEMODE_SELECTION_OFFSET: int = 1
    _ALLOW_CHEATS_OFFSET: int = 3

    def single_player_menu(self) -> None:
        self.key_presser.press("tab")
        self.key_presser.press("enter")

    def create_new_world_menu(self) -> None:
        self.key_presser.press("tab", times=3)
        self.key_presser.press("enter")

    def start_new_world(self) -> None:
        self.key_presser.press("tab", times=(7 - self._current_world_creation_screen_offset))
        self.key_presser.press("enter")

    def select_easy_diff(self) -> None:
        self.key_presser.press("tab", times=2)
        self.key_presser.press("enter", times=3)
        self._current_world_creation_screen_offset = self._SELECT_DIFFICULTY_OFFSET

    def more_world_options(self) -> None:
        self.key_presser.press("tab", times=(6 - self._current_world_creation_screen_offset))
        self.key_presser.press("enter")

    def exit_more_world_options(self) -> None:
        self.key_presser.press("tab", times=5)
        self.key_presser.press("enter")
        self._current_world_creation_screen_offset = self._MORE_WORLD_OPTIONS_OFFSET
