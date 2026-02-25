class Adherent:
    def __init__(self, nom, prenom, id=None):
        self.id = id
        self.nom = nom
        self.prenom=prenom
        self.documents_empruntes = []
        