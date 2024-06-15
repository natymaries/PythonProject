from abc import ABC, abstractmethod


class Forma(ABC):
    numar_laturi = 0
    @abstractmethod
    def schimba_culoarea(self, culoare):
        pass
