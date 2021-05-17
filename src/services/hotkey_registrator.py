import logging

import keyboard
from simpleconf import config
from src.models.action_types import ActionType
from src.services import trigger_executors
from src.services.mc_window_managers.base_window_manager import BaseWindowManager

logger = logging.getLogger(__name__)


class HotkeyRegistrator:
    FALLBACK_EXIT_MACRO_HOTKEY: str = "="

    def __init__(self, window_manager: BaseWindowManager) -> None:
        self.window_manager = window_manager

    def register_hotkeys(self) -> None:
        self._register_rsg_hotkey()
        self._register_ssg_hotkey()
        self._register_exit_world_hotkey()
        self._register_exit_macro_hotkey()

    def _register_rsg_hotkey(self) -> None:
        if not config.rsg_hotkey:
            self._warn_about_missing_hotkey("Hotkey for RSG world generation not specified.")
            return

        keyboard.add_hotkey(
            config.rsg_hotkey,
            trigger_executors.perform_action,
            args=[ActionType.GENERATE_RSG_WORLD, self.window_manager],
        )
        logger.info("Added %s for creating new RSG world", config.rsg_hotkey)

    def _register_ssg_hotkey(self) -> None:
        if not config.ssg_hotkey:
            self._warn_about_missing_hotkey("Hotkey for SSG world generation not specified.")
            return

        keyboard.add_hotkey(
            config.ssg_hotkey,
            trigger_executors.perform_action,
            args=[ActionType.GENERATE_SSG_WORLD, self.window_manager],
        )
        logger.info("Added %s for creating new SSG world", config.ssg_hotkey)

    def _register_exit_world_hotkey(self) -> None:
        if not config.rsg_hotkey:
            self._warn_about_missing_hotkey("Hotkey for exiting world not specified.")
            return

        keyboard.add_hotkey(
            config.exit_world_hotkey,
            trigger_executors.perform_action,
            args=[ActionType.EXIT_WORLD, self.window_manager],
        )
        logger.info("Added %s for exiting the world", config.exit_world_hotkey)

    def _register_exit_macro_hotkey(self) -> None:
        if not config.exit_macro_hotkey:
            logger.error(
                "Hotkey for exiting macro not specified. Falling back to key: %s",
                self.FALLBACK_EXIT_MACRO_HOTKEY,
            )
            keyboard.add_hotkey(self.FALLBACK_EXIT_MACRO_HOTKEY, trigger_executors.quit_macro)
            return

        keyboard.add_hotkey(config.exit_macro_hotkey, trigger_executors.quit_macro)
        logger.info("Added %s for exiting the macro", config.exit_macro_hotkey)

    def _warn_about_missing_hotkey(self, warning: str) -> None:
        if config.warn_about_missing_hotkeys:
            logger.warning(warning)
