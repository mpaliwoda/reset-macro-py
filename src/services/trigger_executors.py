import logging
import os

import keyboard
from src.models.action_types import ActionType
from src.models.exceptions import FailedToRetrieveMinecraftVersion, UnsupportedVersionError
from src.services.action_selector import ActionSelector
from src.services.mc_window_managers.base_window_manager import BaseWindowManager

logger = logging.getLogger(__name__)


def quit_macro() -> None:
    logger.info("Pressed exit, quitting now.")
    keyboard.unhook_all()
    os._exit(0)


def perform_action(action_type: ActionType, window_manager: BaseWindowManager) -> None:
    if not window_manager.is_minecraft_focused():
        return

    action_selector = ActionSelector(window_manager)
    try:
        action = action_selector.select_action(action_type)
    except UnsupportedVersionError as unsupported_version_error:
        logger.info("Looks like minecraft version you're trying to use is not supported. %s", unsupported_version_error)
    except FailedToRetrieveMinecraftVersion as failed_to_retrieve_minecraft_version:
        logger.info("Looks like minecraft version could not be retrieved: %s", failed_to_retrieve_minecraft_version)
    else:
        action.perform()
    finally:
        _clear_events()


def _clear_events() -> None:
    # it's a dirty trick to circumvent the situation when the keyboard module for some reason thinks that the hotkey
    # is being pressed and released continously in some cases - I know it's ugly but it works :(
    keyboard._pressed_events.clear()
    keyboard._physically_pressed_keys.clear()
    keyboard._logically_pressed_keys.clear()
    keyboard._hotkeys.clear()
