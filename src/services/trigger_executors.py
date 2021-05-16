import logging
import os
import sys

import keyboard
from src.models.exceptions import UnsupportedVersionError
from src.services.mc_window_manager import MCWindowManager
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
    mc_window_manager = MCWindowManager(window_title_fetcher)

    if not mc_window_manager.is_minecraft_focused():
        return

    world_generator_selector = WorldGeneratorSelector(mc_window_manager)

    try:
        rsg_world_generator = world_generator_selector.select_rsg_world_generator()
    except UnsupportedVersionError as unsupported_version_error:
        logger.info("Looks like minecraft version you're trying to use is not supported: %s", unsupported_version_error)
    else:
        rsg_world_generator.generate_world()
    finally:
        if sys.platform == "darwin":
            _clear_darwin_events()


def on_new_ssg_world_trigger(window_title_fetcher: BaseWindowTitleFetcher) -> None:
    mc_window_manager = MCWindowManager(window_title_fetcher)

    if not mc_window_manager.is_minecraft_focused():
        return

    world_generator_selector = WorldGeneratorSelector(mc_window_manager)

    try:
        ssg_world_generator = world_generator_selector.select_ssg_world_generator()
    except UnsupportedVersionError as unsupported_version_error:
        logger.info("Looks like minecraft version you're trying to use is not supported: %s", unsupported_version_error)
    else:
        ssg_world_generator.generate_world()
    finally:
        if sys.platform == "darwin":
            _clear_darwin_events()


def on_world_exit(window_title_fetcher: BaseWindowTitleFetcher) -> None:
    mc_window_manager = MCWindowManager(window_title_fetcher)

    if not mc_window_manager.is_minecraft_focused():
        return

    world_generator_selector = WorldGeneratorSelector(mc_window_manager)
    try:
        world_exiter = world_generator_selector.select_world_exiter()
    except UnsupportedVersionError as unsupported_version_error:
        logger.info("Looks like minecraft version you're trying to use is not supported: %s", unsupported_version_error)
    else:
        world_exiter.exit_world()
    finally:
        if sys.platform == "darwin":
            _clear_darwin_events()
