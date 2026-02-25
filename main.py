from bibliothecaire import Bibliothécaire
from livre import Livre
from magazine import Magazine
from adherent import Adherent
from connection import cursor , conn






class Menu:
    
    biblio = Bibliothécaire("Biblio-Tech")

    def afficher_menu(self):
        while True:
            print("\n===== MENU =====")
            print("1 - Ajouter un Livre")
            print("2 - Ajouter un Magazine")
            print("3 - Emprunter un document")
            print("4 - Retourner un document")
            print("5 - Afficher le catalogue")
            print("6 - Changer l'état")
            print("7 - ajouter un adherent")
            print("8 - Supprimer un adherent")
            print("9 - Afficher les adhérents")
            print("10. Supprimer un Document")
            print("0 - Quitter")

            choix = input("Votre choix : ")

            match choix:
                
                case "1":
                    titre = input("Titre du livre : ")
                    auteur = input("Auteur du livre : ")
                    livre = Livre(titre, auteur)
                    # self.biblio.ajouter_document(livre)
                    sql = " INSERT INTO Livres(titre, auteur) VALUES(%s, %s)"
                    val = (livre.titre, livre.auteur)
                    cursor.execute(sql, val)
                    conn.commit()
                    print(f"'{livre.titre}' a été ajouté à la bibliothèque.")
                case "2":
                    titre = input("Titre du magazine : ")
                    numero_edition = input("Numéro de l'édition : ")
                    magaz = Magazine(titre, numero_edition)
                    # self.biblio.ajouter_document(magazine)
                    sql = " INSERT INTO Magazines(titre, numero_edition) VALUES(%s, %s)"
                    val = (magaz.titre, magaz.numero_edition)
                    cursor.execute(sql, val)
                    conn.commit()
                    print(f"'{magaz.titre}' a été ajouté à la bibliothèque.")
                case "3":
                    try:
                        self.biblio.lister_documents()
                        titre = input("Titre du document:").strip()
                        id_ad = input("ID de l'adhérent : ")
                        sql = "select * from Adherents"
                        cursor.execute(sql,)
                        lis_ad=cursor.fetchall()

                        adherent = None
                        for a in lis_ad:
                            if str(a[0]) == id_ad:
                                adherent = Adherent(a[1], a[2], id=a[0])
                                break
                        if not adherent:
                            print("Adhérent non trouvé.")
                        else:
                            # document = self.biblio.recherche_par_titre(titre)
                            sql="select disponibilite from Magazines"
                            cursor.execute(sql,)
                            disponibilite=cursor.fetchone()[0]
                            if disponibilite=='Indisponible':
                                print("Livre est deja Emprunté")
                                
                            else:
                                sql = " SELECT titre, auteur FROM Livres WHERE titre = %s UNION SELECT titre, numero_edition FROM Magazines WHERE titre = %s"
                                cursor.execute(sql, (titre, titre))
                                document = cursor.fetchone()
                                if document:
                                    # document.emprunter(adherent)
                                    sql = " INSERT INTO Emprunts(titre, id_adherent) VALUES(%s, %s)"
                                    val = (document[0], adherent.id)
                                    cursor.execute(sql, val)
                                    conn.commit()
                                    cursor.execute("UPDATE Livres SET disponibilite = 'Indisponible' WHERE titre = %s", (document[0],))
                                    cursor.execute("UPDATE Magazines SET disponibilite = 'Indisponible' WHERE titre = %s", (document[0],))
                                    conn.commit()
                                    print(f"Le document '{document[0]}' a été emprunté par {adherent.nom} {adherent.prenom}.")
                                    break
                                else:
                                    print(f"Document non trouvé.")
                    except ValueError as e:
                        print(e)
                case "4":
                    try:
                        titre = input("Titre du document: ").strip()
                        sql = " SELECT titre FROM Livres WHERE titre = %s UNION SELECT titre FROM Magazines WHERE titre = %s"
                        cursor.execute(sql, (titre, titre))
                        document = cursor.fetchone()
                        # document = self.biblio.recherche_par_titre(titre)
                        if document:
                            # document.retourner(adherent)
                            cursor.execute("UPDATE Livres SET disponibilite = 'Disponible' WHERE titre = %s", (document[0],))
                            cursor.execute("UPDATE Magazines SET disponibilite = 'Disponible' WHERE titre = %s", (document[0],))
                            # cursor.execute("DELETE FROM Emprunts WHERE titre = %s", (document[1],))
                            conn.commit()
                            print(f"Le document '{document[0]}' a été rendu.")
                        else:
                            print(f"Document non trouvé.")
                    except ValueError as e:
                        print(e)  
                case "5":
                    # self.biblio.lister_documents()
                    sql = "SELECT titre, auteur FROM Livres UNION SELECT titre, numero_edition FROM Magazines"
                    cursor.execute(sql)
                    for ligne in cursor.fetchall():
                        print(ligne)

                case "6":
                    print("Modification directe de l'état interdite.")
                case "7":
                    nom = input("Nom de l'adhérent : ")
                    prenom = input("Prénom de l'adhérent : ")
                    adherent = Adherent(nom, prenom)
                    # self.biblio.ajouter_adherent(adherent)
                    sql = " INSERT INTO Adherents(nom, prenom) VALUES(%s, %s)"
                    val = (adherent.nom, adherent.prenom)
                    cursor.execute(sql, val)
                    conn.commit()
                    print(f"{adherent.nom} {adherent.prenom} a été ajouté comme adhérent.")
                case "8":
                    nom = input("Nom de l'adhérent : ")
                    prenom = input("Prénom de l'adhérent : ")
                    adherent = Adherent(nom, prenom)
                    # self.biblio.supprimer_adherent(adherent)
                    sql = " DELETE FROM Adherents WHERE nom = %s AND prenom = %s"
                    cursor.execute(sql, (adherent.nom, adherent.prenom))
                    conn.commit()
                    print(f"{adherent.nom} {adherent.prenom} a été supprimé comme adhérent.")
                case "9":
                    sql="select * from Adherents"
                    cursor.execute(sql,)
                    resultats=cursor.fetchall()
                    for ligne in resultats:
                        print(f"Nom : {ligne[1]} == Prénom: {ligne[2]}")

                    #self.biblio.lister_adherents()
                
                case "10":
                    titre=input("Entrez le titre du document a supprimer")
                    # self.biblio.supprimer_document(titre)
                    sql = " DELETE FROM Livres WHERE titre = %s"
                    cursor.execute(sql, (titre,))
                    conn.commit()
                    print(f"'{titre}' a été supprimé de la bibliothèque.")

                case "0":
                    print("Au Revoir")
                    cursor.close()
                    conn.close()
                    break
            
                case _:
                    print("Choix invalide. Veuillez réessayer.")
                


menu = Menu()
menu.afficher_menu()