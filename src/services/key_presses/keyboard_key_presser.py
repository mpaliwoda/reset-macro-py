import time
from typing import Optional, Tuple

import keyboard

from src.services.key_presses.base_key_presser import BaseKeyPresser


class KeyboardKeyPresser(BaseKeyPresser):
    def press(self, key: str, times: int = 1, delay_in_ms: Optional[int] = None) -> None:
        for _ in range(times):
            keyboard.send(key)
            time.sleep(delay_in_ms if delay_in_ms is not None else self.standard_delay)

    def write(self, sequence: str, delay_in_ms: Optional[int] = None) -> None:
        keyboard.write(sequence, delay=delay_in_ms if delay_in_ms is not None else self.standard_delay)

    def press_key_combination(self, *keys: Tuple[str, ...]) -> None:
        keyboard.send("+".join(*keys))
