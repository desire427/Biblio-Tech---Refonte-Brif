from bibliothecaire import Bibliothécaire
from livre import Livre
from magazine import Magazine



class Menu:
    
    biblio = Bibliothécaire("Bassirou")

    def afficher_menu(self):
        while True:
            print("\n===== MENU =====")
            print("1 - Ajouter un Livre")
            print("2 - Ajouter un Magazine")
            print("3 - Emprunter un document")
            print("4 - Retourner un document")
            print("5 - Afficher le catalogue")
            print("6 - Changer l'etat")
            print("7. Supprimer un Document")
            print("8 - Quitter")

            choix = input("Votre choix : ")

            match choix:
                
                case "1":
                    titre = input("Titre du livre : ")
                    auteur = input("Auteur du livre : ")
                    livre = Livre(titre, auteur)
                    self.biblio.ajouter_document(livre)
                case "2":
                    titre = input("Titre du magazine : ")
                    numero_edition = input("Numéro de l'édition : ")
                    magazine = Magazine(titre, numero_edition)
                    self.biblio.ajouter_document(magazine)
                case "3":
                    try:
                        self.biblio.lister_documents()
                        titre = input("Titre du document:").strip()
                        document = self.biblio.recherche_par_titre(titre)
                        if document:
                            document.emprunter()
                        else:
                            print(f"Document non emprunter.")
                    except ValueError as e:
                        print(e)
                case "4":
                    try:
                        titre = input("Titre du document: ").strip()
                        document= self.biblio.recherche_par_titre(titre)
                        if document:
                            document.retourner()
                    except ValueError as e:
                        print(e)
                case "5":
                    self.biblio.lister_documents()
                case "6":
                    print("Modification directe de l'état interdite.")
                case "7":
                    titre=input("Entrez le titre du document a supprimer")
                    self.biblio.supprimer_document(titre)

                case "8":
                    print("Au revoir !")
                    break
            
                case _:
                    print("Choix invalide. Veuillez réessayer.")
                


menu = Menu()
menu.afficher_menu()