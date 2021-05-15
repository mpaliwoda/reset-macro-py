from AppKit import NSWorkspace
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
from src.services.window_title.base_window_title_fetcher import BaseWindowTitleFetcher


class DarwinWindowTitleFetcher(BaseWindowTitleFetcher):
    def fetch_window_title(self) -> str:
        active_app_name = NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()

        options = kCGWindowListOptionOnScreenOnly
        windowList = CGWindowListCopyWindowInfo(options, kCGNullWindowID)

        for window in windowList:
            if window["kCGWindowOwnerName"] == active_app_name:
                return window.get("kCGWindowName", "Unknown")
        else:
            return "Unknown"
