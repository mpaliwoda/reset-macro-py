import logging
import os.path

from src.services.world_name_generators.base_world_name_generator import BaseWorldNameGenerator

logger = logging.getLogger(__name__)


class TxtFileWorldNameGenerator(BaseWorldNameGenerator):
    WORLD_COUNTER_FILE_NAME_1_16: str = "world_counter_1_16.txt"
    WORLD_COUNTER_FILE_NAME_1_14: str = "world_counter_1_14.txt"
    GENERAL_WORLD_COUNTER: str = "world_counter.txt"

    def generate_new_world_name(self, major_version: float) -> str:
        last_world_number = self._fetch_world_number(major_version)
        current_world_number = last_world_number + 1
        self._save_world_number(current_world_number, major_version)
        return str(current_world_number)

    def _fetch_world_number(self, major_version: float) -> int:
        world_counter_filename = self._world_counter_filename(major_version)
        self._create_world_counter_file_if_does_not_exist(world_counter_filename)

        with open(world_counter_filename, "r") as world_counter_file:
            raw_world_number = world_counter_file.read()

        try:
            return int(raw_world_number)
        except ValueError:
            logger.warning("world_counter.txt doesn't contain valid number: %s. Defaulting to 0.", raw_world_number)
            return 0

    def _save_world_number(self, world_number: int, major_version: float) -> None:
        world_counter_filename = self._world_counter_filename(major_version)
        with open(world_counter_filename, "w") as world_counter_file:
            world_counter_file.truncate(0)
            world_counter_file.seek(0)
            world_counter_file.write(str(world_number))

    def _create_world_counter_file_if_does_not_exist(self, world_counter_filename: str) -> None:
        if not os.path.isfile(world_counter_filename):
            with open(world_counter_filename, "w") as world_counter_file:
                world_counter_file.write(str(0))

    def _world_counter_filename(self, major_version: float) -> str:
        if major_version == 1.16:
            return self.WORLD_COUNTER_FILE_NAME_1_16
        elif major_version in [1.14, 1.15]:
            return self.WORLD_COUNTER_FILE_NAME_1_14
        else:
            return self.GENERAL_WORLD_COUNTER
