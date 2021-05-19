import Xlib.display
from src.services.window_managers.base_window_manager import WindowTitleManager


class X11WindowManager(WindowTitleManager):
    def fetch_window_title(self) -> str:
        display = Xlib.display.Display()
        window_in_focus = display.get_input_focus().focus
        return window_in_focus.get_wm_name()
