########################
#     bibliothèque
#   pour gérer la bdd
########################

import sqlite3 as sq3

# Connexion à la bdd
connexion = sq3.connect("banque.db")

# Curseur
cursor = connexion.cursor()

def requete_perso(requete:str):
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
    print(requete)
    for ligne in cursor.execute(requete):
        print(ligne)
        
    
def get_compte(idCompte):
    """
    Renvoie le compte de l'utilisateur
    
    Parameters
    ----------
    idCompte = int
        L'ID du compte client
        
    Returns
    -------
    Compte : Compte object
        Classe Compte crée afin que ce soit plus simple
    
    """
    class Compte:
        """
        Classe compte qui regroupe toutes les informations sur le compte
        Classe à mettre dans un autre fichier séparé pour y accéder dans
        d'autres fichiers
        """
        def __init__(self,idCompte,nom,prenom,solde):
            self.idCompte = idCompte
            self.nom = nom
            self.prenom = prenom
            self.solde = solde
            
            
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
    idCompte = int
        L'ID du compte du client
        
    Returns
    -------
        User = User object
            Classe User crée pour pouvoir accéder à tous les attributs en
            une seule variabale
    
    """
    class User():
        def __init__(self,idCompte,identifiant,mdp):
            self.idCompte = idCompte
            self.identifiant = identifiant
            self.mdp = mdp
            
    
    rep = list(cursor.execute("SELECT * FROM connexion WHERE idCompte=?",
                              (idCompte,)))
    
    if len(rep) == 0:
        return False,"Aucun compte n'a été trouvé"
    
    for row in rep:
        user_connexion = User(rep[0][0],
                              rep[0][1],
                              rep[0][2])
        return user_connexion
