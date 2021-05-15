import Xlib.display
from src.services.window_title.base_window_title_fetcher import BaseWindowTitleFetcher


class X11WindowTitleFetcher(BaseWindowTitleFetcher):
    def fetch_window_title(self) -> str:
        display = Xlib.display.Display()
        window_in_focus = display.get_input_focus().focus
        return window_in_focus.get_wm_name()
