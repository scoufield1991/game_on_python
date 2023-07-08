from abc import ABC, abstractmethod


class IDeck(ABC):

    @abstractmethod
    def _open_deck(self):
        pass

    @abstractmethod
    def _shuffle_deck(self):
        pass
