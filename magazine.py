from abstraite import Document


class Magazine(Document):
    def __init__(self, titre, numero_edition):
        super().__init__(titre)
        self.numero_edition = numero_edition

    def emprunter(self):
        if not self.disponibilite:
            raise ValueError("Le magazine est déjà emprunté.")
        self._changer_disponibilite(False)
        print(f"Le magazine '{self.titre}' a été emprunté.")

    def retourner(self):
        if self.disponibilite:
            raise ValueError("Le magazine n'est pas emprunté.")
        self._changer_disponibilite(True)
        print(f"Le magazine '{self.titre}' a été rendu.")

    def afficher_details(self):
        etat = "Disponible" if self.disponibilite else "Indisponible"
        print(f"{self.titre} |==| {self.numero_edition} |==| {etat}")

    def affichier_un_detail(self):
        etat = "Disponible" if self.disponibilite else "Indisponible"
        print(f"{self.titre} : {self.numero_edition} - {etat}")

    def chang_etat_non(self):
        print("Modification directe interdite.")

