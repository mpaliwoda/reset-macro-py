from src.services.world_name_generators.base_world_name_generator import BaseWorldNameGenerator
from src.services.world_name_generators.txt_file_world_name_generator import TxtFileWorldNameGenerator


class WorldNameGeneratorSelector:
    def select_world_name_generator(self) -> BaseWorldNameGenerator:
        return TxtFileWorldNameGenerator()
