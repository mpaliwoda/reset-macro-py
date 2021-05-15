import re
from typing import Pattern

from src.models.exceptions import UnsupportedVersionError
from src.world_generators.base_world_generator import BaseWorldGenerator
from src.world_generators.v1_14 import RSGGenerator as RSGGenerator_1_14
from src.world_generators.v1_16 import RSGGenerator as RSGGenerator_1_16
from src.world_generators.v1_16 import SSGGenerator as SSGGenerator_1_16
from src.world_generators.world_exiter import BaseWorldExiter, WorldExiter


class WorldGeneratorSelector:
    MC_MAJOR_VERSION_REGEX: Pattern = re.compile(r"minecraft\*?\s*(?P<major_version>\d\.\d+)\.\d+.*?", re.IGNORECASE)

    def select_rsg_world_generator(self, window_title: str) -> BaseWorldGenerator:
        major_version = self._retrieve_major_version(window_title)

        if major_version == 1.16:
            return RSGGenerator_1_16()
        elif 1.14 <= major_version <= 1.15:
            return RSGGenerator_1_14()
        else:
            raise UnsupportedVersionError(
                f"RSG world generation for version {major_version} is not supported and probably won't be in the future"
            )

    def select_ssg_world_generator(self, window_title: str) -> BaseWorldGenerator:
        major_version = self._retrieve_major_version(window_title)

        if major_version == 1.16:
            return SSGGenerator_1_16()
        else:
            raise UnsupportedVersionError(
                f"SSG world generation for version {major_version} is not supported and probably won't be in the future"
            )

    def select_world_exiter(self, window_title: str) -> BaseWorldExiter:
        major_version = self._retrieve_major_version(window_title)
        if major_version >= 1.14:
            return WorldExiter()
        else:
            raise UnsupportedVersionError(
                f"Exitint world for version {major_version} is not supported and probably won't be in the future"
            )

    def _retrieve_major_version(self, window_title: str) -> float:
        match = self.MC_MAJOR_VERSION_REGEX.match(window_title)
        if match:
            return float(match.group("major_version"))
        # just fall back to 1.16
        return 1.16
