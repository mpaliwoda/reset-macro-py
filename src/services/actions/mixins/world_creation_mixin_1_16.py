import logging
from typing import Dict

from simpleconf import config

from src.models.game_state import GameState
from src.services.key_presses.base_key_presser import BaseKeyPresser

logger = logging.getLogger(__name__)


class WorldCreationMixin_1_16:
    key_presser: BaseKeyPresser
    game_state: GameState

    _SELECT_DIFFICULTY_OFFSET: int = 2
    _MORE_WORLD_OPTIONS_OFFSET: int = 6

    _POSSIBLE_DIFFICULTIES_MAPPING: Dict[str, int] = {
        "normal": 0,
        "hard": 1,
        "easy": 3,
    }

    def single_player_menu(self) -> None:
        self.key_presser.press("tab")
        self.key_presser.press("enter")

    def create_new_world_menu(self) -> None:
        self.key_presser.press("tab", times=3)
        self.key_presser.press("enter")

    def start_new_world(self) -> None:
        self.key_presser.press("tab", times=(7 - self.game_state.world_creation_screen_offset))
        self.key_presser.press("enter")
        self.game_state.world_creation_screen_offset = 0

    def select_difficulty(self) -> None:
        self.key_presser.press("tab", times=2)
        self.key_presser.press("enter", times=self._get_difficulty_from_config())
        self.game_state.world_creation_screen_offset = self._SELECT_DIFFICULTY_OFFSET

    def more_world_options(self) -> None:
        self.key_presser.press("tab", times=(6 - self.game_state.world_creation_screen_offset))
        self.key_presser.press("enter")

    def exit_more_world_options(self) -> None:
        self.key_presser.press("tab", times=5)
        self.key_presser.press("enter")
        self.game_state.world_creation_screen_offset = self._MORE_WORLD_OPTIONS_OFFSET

    def set_seed_field(self) -> None:
        self.key_presser.press("tab", times=3)

    def _get_difficulty_from_config(self) -> int:
        if config.difficulty.casefold() in self._POSSIBLE_DIFFICULTIES_MAPPING:
            return self._POSSIBLE_DIFFICULTIES_MAPPING[config.difficulty]
        logger.warning(
            "Selected incorrect diffuculty in config. Defaulting to easy. Allowed diffculties: %s",
            list(self._POSSIBLE_DIFFICULTIES_MAPPING.keys()),
        )
        return self._POSSIBLE_DIFFICULTIES_MAPPING["easy"]
