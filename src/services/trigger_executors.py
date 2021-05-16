import logging
import os

import keyboard
from src.models.exceptions import UnsupportedVersionError
from src.services.mc_window_managers.base_window_manager import BaseWindowManager
from src.services.world_generator_selector import WorldGeneratorSelector

logger = logging.getLogger(__name__)


def on_quit() -> None:
    logger.info("Pressed exit, quitting now.")
    keyboard.unhook_all()
    os._exit(0)


def _clear_events() -> None:
    # it's a dirty trick to circumvent the situation when the keyboard module for some reason thinks that the hotkey
    # is being pressed and released continously in some cases - I know it's ugly but it works :(
    keyboard._pressed_events.clear()
    keyboard._physically_pressed_keys.clear()
    keyboard._logically_pressed_keys.clear()
    keyboard._hotkeys.clear()


def on_new_rsg_world_trigger(window_manager: BaseWindowManager) -> None:
    if not window_manager.is_minecraft_focused():
        return

    world_generator_selector = WorldGeneratorSelector(window_manager)

    try:
        rsg_world_generator = world_generator_selector.select_rsg_world_generator()
    except UnsupportedVersionError as unsupported_version_error:
        logger.info("Looks like minecraft version you're trying to use is not supported: %s", unsupported_version_error)
    else:
        rsg_world_generator.generate_world()
    finally:
        _clear_events()


def on_new_ssg_world_trigger(window_manager: BaseWindowManager) -> None:
    if not window_manager.is_minecraft_focused():
        return

    world_generator_selector = WorldGeneratorSelector(window_manager)

    try:
        ssg_world_generator = world_generator_selector.select_ssg_world_generator()
    except UnsupportedVersionError as unsupported_version_error:
        logger.info("Looks like minecraft version you're trying to use is not supported: %s", unsupported_version_error)
    else:
        ssg_world_generator.generate_world()
    finally:
        _clear_events()


def on_world_exit(window_manager: BaseWindowManager) -> None:
    if not window_manager.is_minecraft_focused():
        return

    world_generator_selector = WorldGeneratorSelector(window_manager)
    try:
        world_exiter = world_generator_selector.select_world_exiter()
    except UnsupportedVersionError as unsupported_version_error:
        logger.info("Looks like minecraft version you're trying to use is not supported: %s", unsupported_version_error)
    else:
        world_exiter.exit_world()
    finally:
        _clear_events()
