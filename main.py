import logging.config
import sys

import keyboard
from simpleconf import config
from src.models.exceptions import UnsupportedPlatformError
from src.services import hotkey_registrator
from src.services.mc_window_managers.dummy_window_manager import DummyWindowManager
from src.services.mc_window_managers.base_window_manager import BaseWindowManager


def _select_correct_window_manager() -> BaseWindowManager:
    if not config.check_minecraft_window_before_running_hotkey:
        return DummyWindowManager()

    if sys.platform == "win32":
        from src.services.mc_window_managers.windows_window_manager import WindowsWindowManager

        return WindowsWindowManager()
    elif sys.platform == "linux":
        from src.services.mc_window_managers.x11_window_manager import X11WindowManager

        return X11WindowManager()
    elif sys.platform == "darwin":
        from src.services.mc_window_managers.darwin_window_manager import DarwinWindowManager

        return DarwinWindowManager()
    else:
        # if not any of those 3, the program will already have thrown an exception
        pass


if __name__ == "__main__":
    config._load("config.ini")

    if sys.platform == "win32":
        config._use("default", "windows")
    elif sys.platform == "linux":
        config._use("default", "linux")
    elif sys.platform == "darwin":
        config.use("default", "macos")
    else:
        raise UnsupportedPlatformError(f"Platform {sys.platform} is not supported")

    logging.config.fileConfig(config.logging_config)
    logger = logging.getLogger(__name__)

    logger.info("Starting macro. Press %s or ctrl+c to exit", config.exit_macro_hotkey)
    logger.info("Using the delay of %s miliseconds", config.key_delay_in_miliseconds)

    window_manager = _select_correct_window_manager()
    logger.debug("Using fetcher: %s", window_manager)

    logger.info("Registering hotkeys...")
    hotkey_registrator.register_hotkeys(window_manager)
    keyboard.wait()
