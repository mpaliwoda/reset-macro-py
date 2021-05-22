from typing import Type

from src.models.action_types import ActionType
from src.models.exceptions import UnsupportedVersionError
from src.services.actions.base_action import BaseAction
from src.services.actions.dummy_action import DummyAction
from src.services.actions.exit_world_post_1_14 import ExitWorldPost_1_14
from src.services.actions.force_perch_post_1_14 import ForcePerchPost_1_14
from src.services.actions.generate_world_1_14 import GenerateRSGWorld_1_14
from src.services.actions.generate_world_1_16 import GenerateFSGWorld_1_16, GenerateRSGWorld_1_16, GenerateSSGWorld_1_16


class ActionSelector:
    def select_action(self, action_type: ActionType, major_version: float) -> Type[BaseAction]:
        if action_type == ActionType.GENERATE_RSG_WORLD:
            return self._select_rsg_world_generator(major_version)
        elif action_type == ActionType.GENERATE_SSG_WORLD:
            return self._select_ssg_world_generator(major_version)
        elif action_type == ActionType.GENERATE_FSG_WORLD:
            return self._select_fsg_world_generator(major_version)
        elif action_type == ActionType.EXIT_WORLD:
            return self._select_world_exiter(major_version)
        elif action_type == ActionType.FORCE_PERCH:
            return self._select_perch_enforcer(major_version)
        return DummyAction

    def _select_rsg_world_generator(self, major_version: float) -> Type[BaseAction]:
        if major_version == 1.16:
            return GenerateRSGWorld_1_16
        elif 1.14 <= major_version <= 1.15:
            return GenerateRSGWorld_1_14
        raise UnsupportedVersionError(f"RSG world generation for version {major_version} is not supported")

    def _select_ssg_world_generator(self, major_version: float) -> Type[BaseAction]:
        if major_version == 1.16:
            return GenerateSSGWorld_1_16
        raise UnsupportedVersionError(f"SSG world generation for version {major_version} is not supported")

    def _select_fsg_world_generator(self, major_version: float) -> Type[BaseAction]:
        if major_version == 1.16:
            return GenerateFSGWorld_1_16
        raise UnsupportedVersionError(f"FSG world generation for version {major_version} is not supported")

    def _select_world_exiter(self, major_version: float) -> Type[BaseAction]:
        if major_version >= 1.14:
            return ExitWorldPost_1_14
        raise UnsupportedVersionError(f"Exiting world for version {major_version} is not supported")

    def _select_perch_enforcer(self, major_version: float) -> Type[BaseAction]:
        if major_version >= 1.14:
            return ForcePerchPost_1_14
        raise UnsupportedVersionError(f"Forcing perch for version {major_version} is not supported")
