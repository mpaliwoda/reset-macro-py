from src.services.key_presses.base_key_presser import BaseKeyPresser


class WorldCreationMixin_1_14:
    key_presser: BaseKeyPresser

    def single_player_menu(self) -> None:
        self.key_presser.press("tab")
        self.key_presser.press("enter")

    def create_new_world_menu(self) -> None:
        self.key_presser.press("tab", times=4)
        self.key_presser.press("enter")

    def start_new_world(self) -> None:
        self.key_presser.press("tab", times=4)
        self.key_presser.press("enter")
