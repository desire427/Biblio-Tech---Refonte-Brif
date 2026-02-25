class Adherent:
    def __init__(self, nom, prenom,Telephone, id=None):
        self.id = id
        self.nom = nom
        self.prenom=prenom
        self.Telephone=Telephone
        self.documents_empruntes = []
        