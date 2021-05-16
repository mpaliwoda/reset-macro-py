import abc
import logging
import sys
import time

from simpleconf import config
from src.services.key_presses.keyboard_key_presser import KeyboardKeyPresser

logger = logging.getLogger(__name__)


class BaseWorldExiter(abc.ABC):
    @abc.abstractmethod
    def pause_game(self) -> None:
        pass

    @abc.abstractmethod
    def save_and_quit_to_title(self) -> None:
        pass

    @abc.abstractmethod
    def exit_world(self) -> None:
        pass


class WorldExiter(BaseWorldExiter):
    _DELAY_UNTIL_ESC_IS_PRESSED_ON_WINDOWS: float = 0.5

    def __init__(self) -> None:
        self.key_presser = KeyboardKeyPresser(delay_in_miliseconds=0)

    def pause_game(self) -> None:
        # give time to release ctrl, otherwise acts like super key was pressed on Windows
        if sys.platform == "win32" and "ctrl" in config.exit_world_hotkey.casefold():
            time.sleep(self._DELAY_UNTIL_ESC_IS_PRESSED_ON_WINDOWS)

        self.key_presser.press("esc")

    def save_and_quit_to_title(self) -> None:
        self.key_presser.press("tab", times=8)
        self.key_presser.press("enter")

    def exit_world(self) -> None:
        logger.info("Exiting world")
        self.pause_game()
        self.save_and_quit_to_title()
