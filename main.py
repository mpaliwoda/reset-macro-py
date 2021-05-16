import logging.config
import sys

import keyboard
from simpleconf import config
from src.models.exceptions import UnsupportedPlatformError
from src.services import hotkey_registrator
from src.services.window_title.base_window_title_fetcher import BaseWindowTitleFetcher


def _select_correct_window_title_fetcher() -> BaseWindowTitleFetcher:
    if sys.platform == "win32":
        from src.services.window_title.windows_window_title_fetcher import WindowsWindowTitleFetcher

        return WindowsWindowTitleFetcher()
    elif sys.platform == "linux":
        from src.services.window_title.x11_window_title_fetcher import X11WindowTitleFetcher

        return X11WindowTitleFetcher()
    elif sys.platform == "darwin":
        from src.services.window_title.darwin_window_title_fetcher import DarwinWindowTitleFetcher

        return DarwinWindowTitleFetcher()
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

    window_title_fetcher = _select_correct_window_title_fetcher()
    logger.debug("Using fetcher: %s", window_title_fetcher)

    logger.info("Registering hotkeys...")
    hotkey_registrator.register_hotkeys(window_title_fetcher)
    keyboard.wait()
