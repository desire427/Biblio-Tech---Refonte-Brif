class Bibliothécaire:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = []

    def ajouter_document(self, document):
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
            doc.affichier_un_detail()
