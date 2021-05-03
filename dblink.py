########################
#     bibliothèque
#   pour gérer la bdd
########################

import sqlite3 as sq3

# Connexion à la bdd
connexion = sq3.connect("banque.db")

# Curseur
cursor = connexion.cursor()


# Définition des classes
class User():
    def __init__(self, idCompte, identifiant, mdp):
        self.idCompte = idCompte
        self.identifiant = identifiant
        self.mdp = mdp


class Compte():
    def __init__(self, idCompte, nom, prenom, solde, sexe, naiss):
        self.idCompte = idCompte
        self.nom = nom
        self.prenom = prenom
        self.solde = solde
        self.sexe = sexe
        self.naiss = naiss


def requete_perso(requete: str):
    """
    Fonction qui renvoie la réponse à la requête entrée
    A ne pas utiliser de préférence
    
    Parameters
    ----------
    requete : str
        Requête demandée
        
    Returns
    -------
    reponse : sqlite3.execute (?)
        Réponse à la requête
    
    None : python.None
        En cas d'erreur
    
    """
    print(f"Nouvelle requête !")
    rep = list(cursor.execute(requete))
    return rep


def get_compte(idCompte):
    """
    Renvoie le compte de l'utilisateur
    
    Parameters
    ----------
    idCompte : int
        L'ID du compte client
        
    Returns
    -------
    Compte : Compte object
        Classe Compte crée afin que ce soit plus simple
    
    """

    rep = list(cursor.execute("SELECT * FROM compte WHERE idCompte=?",
                              (idCompte,)))

    if len(rep) == 0:
        return "Aucun compte trouvé"

    for row in rep:
        compte = Compte(rep[0][0],
                        rep[0][1],
                        rep[0][2],
                        rep[0][3])
        return compte


def get_user_connexion(idCompte):
    """
    Renvoie les identifiants de l'utilisateur
    
    Parameters
    ----------
    idCompte : int
        L'ID du compte du client
        
    Returns
    -------
        User : User object
            Classe User crée pour pouvoir accéder à tous les attributs en
            une seule variabale
    
    """

    rep = list(cursor.execute("SELECT * FROM connexion WHERE idCompte=?",
                              (idCompte,)))

    if len(rep) == 0:
        return False, "Aucun compte n'a été trouvé"

    for row in rep:
        user_connexion = User(rep[0][0],
                              rep[0][1],
                              rep[0][2])
        return user_connexion


def insert_user_data(nom, prenom, sexe, naiss, identifiant, mdp, solde=0):
    """
    Crée un compte utilisateur en l'insérant dans la base de données

    Parameters
    ----------
    nom         : str   --> Nom du nouvel utilisateur
    prenom      : str   --> Prénom du nouvel utilisateur
    sexe        : str   --> Sexe du nouvel utilisateur. Ne peut prendre que "F"(féminin) ou "M"(masculin) en valeur
    naiss       : str   --> Date de naissance du nouvel utilisateur. Ne peut prendre que AAAA-MM-JJ en valeur
    identifiant : str   --> identifiant de connexion du nouvel utilisateur
    mdp         : str   --> mot de passe de connexion du nouvel utilisateur
    solde       : int   --> Solde du nouvel utilisateur. 0 est la valeur par défaut

    """
    try:

        req1 = requete_perso("SELECT idCompte FROM connexion ORDER BY idCompte DESC")

        idCompte = req1[0][0] + 1   # On prend le dernier idCompte de la bdd (=[0][0])
                                    # Et on rajoute 1 pour le nouveau compte

        req2 = "INSERT INTO compte VALUES(?,?,?,?,?,?)"
        data_to_insert = (idCompte, nom, prenom, solde, sexe, naiss)

        req3 = "INSERT INTO connexion VALUES(?,?,?)"
        data_to_insert2 = (idCompte, identifiant, mdp)

        cursor.execute(req2, data_to_insert)
        cursor.execute(req3, data_to_insert2)
        connexion.commit()
        print("Compte inséré dans la base de données avec succès.")

    except Exception as e:

        print("Une erreur est survenue :", e)

insert_user_data("bodin", "bastien", "M","2004-11-10", "babibou", "babou")
print(requete_perso("SELECT nom,prenom FROM compte ORDER BY idCompte DESC"))
