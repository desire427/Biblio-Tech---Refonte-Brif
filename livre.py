from abstraite import Document


class Livre(Document):
    def __init__(self, titre, auteur, id=None):
        super().__init__(titre, id)
        self.auteur = auteur

    def emprunter(self, adherent):
        if not self.disponibilite:
            raise ValueError("Le livre est déjà emprunté.")
        self._changer_disponibilite(False)
        adherent.documents_empruntes.append(self)
        # sql = " INSERT INTO Emprunts(id_livre, id_adherent, date_emprunt, date_retour) VALUES(%s, %s, %s, %s)"
        # val = (self.id, adherent.id,)
        # cursor.execute(sql, val)
        # conn.commit()
        print(f"Le livre '{self.titre}' de {self.auteur} a été emprunté par {adherent.nom} {adherent.prenom}.")

    def retourner(self, adherent):
        if self not in adherent.documents_empruntes:
            raise ValueError("Ce livre n'est pas emprunté par cet adhérent.")
        adherent.documents_empruntes.remove(self)
        self._changer_disponibilite(True)
        print(f"Le livre '{self.titre}' de {self.auteur} a été rendu par {adherent.nom} {adherent.prenom}.")

    def afficher_details(self):
        etat = "Disponible" if self.disponibilite else "Indisponible"
        print(f"{self.titre} |==| {self.auteur} |==| {etat}")

    def afficher_un_detail(self):
        etat = "Disponible" if self.disponibilite else "Indisponible"
        print(f"{self.titre} |==| {self.auteur} |==| {etat}")

    def chang_etat_non(self):
        print("Modification directe interdite.")