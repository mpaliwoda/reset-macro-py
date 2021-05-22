import sys

from src.services.key_presses.base_key_presser import BaseKeyPresser


class KeyPresserSelector:
    def select_key_presser(self) -> BaseKeyPresser:
        if sys.platform == "win32":
            from src.services.key_presses.keyboard_key_presser import KeyboardKeyPresser

            return KeyboardKeyPresser()
        else:
            from src.services.key_presses.pyautogui_key_presser import PyautoguiKeyPresser

            return PyautoguiKeyPresser()
