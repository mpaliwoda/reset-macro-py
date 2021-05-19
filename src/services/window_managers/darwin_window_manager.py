from AppKit import NSWorkspace
from Quartz import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionOnScreenOnly

from src.services.window_managers.base_window_manager import WindowTitleManager


class DarwinWindowManager(WindowTitleManager):
    def fetch_window_title(self) -> str:
        active_app_name = NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()

        options = kCGWindowListOptionOnScreenOnly
        window_list = CGWindowListCopyWindowInfo(options, kCGNullWindowID)

        for window in window_list:
            if window["kCGWindowOwnerName"] == active_app_name:
                return window.get("kCGWindowName", "Unknown")
        else:
            return "Unknown"
