import logging

import keyboard
from src import config
from src.services import trigger_executors
from src.services.window_title.base_window_title_fetcher import BaseWindowTitleFetcher

logger = logging.getLogger(__name__)


def register_hotkeys(window_title_fetcher: BaseWindowTitleFetcher) -> None:
    keyboard.add_hotkey(config.RSG_HOTKEY, trigger_executors.on_new_rsg_world_trigger, args=[window_title_fetcher])
    logger.info("Added %s for creating new RSG world", config.RSG_HOTKEY)

    keyboard.add_hotkey(config.SSG_HOTKEY, trigger_executors.on_new_ssg_world_trigger, args=[window_title_fetcher])
    logger.info("Added %s for creating new SSG world", config.SSG_HOTKEY)

    keyboard.add_hotkey(config.EXIT_WORLD_HOTKEY, trigger_executors.on_world_exit, args=[window_title_fetcher])
    logger.info("Added %s for exiting the world", config.EXIT_WORLD_HOTKEY)

    keyboard.add_hotkey(config.EXIT_MACRO_HOTKEY, trigger_executors.on_quit)
    logger.info("Added %s for quitting the macro", config.EXIT_MACRO_HOTKEY)
