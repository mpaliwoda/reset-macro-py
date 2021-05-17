from simpleconf import config
from src.models.action_types import ActionType
from src.models.game_state import GameState
from src.models.exceptions import UnsupportedVersionError
from src.services.actions.base_action import BaseAction
from src.services.actions.exit_world_post_1_14 import ExitWorldPost_1_14
from src.services.actions.force_perch_post_1_14 import ForcePerchPost_1_14
from src.services.actions.generate_world_1_14 import GenerateRSGWorld_1_14
from src.services.actions.generate_world_1_16 import GenerateRSGWorld_1_16, GenerateSSGWorld_1_16
from src.services.key_presses.keyboard_key_presser import KeyboardKeyPresser
from src.services.mc_window_managers.base_window_manager import BaseWindowManager


class ActionSelector:
    def __init__(self, game_state: GameState, window_manager: BaseWindowManager) -> None:
        self.game_state = game_state
        self.window_manager = window_manager

    def select_action(self, action_type: ActionType) -> BaseAction:
        if action_type == ActionType.GENERATE_RSG_WORLD:
            return self._select_rsg_world_generator()
        elif action_type == ActionType.GENERATE_SSG_WORLD:
            return self._select_ssg_world_generator()
        elif action_type == ActionType.EXIT_WORLD:
            return self._select_world_exiter()
        elif action_type == ActionType.FORCE_PERCH:
            return self._select_perch_enforcer()
        else:
            assert False, "This should never be called"

    def _select_rsg_world_generator(self) -> BaseAction:
        major_version = self.window_manager.major_version()
        key_presser = KeyboardKeyPresser(delay_in_miliseconds=config.key_delay_in_miliseconds)

        if major_version == 1.16:
            return GenerateRSGWorld_1_16(self.game_state, key_presser)
        elif 1.14 <= major_version <= 1.15:
            return GenerateRSGWorld_1_14(self.game_state, key_presser)
        else:
            raise UnsupportedVersionError(f"RSG world generation for version {major_version} is not supported")

    def _select_ssg_world_generator(self) -> BaseAction:
        major_version = self.window_manager.major_version()
        key_presser = KeyboardKeyPresser(delay_in_miliseconds=config.key_delay_in_miliseconds)

        if major_version == 1.16:
            return GenerateSSGWorld_1_16(self.game_state, key_presser)
        else:
            raise UnsupportedVersionError(f"SSG world generation for version {major_version} is not supported")

    def _select_world_exiter(self) -> BaseAction:
        major_version = self.window_manager.major_version()
        key_presser = KeyboardKeyPresser(delay_in_miliseconds=0)

        if major_version >= 1.14:
            return ExitWorldPost_1_14(self.game_state, key_presser)
        else:
            raise UnsupportedVersionError(f"Exiting world for version {major_version} is not supported")

    def _select_perch_enforcer(self) -> BaseAction:
        major_version = self.window_manager.major_version()
        key_presser = KeyboardKeyPresser(delay_in_miliseconds=config.key_delay_in_miliseconds)

        if major_version >= 1.14:
            return ForcePerchPost_1_14(self.game_state, key_presser)
        else:
            raise UnsupportedVersionError(f"Forcing perch for version {major_version} is not supported")
