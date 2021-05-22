import logging

from simpleconf import config

from src.services.actions.base_action import BaseAction
from src.services.actions.mixins.world_creation_mixin_1_14 import WorldCreationMixin_1_14
from src.services.world_name_generator_selector import WorldNameGeneratorSelector

logger = logging.getLogger(__name__)


class GenerateRSGWorld_1_14(BaseAction, WorldCreationMixin_1_14):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.world_name_generator = WorldNameGeneratorSelector().select_world_name_generator()

    def perform(self) -> None:
        logger.info("Generating new 1.14 RSG world")
        self.single_player_menu()
        self.create_new_world_menu()
        if config.name_worlds:
            self.name_world()
        self.start_new_world()
