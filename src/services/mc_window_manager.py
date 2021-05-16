import re
from typing import Pattern

from simpleconf import config
from src.services.window_title.base_window_title_fetcher import BaseWindowTitleFetcher


class MCWindowManager:
    MC_MAJOR_VERSION_REGEX: Pattern = re.compile(r"minecraft\*?\s*(?P<major_version>\d\.\d+)\.\d+.*?", re.IGNORECASE)

    def __init__(self, window_title_fetcher: BaseWindowTitleFetcher) -> None:
        self.title_fetcher = window_title_fetcher

    def get_major_version(self) -> float:
        if not config.check_minecraft_window_before_running_hotkey:
            return float(config.active_minecraft_version)

        match = self.MC_MAJOR_VERSION_REGEX.match(self._current_window_title())
        if match:
            return float(match.group("major_version"))

        # fallback to active minecraft version
        return float(config.active_minecraft_version)

    def is_minecraft_focused(self) -> bool:
        if not config.check_minecraft_window_before_running_hotkey:
            return True
        return "minecraft" in self._current_window_title().casefold()

    def _current_window_title(self) -> str:
        return self.title_fetcher.fetch_window_title()
