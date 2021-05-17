import pyautogui
from src.services.key_presses.base_key_presser import BaseKeyPresser
from typing import Optional


class PyautoguiKeyPresser(BaseKeyPresser):
    def press(self, key: str, times: int = 1, delay_in_ms: Optional[int] = None) -> None:
        pyautogui.press(key, presses=times, interval=(delay_in_ms if delay_in_ms is not None else self.standard_delay))

    def write(self, sequence: str, delay_in_ms: Optional[int] = None) -> None:
        pyautogui.write(sequence, interval=(delay_in_ms if delay_in_ms is not None else self.standard_delay))
