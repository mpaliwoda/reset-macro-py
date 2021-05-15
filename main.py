import logging.config
import sys

import keyboard
from src import config
from src.models.exceptions import UnsupportedPlatformError
from src.services import hotkey_registrator
from src.services.window_title.base_window_title_fetcher import BaseWindowTitleFetcher

logging.config.fileConfig(config.LOGGING_CONFIG)
logger = logging.getLogger(__name__)


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
        raise UnsupportedPlatformError(f"Platform: {sys.platform} is not supported.")


if __name__ == "__main__":
    logger.info("Starting macro. Press %s or ctrl+c to exit", config.EXIT_MACRO_HOTKEY)
    logger.info("Using the delay of %s miliseconds", config.KEY_DELAY_IN_MILISECONDS)

    window_title_fetcher = _select_correct_window_title_fetcher()
    logger.debug("Using fetcher: %s", window_title_fetcher)

    logger.info("Registering hotkeys...")
    hotkey_registrator.register_hotkeys(window_title_fetcher)
    keyboard.wait()
