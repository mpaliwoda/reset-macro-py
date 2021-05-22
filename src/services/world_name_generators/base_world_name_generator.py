import abc


class BaseWorldNameGenerator(abc.ABC):
    @abc.abstractmethod
    def generate_new_world_name(self, major_version: float) -> str:
        pass
