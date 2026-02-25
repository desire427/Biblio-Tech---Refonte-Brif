class Bibliothécaire:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = []
        self.adherents = []


    def ajouter_document(self,document):
        for doc in self.catalogue:
            if doc.titre == document.titre:
                print(f"Le document '{document.titre}' existe déjà dans la bibliothèque.")
                return
        self.catalogue.append(document)
        print(f"'{document.titre}' a été ajouté à la bibliothèque.")

    def supprimer_document(self, titre):
        for doc in self.catalogue:
            if doc.titre == titre:
                self.catalogue.remove(doc)
                print(f"'{titre}' a été supprimé de la bibliothèque.")
                return
        print(f"Document '{titre}' non trouvé.")

    def recherche_par_titre(self, titre):
        for doc in self.catalogue:
            if doc.titre.lower().replace(" ", "") == titre.lower().replace(" ", ""):
                return doc
        print(f"Document '{titre}' non trouvé.")


    def lister_documents(self):
        print(f"\nInventaire de {self.nom} :")
        for doc in self.catalogue:
            doc.afficher_details()

    def lister_un_document(self):
        print(f"\nInventaire de {self.nom} :")
        for doc in self.catalogue:
            doc.afficher_un_detail()

    def ajouter_adherent(self, adherent):
        for a in self.adherents:
            if a.nom == adherent.nom and a.prenom == adherent.prenom:
                print(f"{adherent.nom} {adherent.prenom} est déjà un adhérent.")
                return
        self.adherents.append(adherent)
        print(f"{adherent.nom} {adherent.prenom} a été ajouté comme adhérent.")

    def supprimer_adherent(self, adherent):
        if adherent not in self.adherents:
            print(f"{adherent.nom} {adherent.prenom} n'est pas un adhérent.")
            return
        self.adherents.remove(adherent)
        print(f"{adherent.nom} {adherent.prenom} a été supprimé comme adhérent.")

    def lister_adherents(self):
        print(f"\nListe des adhérents de {self.nom} :")
        for adherent in self.adherents:
            print(f"{adherent.nom} {adherent.prenom}")
