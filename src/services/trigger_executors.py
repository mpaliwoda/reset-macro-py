import logging
import os
import sys

import keyboard
from src.services.window_title.base_window_title_fetcher import BaseWindowTitleFetcher
from src.services.world_generator_selector import WorldGeneratorSelector

logger = logging.getLogger(__name__)


def _is_minecraft_focused(window_title: str) -> bool:
    return "minecraft" in window_title.casefold()


def on_quit() -> None:
    logger.info("Pressed exit, quitting now.")
    keyboard.unhook_all()
    os._exit(0)


def _clear_darwin_events() -> None:
      keyboard._pressed_events.clear()
      keyboard._physically_pressed_keys.clear()
      keyboard._logically_pressed_keys.clear()
      keyboard._hotkeys.clear()


def on_new_rsg_world_trigger(window_title_fetcher: BaseWindowTitleFetcher) -> None:
    window_title = window_title_fetcher.fetch_window_title()

    if not _is_minecraft_focused(window_title):
        return

    world_generator_selector = WorldGeneratorSelector()
    rsg_world_generator = world_generator_selector.select_rsg_world_generator(window_title)
    rsg_world_generator.generate_world()

    if sys.platform == "darwin":
        _clear_darwin_events()


def on_new_ssg_world_trigger(window_title_fetcher: BaseWindowTitleFetcher) -> None:
    window_title = window_title_fetcher.fetch_window_title()

    if not _is_minecraft_focused(window_title):
        return

    world_generator_selector = WorldGeneratorSelector()
    ssg_world_generator = world_generator_selector.select_ssg_world_generator(window_title)
    ssg_world_generator.generate_world()

    if sys.platform == "darwin":
        _clear_darwin_events()


def on_world_exit(window_title_fetcher: BaseWindowTitleFetcher) -> None:
    window_title = window_title_fetcher.fetch_window_title()

    if not _is_minecraft_focused(window_title):
        return

    world_generator_selector = WorldGeneratorSelector()
    world_exiter = world_generator_selector.select_world_exiter(window_title)
    world_exiter.exit_world()

    if sys.platform == "darwin":
        _clear_darwin_events()
