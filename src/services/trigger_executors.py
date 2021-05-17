import logging
import os
from typing import TYPE_CHECKING

import keyboard
from src.models.action_types import ActionType
from src.models.exceptions import FailedToRetrieveMinecraftVersion, UnsupportedVersionError

if TYPE_CHECKING:
    from src import Macro

logger = logging.getLogger(__name__)


def quit_macro() -> None:
    logger.info("Pressed exit, quitting now.")
    keyboard.unhook_all()
    os._exit(0)


def perform_action(action_type: ActionType, macro: "Macro") -> None:
    if not macro.window_manager.is_minecraft_focused():
        return

    major_version = macro.window_manager.major_version()
    try:
        action_class = macro.action_selector.select_action(action_type, major_version)
    except UnsupportedVersionError as unsupported_version_error:
        logger.info("Looks like minecraft version you're trying to use is not supported. %s", unsupported_version_error)
    except FailedToRetrieveMinecraftVersion as failed_to_retrieve_minecraft_version:
        logger.info("Looks like minecraft version could not be retrieved: %s", failed_to_retrieve_minecraft_version)
    else:
        action_class(key_presser=macro.key_presser, game_state=macro.game_state).perform()
    finally:
        _clear_events()


def _clear_events() -> None:
    # it's a dirty trick to circumvent the situation when the keyboard module for some reason thinks that the hotkey
    # is being pressed and released continously in some cases - I know it's ugly but it works :(
    keyboard._pressed_events.clear()
    keyboard._physically_pressed_keys.clear()
    keyboard._logically_pressed_keys.clear()
    keyboard._hotkeys.clear()
