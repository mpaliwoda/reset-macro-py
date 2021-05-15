import abc


class BaseWindowTitleFetcher(abc.ABC):
    @abc.abstractmethod
    def fetch_window_title(self) -> str:
        pass
