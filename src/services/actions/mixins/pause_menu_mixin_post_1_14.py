import sys
import time

from simpleconf import config
from src.services.key_presses.base_key_presser import BaseKeyPresser


class PauseMenuMixinPost_1_14:
    key_presser: BaseKeyPresser

    def pause_game(self) -> None:
        # give time to release ctrl, otherwise acts like super key was pressed on Windows
        if sys.platform == "win32" and "ctrl" in config.exit_world_hotkey.casefold():
            time.sleep(self._DELAY_UNTIL_ESC_IS_PRESSED_ON_WINDOWS)
        self.key_presser.press("esc")

    def save_and_quit_to_title(self) -> None:
        self.key_presser.press("tab", times=8)
        self.key_presser.press("enter")
