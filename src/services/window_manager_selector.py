import sys

from simpleconf import config
from src.services.window_managers.base_window_manager import BaseWindowManager
from src.services.window_managers.dummy_window_manager import DummyWindowManager


class WindowManagerSelector:
    def select_window_manager(self) -> BaseWindowManager:
        if not config.check_minecraft_window_before_executing_actions:
            return DummyWindowManager()

        if sys.platform == "win32":
            from src.services.window_managers.windows_window_manager import WindowsWindowManager

            return WindowsWindowManager()
        elif sys.platform == "linux":
            from src.services.window_managers.x11_window_manager import X11WindowManager

            return X11WindowManager()
        elif sys.platform == "darwin":
            from src.services.window_managers.darwin_window_manager import DarwinWindowManager

            return DarwinWindowManager()
