import abc


class BaseWorldGenerator(abc.ABC):
    @abc.abstractmethod
    def single_player_menu(self) -> None:
        pass

    @abc.abstractmethod
    def create_new_world_menu(self) -> None:
        pass

    @abc.abstractmethod
    def start_new_world(self) -> None:
        pass

    @abc.abstractmethod
    def more_world_options(self) -> None:
        pass

    @abc.abstractmethod
    def exit_more_world_options(self) -> None:
        pass

    @abc.abstractmethod
    def generate_world(self) -> None:
        pass
