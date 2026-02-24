from abc import ABC, abstractmethod


class Document(ABC):
    def __init__(self, titre: str):
        self._titre = titre
        self.__disponibilite = True

    @property
    def titre(self):
        return self._titre

    @property
    def disponibilite(self):
        return self.__disponibilite

    def _changer_disponibilite(self, etat):
        self.__disponibilite = etat

    @abstractmethod
    def emprunter(self):
        pass

    @abstractmethod
    def retourner(self):
        pass

    @abstractmethod
    def afficher_details(self):
        pass

    @abstractmethod
    def affichier_un_detail(self):
        pass

    @abstractmethod
    def chang_etat_non(self):
        pass


