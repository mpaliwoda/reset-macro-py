import sys

from simpleconf import config

from src.services.key_presses.base_key_presser import BaseKeyPresser


class KeyPresserSelector:
    def select_key_presser(self) -> BaseKeyPresser:
        if sys.platform == "win32":
            from src.services.key_presses.keyboard_key_presser import KeyboardKeyPresser

            return KeyboardKeyPresser(delay_in_ms=config.key_delay_in_miliseconds)
        else:
            from src.services.key_presses.pyautogui_key_presser import PyautoguiKeyPresser

            return PyautoguiKeyPresser(delay_in_ms=config.key_delay_in_miliseconds)
