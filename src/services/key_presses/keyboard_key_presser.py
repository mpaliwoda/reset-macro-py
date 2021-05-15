import logging
import time

import keyboard
from src.services.key_presses.base_key_presser import BaseKeyPresser

logger = logging.getLogger(__name__)


class KeyboardKeyPresser(BaseKeyPresser):
    def press(self, key: str, times: int = 1) -> None:
        for _ in range(times):
            keyboard.send(key)
            time.sleep(self.delay)

    def write(self, sequence: str, instant: bool = True) -> None:
        keyboard.write(sequence, delay=(0 if instant else self.delay))
