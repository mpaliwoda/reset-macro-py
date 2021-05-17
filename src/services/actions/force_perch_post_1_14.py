from simpleconf import config
from src.models.game_state import GameState
from src.services.actions.base_action import BaseAction
from src.services.actions.mixins.pause_menu_mixin_post_1_14 import PauseMenuMixinPost_1_14
from src.services.key_presses.base_key_presser import BaseKeyPresser


class ForcePerchPost_1_14(BaseAction, PauseMenuMixinPost_1_14):
    FORCE_PERCH_COMMAND: str = r"/data merge entity @e[type=ender_dragon,limit=1] {DragonPhase:2}"

    def __init__(self, game_state: GameState, key_presser: BaseKeyPresser) -> None:
        self.game_state = game_state
        self.key_presser = key_presser

    def enter_force_perch_command(self) -> None:
        self.key_presser.press(config.enter_chat_key)
        self.key_presser.write(self.FORCE_PERCH_COMMAND, instant=config.write_text_instantly)
        self.key_presser.press("enter")

    def perform(self) -> None:
        self.pause_game()
        self.open_to_lan(allow_cheats=True)
        self.enter_force_perch_command()
