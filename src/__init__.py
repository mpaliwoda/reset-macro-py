import logging.config
import sys

import keyboard
from simpleconf import config

from src.models.game_state import GameState
from src.services.action_selector import ActionSelector
from src.services.hotkey_registrator import HotkeyRegistrator
from src.services.key_presser_selector import KeyPresserSelector
from src.services.window_manager_selector import WindowManagerSelector


class Macro:
    def __init__(self) -> None:
        self.load_config()
        self.init_logging()

        self.game_state = GameState(opened_to_lan=False, world_creation_screen_offset=0)
        self.action_selector = ActionSelector()
        self.window_manager = WindowManagerSelector().select_window_manager()
        self.key_presser = KeyPresserSelector().select_key_presser()
        self.key_presser.set_standard_delay(config.key_delay_in_miliseconds)

    def run(self) -> None:
        hotkey_registrator = HotkeyRegistrator(self)
        hotkey_registrator.register_hotkeys()
        keyboard.wait()

    def load_config(self) -> None:
        config._load("config.ini")

        if sys.platform == "win32":
            config._use("default", "windows")
        elif sys.platform == "linux":
            config._use("default", "linux")
        elif sys.platform == "darwin":
            config._use("default", "macos")

    def init_logging(self) -> None:
        logging.config.fileConfig(config.logging_config)
