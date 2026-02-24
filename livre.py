from abstraite import Document


class Livre(Document):
    def __init__(self, titre, auteur):
        super().__init__(titre)
        self.auteur = auteur

    def emprunter(self):
        if not self.disponibilite:
            raise ValueError("Le livre est déjà emprunté.")
        self._changer_disponibilite(False)
        print(f"Le livre '{self.titre}' de {self.auteur} a été emprunté.")

    def retourner(self):
        if self.disponibilite:
            raise ValueError("Le livre n'est pas emprunté.")
        self._changer_disponibilite(True)
        print(f"Le livre '{self.titre}' de {self.auteur} a été rendu.")

    def afficher_details(self):
        etat = "Disponible" if self.disponibilite else "Indisponible"
        print(f"{self.titre} |==| {self.auteur} |==| {etat}")

    def afficher_un_detail(self):
        etat = "Disponible" if self.disponibilite else "Indisponible"
        print(f"{self.titre} |==| {self.auteur} |==| {etat}")

    def affichier_un_detail(self):
        etat = "Disponible" if self.disponibilite else "Indisponible"
        print(f"{self.titre} |==| {self.auteur} |==| {etat}")

    def chang_etat_non(self):
        print("Modification directe interdite.")