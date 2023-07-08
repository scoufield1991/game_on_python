from abc import ABC, abstractmethod


class IPlay:

    @abstractmethod
    def _start_game(self):
        pass

    @abstractmethod
    def _finish_game(self):
        pass
