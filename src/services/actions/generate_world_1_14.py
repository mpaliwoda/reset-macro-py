import logging

from src.services.actions.base_action import BaseAction
from src.services.actions.mixins.world_creation_mixin_1_14 import WorldCreationMixin_1_14

logger = logging.getLogger(__name__)


class GenerateRSGWorld_1_14(BaseAction, WorldCreationMixin_1_14):
    def perform(self) -> None:
        logger.info("Generating new 1.14 RSG world")
        self.single_player_menu()
        self.create_new_world_menu()
        self.start_new_world()
