from abstraite import Document


class Magazine(Document):
    def __init__(self, titre, numero_edition, id=None):
        super().__init__(titre, id)
        self.numero_edition = numero_edition

    def emprunter(self, adherent):
 
        if not self.disponibilite:
            raise ValueError("Le magazine est déjà emprunté.")
        self._changer_disponibilite(False)
        adherent.documents_empruntes.append(self)
        print(f"Le magazine '{self.titre}' a été emprunté par {adherent.nom} {adherent.prenom}.")


    def retourner(self, adherent):
        if self not in adherent.documents_empruntes:
            raise ValueError("Ce magazine n'est pas emprunté par cet adhérent.")
        adherent.documents_empruntes.remove(self)
        self._changer_disponibilite(True)
        print(f"Le magazine '{self.titre}' a été rendu par {adherent.nom} {adherent.prenom}.")

    def afficher_details(self):
        etat = "Disponible" if self.disponibilite else "Indisponible"
        print(f"{self.titre} |==| {self.numero_edition} |==| {etat}")

    def afficher_un_detail(self):
        etat = "Disponible" if self.disponibilite else "Indisponible"
        print(f"{self.titre} : {self.numero_edition} - {etat}")

    def chang_etat_non(self):
        print("Modification directe interdite.")

