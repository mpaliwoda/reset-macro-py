from simpleconf import config
from src.services.mc_window_managers.base_window_manager import BaseWindowManager


class DummyWindowManager(BaseWindowManager):
    def is_minecraft_focused(self) -> bool:
        return True

    def major_version(self) -> float:
        return float(config.active_minecraft_version)
