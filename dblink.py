########################
#     bibliothèque
#   pour gérer la bdd
########################

"""
Fait de A à Z par Bastien
Voir issues sur github pour la liste des bugs du projet.
"""

# Importation des bibliothèques
import sqlite3 as sq3
import datetime

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


def insert_user_data(nom, prenom, sexe, naiss, mdp, solde=0):
    """
    Crée un compte utilisateur en l'insérant dans la base de données

    Parameters
    ----------
    nom         : str   --> Nom du nouvel utilisateur
    prenom      : str   --> Prénom du nouvel utilisateur
    sexe        : str   --> Sexe du nouvel utilisateur. Ne peut prendre que "F"(féminin) ou "M"(masculin) en valeur
    naiss       : str   --> Date de naissance du nouvel utilisateur. Ne peut prendre que AAAA-MM-JJ en valeur
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
        data_to_insert2 = (idCompte, nom, mdp)

        cursor.execute(req2, data_to_insert)
        cursor.execute(req3, data_to_insert2)
        connexion.commit()
        print("Compte inséré dans la base de données avec succès.")

    except Exception as e:

        print("Une erreur est survenue :", e)
        

def is_user_exist(identifiant, mdp):
    """
    Fonction qui vérifie si un utilisateur est dans la base de données ou non.
    
    Parameters
    ----------
    identifiant : str   --> l'identifiant entré par l'utilisateur
    mdp         : str   --> le mot de passe entré par l'utilisateur
    
    Returns
    -------
    idCompte : int       --> L'idCompte de l'utilisateur dans la bdd
    False    : Boolean   --> Si le compte n'existe pas dans la bdd
    
    """
    try :
        req = "SELECT * FROM connexion"
        res = requete_perso(req)
        
        # res est une liste de tuples comportant l'identifiant et le mdp
        for elem in res:
            if elem[1] == identifiant and elem[2] == mdp:
                return elem[0]
            
        return False
    except Exception as e:
        return "Une erreur est survenue :", e
    

def virement(donne,recoit,montant):
    """
    Foncction qui effetue un virement d'un compte à l'autre.
    
    Parameters
    ----------
    donne   : int   --> L'idCompte de la personne qui donne l'argent
    recoit  : int   --> L'idCompte de la personne qui reçoit l'argent
    montant : int   --> Le montant du virement
    
    Returns
    -------
    True : boolean   --> Si la transaction a bien été effetuée
    (False, error) : tuple   --> Si la transaction n'a pas pu être effetuée
                                --> Renvoie False
                                --> Renvoie l'erreur

    Bugs
    ----
    Problème de date : elle affiche la bonne date du virement sous le format demandé,
    mais dans la base de données n'indique que "1991". La seule supposition possible peut être due
    au fait de l'encodage du sgbd en 32 bits qui créerait un problème lors de l'insertion
    
    """
    try:
        req_solde_compte1 = f"SELECT solde FROM compte WHERE idCompte={donne}"
        req_solde_compte2 = f"SELECT solde FROM compte WHERE idCompte={recoit}"

        rep_req1 = requete_perso(req_solde_compte1)
        rep_req2 = requete_perso(req_solde_compte2)

        nouveau_solde1 = rep_req1[0][0]-montant
        nouveau_solde2 = rep_req2[0][0]+montant

        req_update_compte1 = f"UPDATE compte SET solde={nouveau_solde1} WHERE idCompte={donne}"
        req_update_compte2 = f"UPDATE compte SET solde={nouveau_solde2} WHERE idCompte={recoit}"

        requete_perso(req_update_compte1)
        requete_perso(req_update_compte2)

        maintenant = datetime.datetime.now().strftime("%Y-%m-%d")
        print(type(maintenant))

        print(maintenant)

        req_virement = f"INSERT INTO virements VALUES({donne},{recoit},{montant},{maintenant})"
        requete_perso(req_virement)

        connexion.commit()

        return True
    except Exception as e:
        return False, e
