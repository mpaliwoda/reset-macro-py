import logging

from src.models.exceptions import UnsupportedVersionError
from src.services.mc_window_managers.base_window_manager import BaseWindowManager
from src.world_generators.base_world_generator import BaseWorldGenerator
from src.world_generators.v1_14 import RSGGenerator as RSGGenerator_1_14
from src.world_generators.v1_16 import RSGGenerator as RSGGenerator_1_16
from src.world_generators.v1_16 import SSGGenerator as SSGGenerator_1_16
from src.world_generators.world_exiter import BaseWorldExiter, WorldExiter


class WorldGeneratorSelector:
    def __init__(self, window_manager: BaseWindowManager) -> None:
        self.window_manager = window_manager

    def select_rsg_world_generator(self) -> BaseWorldGenerator:
        major_version = self.window_manager.major_version()

        if major_version == 1.16:
            return RSGGenerator_1_16()
        elif 1.14 <= major_version <= 1.15:
            return RSGGenerator_1_14()
        else:
            raise UnsupportedVersionError(
                f"RSG world generation for version {major_version} is not supported and probably won't be in the future"
            )

    def select_ssg_world_generator(self) -> BaseWorldGenerator:
        major_version = self.window_manager.major_version()

        if major_version == 1.16:
            return SSGGenerator_1_16()
        else:
            raise UnsupportedVersionError(
                f"SSG world generation for version {major_version} is not supported and probably won't be in the future"
            )

    def select_world_exiter(self) -> BaseWorldExiter:
        major_version = self.window_manager.major_version()

        if major_version >= 1.14:
            return WorldExiter()
        else:
            raise UnsupportedVersionError(
                f"Exitint world for version {major_version} is not supported and probably won't be in the future"
            )
