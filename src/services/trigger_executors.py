import logging
import os

import keyboard
from src.models.actions import Action
from src.models.exceptions import FailedToRetrieveMinecraftVersion, UnsupportedVersionError
from src.services.action_performer_selector import ActionPerformerSelector
from src.services.mc_window_managers.base_window_manager import BaseWindowManager

logger = logging.getLogger(__name__)


def on_quit_macro_trigger() -> None:
    logger.info("Pressed exit, quitting now.")
    keyboard.unhook_all()
    os._exit(0)


def on_new_rsg_world_trigger(window_manager: BaseWindowManager) -> None:
    _perform_action(action=Action.GENERATE_RSG_WORLD, window_manager=window_manager)


def on_new_ssg_world_trigger(window_manager: BaseWindowManager) -> None:
    _perform_action(action=Action.GENERATE_SSG_WORLD, window_manager=window_manager)


def on_world_exit_trigger(window_manager: BaseWindowManager) -> None:
    _perform_action(action=Action.EXIT_WORLD, window_manager=window_manager)


def _clear_events() -> None:
    # it's a dirty trick to circumvent the situation when the keyboard module for some reason thinks that the hotkey
    # is being pressed and released continously in some cases - I know it's ugly but it works :(
    keyboard._pressed_events.clear()
    keyboard._physically_pressed_keys.clear()
    keyboard._logically_pressed_keys.clear()
    keyboard._hotkeys.clear()


def _perform_action(action: Action, window_manager: BaseWindowManager) -> None:
    if not window_manager.is_minecraft_focused():
        return

    action_performer_selector = ActionPerformerSelector(window_manager)
    try:
        action_performer = action_performer_selector.select_action_performer(action)
    except UnsupportedVersionError as unsupported_version_error:
        logger.info("Looks like minecraft version you're trying to use is not supported. %s", unsupported_version_error)
    except FailedToRetrieveMinecraftVersion as failed_to_retrieve_minecraft_version:
        logger.info("Looks like minecraft version could not be retrieved: %s", failed_to_retrieve_minecraft_version)
    else:
        action_performer.perform_action()
    finally:
        _clear_events()
