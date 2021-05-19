import win32gui
from src.services.window_managers.base_window_manager import WindowTitleManager


class WindowsWindowManager(WindowTitleManager):
    def fetch_window_title(self) -> str:
        window_in_focus = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(window_in_focus)
