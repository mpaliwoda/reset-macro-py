from src.models.actions import Action
from src.models.exceptions import UnsupportedVersionError
from src.services.action_performers.base_action_performer import BaseActionPerformer
from src.services.action_performers.base_world_exiter import BaseWorldExiter
from src.services.action_performers.base_world_generator import BaseWorldGenerator
from src.services.action_performers.world_exiter_post_1_14 import WorldExiterPost_1_14
from src.services.action_performers.world_generators_1_14 import RSGGenerator as RSGGenerator_1_14
from src.services.action_performers.world_generators_1_16 import RSGGenerator as RSGGenerator_1_16
from src.services.action_performers.world_generators_1_16 import SSGGenerator as SSGGenerator_1_16
from src.services.mc_window_managers.base_window_manager import BaseWindowManager


class ActionPerformerSelector:
    def __init__(self, window_manager: BaseWindowManager) -> None:
        self.window_manager = window_manager

    def select_action_performer(self, action: Action) -> BaseActionPerformer:
        if action == Action.GENERATE_RSG_WORLD:
            return self._select_rsg_world_generator()
        elif action == Action.GENERATE_SSG_WORLD:
            return self._select_ssg_world_generator()
        elif action == Action.EXIT_WORLD:
            return self._select_world_exiter()
        else:
            assert False, "This should never be called"

    def _select_rsg_world_generator(self) -> BaseWorldGenerator:
        major_version = self.window_manager.major_version()

        if major_version == 1.16:
            return RSGGenerator_1_16()
        elif 1.14 <= major_version <= 1.15:
            return RSGGenerator_1_14()
        else:
            raise UnsupportedVersionError(
                f"RSG world generation for version {major_version} is not supported and probably won't be in the future"
            )

    def _select_ssg_world_generator(self) -> BaseWorldGenerator:
        major_version = self.window_manager.major_version()

        if major_version == 1.16:
            return SSGGenerator_1_16()
        else:
            raise UnsupportedVersionError(
                f"SSG world generation for version {major_version} is not supported and probably won't be in the future"
            )

    def _select_world_exiter(self) -> BaseWorldExiter:
        major_version = self.window_manager.major_version()

        if major_version >= 1.14:
            return WorldExiterPost_1_14()
        else:
            raise UnsupportedVersionError(
                f"Exitint world for version {major_version} is not supported and probably won't be in the future"
            )
