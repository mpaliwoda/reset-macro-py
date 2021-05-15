import win32gui
from src.services.window_title.base_window_title_fetcher import BaseWindowTitleFetcher


class WindowsWindowTitleFetcher(BaseWindowTitleFetcher):
    def fetch_window_title(self) -> str:
        window_in_focus = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(window_in_focus)
