import logging

import keyboard
from simpleconf import config
from src.services import trigger_executors
from src.services.window_title.base_window_title_fetcher import BaseWindowTitleFetcher

logger = logging.getLogger(__name__)


def register_hotkeys(window_title_fetcher: BaseWindowTitleFetcher) -> None:
    keyboard.add_hotkey(config.rsg_hotkey, trigger_executors.on_new_rsg_world_trigger, args=[window_title_fetcher])
    logger.info("Added %s for creating new RSG world", config.rsg_hotkey)

    keyboard.add_hotkey(config.ssg_hotkey, trigger_executors.on_new_ssg_world_trigger, args=[window_title_fetcher])
    logger.info("Added %s for creating new SSG world", config.ssg_hotkey)

    keyboard.add_hotkey(config.exit_world_hotkey, trigger_executors.on_world_exit, args=[window_title_fetcher])
    logger.info("Added %s for exiting the world", config.exit_world_hotkey)

    keyboard.add_hotkey(config.exit_macro_hotkey, trigger_executors.on_quit)
    logger.info("Added %s for quitting the macro", config.exit_macro_hotkey)
