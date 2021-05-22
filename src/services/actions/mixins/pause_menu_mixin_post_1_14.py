from src.models.game_state import GameState
from src.services.key_presses.base_key_presser import BaseKeyPresser


class PauseMenuMixinPost_1_14:
    key_presser: BaseKeyPresser
    game_state: GameState

    def pause_game(self) -> None:
        self.key_presser.press("esc", delay_in_ms=0)

    def open_to_lan(self, allow_cheats: bool) -> None:
        self.key_presser.press("tab", times=7)
        self.key_presser.press("enter")

        if allow_cheats:
            self.key_presser.press("tab", times=4)
            self.key_presser.press("enter")

        self.key_presser.press("tab")
        self.key_presser.press("enter")
        self.game_state.opened_to_lan = True

    def save_and_quit_to_title(self) -> None:
        self.key_presser.press("tab", times=(8 if not self.game_state.opened_to_lan else 7), delay_in_ms=0)
        self.key_presser.press("enter", delay_in_ms=0)
        self.game_state.opened_to_lan = False
