# Biblio-Tech - Documentation Technique

Ce document détaille l'architecture technique et le fonctionnement du système de gestion de bibliothèque **Biblio-Tech**. Ce projet a été conçu en respectant les piliers de la Programmation Orientée Objet (POO) et intègre une persistance des données via une base de données MySQL.

## Architecture Globale

Le projet est structuré autour de classes modèles (`Livre`, `Magazine`, `Adherent`) héritant pour certaines d'une classe abstraite (`Document`). L'interaction utilisateur est gérée par la classe `Menu` dans `main.py`, qui assure la liaison avec la base de données MySQL pour la persistance des informations.

## Détail des Classes et Méthodes

### 1. `abstraite.py` : Le contrat d'interface

Ce fichier définit la classe de base du système.

#### Classe `Document(ABC)`
Classe abstraite héritant de `ABC` (Abstract Base Class). Elle ne peut pas être instanciée directement et impose une structure aux classes filles.

*   **`__init__(self, titre: str)`** : Constructeur initialisant le titre et définissant l'attribut privé `__disponibilite` à `True` par défaut.
*   **`@property titre`** : Accesseur (getter) pour le titre.
*   **`@property disponibilite`** : Accesseur pour l'état de disponibilité. L'attribut étant privé (`__disponibilite`), il est inaccessible directement de l'extérieur (Encapsulation).
*   **`_changer_disponibilite(self, etat)`** : Méthode protégée permettant de modifier l'état interne. Elle est destinée à être utilisée uniquement par les méthodes internes des sous-classes.
*   **Méthodes abstraites (`emprunter`, `retourner`, `afficher_details`, etc.)** : Ces méthodes n'ont pas d'implémentation dans `Document`. Elles obligent toutes les sous-classes (`Livre`, `Magazine`) à fournir leur propre logique.

### 2. `livre.py` : Implémentation concrète pour les Livres

Gère la logique spécifique aux livres.

#### Classe `Livre(Document)`
*   **`__init__(self, titre, auteur)`** : Appelle le constructeur parent pour le titre et initialise l'attribut spécifique `auteur`.
*   **`emprunter(self)`** : Tente d'emprunter le livre.
    *   Vérifie la disponibilité via la propriété.
    *   Si indisponible, lève une `ValueError` ("Le livre est déjà emprunté").
    *   Si disponible, utilise `_changer_disponibilite(False)` pour verrouiller le livre.
*   **`retourner(self)`** : Tente de rendre le livre.
    *   Si déjà disponible, lève une `ValueError`.
    *   Sinon, rétablit la disponibilité.
*   **`afficher_details(self)`** : Affiche les détails formatés : `Titre |==| Auteur |==| État`.
*   **`chang_etat_non(self)`** : Méthode de sécurité explicite pour signaler que la modification directe de l'état est interdite.

### 3. `magazine.py` : Implémentation concrète pour les Magazines

Gère la logique spécifique aux magazines.

#### Classe `Magazine(Document)`
*   **`__init__(self, titre, numero_edition)`** : Initialise le titre et le `numero_edition`.
*   **`emprunter(self)` / `retourner(self)`** : Logique identique à celle du livre, mais avec des messages adaptés au type "Magazine".
*   **`afficher_details(self)`** : Affiche les détails formatés : `Titre |==| Numéro d'édition |==| État`.

### 4. `adherent.py` : Gestion des Utilisateurs

Représente les membres de la bibliothèque.

#### Classe `Adherent`
*   **`__init__(self, nom, prenom, Telephone)`** : Initialise les informations personnelles de l'adhérent.
*   **`documents_empruntes`** : Liste permettant de suivre les documents actuellement en possession de l'adhérent.

### 5. `connexion.py` : Couche de Persistance

Ce fichier gère la connexion technique à la base de données.
*   Initialise l'objet `conn` (connexion MySQL) et le `cursor` permettant l'exécution des requêtes SQL dans l'ensemble de l'application.

### 6. `bibliothecaire.py` : Logique Métier

Cette classe peut agir comme gestionnaire en mémoire pour certaines opérations logiques sur le catalogue.

#### Classe `Bibliothécaire`
*   **Gestion du catalogue** : Méthodes pour ajouter, supprimer et rechercher des documents dans une liste locale.
*   **Gestion des adhérents** : Méthodes pour lister et gérer les adhérents en mémoire.

### 7. `main.py` : Contrôleur Principal et Interface

Point d'entrée de l'application, gérant l'interaction utilisateur et les transactions avec la base de données.

#### Classe `Menu`
*   **`authentification(self)`** : Système de connexion sécurisé.
    *   Utilise la bibliothèque **`bcrypt`** pour hacher et vérifier les mots de passe.
    *   Interroge la table `Bibliothecaire` pour valider les accès.
*   **`afficher_menu(self)`** : Boucle infinie (`while True`) présentant les options.
    *   **Gestion des choix (`match/case`)** :
        *   **Cas 1 & 2 (Ajout)** : Instancie un `Livre` ou un `Magazine` et l'insère dans la base de données (`INSERT INTO`).
        *   **Cas 3 (Emprunt)** : Vérifie la disponibilité via SQL, met à jour le statut du document et enregistre l'emprunt.
        *   **Cas 7, 8, 9 (Adhérents)** : Gestion complète (Ajout, Suppression, Affichage) des adhérents via requêtes SQL.

## Concepts Clés

1.  **Programmation Orientée Objet** : Utilisation de l'héritage (`Document`), de l'encapsulation et du polymorphisme pour structurer le code.
2.  **Persistance des Données** : Utilisation de **MySQL** pour stocker durablement les livres, magazines, adhérents et emprunts, remplaçant le stockage volatile en mémoire.
3.  **Sécurité** : Intégration de **bcrypt** pour la protection des mots de passe et prévention des accès non autorisés.
4.  **Intégrité des Données** : Le système vérifie la disponibilité des documents en base de données avant d'autoriser un emprunt.