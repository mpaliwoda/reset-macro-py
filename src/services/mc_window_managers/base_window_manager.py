import abc
import re
from typing import Pattern

from src.models.exceptions import FailedToRetrieveMinecraftVersion


class BaseWindowManager(abc.ABC):
    @abc.abstractmethod
    def is_minecraft_focused(self) -> bool:
        pass

    @abc.abstractmethod
    def major_version(self) -> float:
        pass


class WindowTitleManager(BaseWindowManager):
    MC_MAJOR_VERSION_REGEX: Pattern = re.compile(r"minecraft\*?\s*(?P<major_version>\d\.\d+)\.\d+.*?", re.IGNORECASE)

    @abc.abstractmethod
    def fetch_window_title(self) -> str:
        pass

    def is_minecraft_focused(self) -> bool:
        return "minecraft" in self.fetch_window_title().casefold()

    def major_version(self) -> float:
        title = self.fetch_window_title()
        match = self.MC_MAJOR_VERSION_REGEX.match(title)
        if not match:
            raise FailedToRetrieveMinecraftVersion(f"Could not retrieve minecraft version from title: {title}")
        return float(match.group("major_version"))
