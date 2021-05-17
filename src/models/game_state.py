from dataclasses import dataclass


@dataclass
class GameState:
    opened_to_lan: bool
    world_creation_screen_offset: int
