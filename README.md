# Biblio-Tech - Documentation Technique

Ce document détaille l'architecture technique et le fonctionnement du système de gestion de bibliothèque **Biblio-Tech**. Ce projet a été refondu pour respecter strictement les piliers de la Programmation Orientée Objet (POO) : Abstraction, Encapsulation et Polymorphisme.

## Architecture Globale

Le projet est structuré autour d'une classe abstraite parente (`Document`) et de classes enfants concrètes (`Livre`, `Magazine`), gérées par un contrôleur (`Bibliothécaire`) et accessibles via une interface console (`Menu`).

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

### 4. `bibliothecaire.py` : Le Gestionnaire

Cette classe agit comme le chef d'orchestre. Elle manipule des objets `Document` sans avoir besoin de connaître leur type précis (Polymorphisme).

#### Classe `Bibliothécaire`
*   **`__init__(self, nom)`** : Initialise le nom du bibliothécaire et crée une liste vide `catalogue`.
*   **`ajouter_document(self, document)`** : Ajoute un objet au catalogue.
    *   Vérifie d'abord si un document avec le même titre existe déjà pour éviter les doublons.
*   **`supprimer_document(self, titre)`** : Parcourt le catalogue, trouve le document correspondant au titre et le retire de la liste.
*   **`recherche_par_titre(self, titre)`** : Recherche un document.
    *   Effectue une comparaison insensible à la casse et aux espaces (`lower().replace(" ", "")`) pour une meilleure expérience utilisateur.
    *   Retourne l'objet `Document` trouvé ou affiche un message si non trouvé.
*   **`lister_documents(self)`** : Affiche l'inventaire complet.
    *   Boucle sur le catalogue et appelle `doc.afficher_details()`. Grâce au polymorphisme, Python exécute la version de la méthode correspondant au type réel de l'objet (Livre ou Magazine).

### 5. `main.py` : L'Interface Utilisateur

Gère l'interaction avec l'utilisateur via la console.

#### Classe `Menu`
*   **`afficher_menu(self)`** : Boucle infinie (`while True`) présentant les options.
    *   **Gestion des choix (`match/case`)** :
        *   **Cas 1 & 2 (Ajout)** : Instancie un `Livre` ou un `Magazine` et demande au bibliothécaire de l'ajouter.
        *   **Cas 3 (Emprunt)** :
            1. Recherche le document par titre.
            2. Si trouvé, appelle `document.emprunter()`.
            3. Capture l'exception `ValueError` si le document est déjà emprunté et affiche l'erreur proprement.
        *   **Cas 4 (Retour)** : Similaire à l'emprunt, appelle `document.retourner()`.
        *   **Cas 6 (Sécurité)** : Démontre l'interdiction de modification directe.

## Concepts Clés

1.  **Uniformisation** : Le catalogue contient des objets mixtes (`Livre`, `Magazine`) stockés dans une même liste grâce à leur héritage commun de `Document`.
2.  **Sécurité des Données** : L'état `__disponibilite` est inaccessible depuis `main.py`. Le menu doit obligatoirement passer par les méthodes `emprunter()` ou `retourner()`, garantissant l'intégrité des données.
3.  **Évolutivité** : Pour ajouter un nouveau type (ex: DVD), il suffit de créer une classe `DVD(Document)`. Le `Bibliothécaire` n'aura pas besoin d'être modifié pour gérer ce nouveau type.