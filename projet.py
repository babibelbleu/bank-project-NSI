# Projet de NSI en terminale 2021 Quentin Kimppienne, Bodin Bastien
# Projet : création d'une fausse application bancaire avec une monnaie fictive

from tkinter import *
from tkinter import ttk, Menu
from tkinter import Entry, Frame
from tkinter import messagebox
import time
import dblink


# fonctions pour supprimer tout les widget d'un page
def effacer():
    for widget in frame.winfo_children():
        widget.destroy()


def effacer_crea():
    if var_mot_de_passe2 is None or var_prenom is None or var_nom is None or date is None or sexe is None:
        messagebox.showerror("Erreur", "Vous n'avez pas remplie tout les critére")
    else:
        for widget in frame.winfo_children():
            widget.destroy()
    dblink.insert_user_data(str(var_nom), str(var_prenom), str(sexe), date, str(var_mot_de_passe2))


def connecte_crea():
    global mon_menu
    mon_menu = Menu(windows)
    windows.config(menu=mon_menu, bg='#41B77F')
    file_menu = Menu(mon_menu)
    mon_menu.add_cascade(label="Information personnelle", menu=file_menu)
    file_menu.add_command(label="Information personnelle", command=lambda: [effacer(), info()])

    menu_depense = Menu(mon_menu)
    mon_menu.add_cascade(label="Compte", menu=menu_depense)
    menu_depense.add_command(label="Compte", command=lambda: [effacer(), compte()])
    menu_depense.add_command(label="Dépense", command=lambda: [effacer(), depense()])

    menu_deco = Menu(mon_menu)
    mon_menu.add_cascade(label="Paramêtre", menu=menu_deco)
    menu_deco.add_command(label="Paramêtre", command=lambda: [effacer(), parametre()])
    menu_deco.add_command(label="Déconnexion", command=lambda: [effacer(), delete(), page_compte()])

    label_slogan1 = Label(frame, text="La banque de tous les lycéens sauf les Littéraires",
                          font=("Damion", 20), bg='#41B77F')
    label_slogan1.pack()

    width3 = 100
    height3 = 100
    image3 = PhotoImage(file='data-science.png').zoom(5).subsample(32)
    canvas3 = Canvas(frame, width=width3, height=height3, bg='#41B77F', bd=0, highlightthickness=0)
    canvas3.create_image(width / 2, height / 2, image=image3)
    canvas3.pack()

    label = Label(frame, text=("Bienvenue Monsieur", str(var_prenom), "."),
                  font=("Damion", 35), bg='#41B77F')
    label.pack()

    # création d'une animation
    can = Canvas(frame, height=400, width=1080, bg='#007FFF', bd=1)
    can.pack(pady=50)
    can.create_rectangle(50, 50, 1030, 350, fill='black')
    ball = can.create_oval(100, 100, 150, 150, fill='yellow')
    x = 1
    y = 2

    while True:
        try:
            can.move(ball, x, y)
            time.sleep(0.001)
            can.update()
            if can.coords(ball)[0] <= 50 or can.coords(ball)[2] >= 1030:
                x = x * -1
            elif can.coords(ball)[1] <= 50 or can.coords(ball)[3] >= 350:
                y = y * -1
        except:
            break


# -------------------------------------------------------------------------------------------------------------------------
# Partie du code pour le compte en francais
def delete():
    mon_menu.delete("Information personnelle")
    mon_menu.delete("Compte")
    mon_menu.delete("Paramêtre")


# fonction pour créer page principales
def page_compte():
    # ajout slogan prémiére page
    label_slogancompte = Label(frame, text="La banque de tous les lycéens sauf les Littéraires",
                               font=("Damion", 20), bg='#41B77F')
    label_slogancompte.pack()

    # création images
    height2 = 100
    width2 = 100
    image2 = PhotoImage(file='data-science.png').zoom(5).subsample(32)
    canvas2 = Canvas(frame, width=width2, height=height2, bg='#41B77F', bd=0, highlightthickness=0)
    canvas2.create_image(width / 2, height / 2, image=image2)
    canvas2.pack()

    # crétion du demandeur de compte(nom utilisateur )
    label_titlecompte = Label(frame, text="Nom utilisateur", font=("Comic sans MS", 20),
                              bg='#41B77F', bd=0, highlightthickness=0)
    label_titlecompte.pack()

    # creation de la zone de texte pour le nom
    nom_entrycompte = Entry(frame, font=("Comic sans MS", 20), bg='#41B77F', fg='black')
    nom_entrycompte.pack()

    # creation de la zone de texte pour le nom
    label_titlecompte = Label(frame, text="mot de passe", font=("Comic sans MS", 20), bg='#41B77F',
                              bd=0, highlightthickness=0)
    label_titlecompte.pack()

    # creation de la zone de texte pour le mot de passe
    nom_entrycompte2 = Entry(frame, font=("Comic sans MS", 20), show='*', bg='#41B77F', fg='black')
    nom_entrycompte2.pack()

    # création bouton connexion
    button_co = Button(frame, text="connexion", font=("Comic sans MS", 20), bg='#007FFF',
                       fg='#40E0D0', activeforeground='#40E0D0', activebackground='#007FFF', bd='1',
                       command=lambda: [effacer(), page_connecte(), connecte()])
    button_co.pack(pady=5)

    # création bouton création compte
    button_compte = Button(frame, text="se créer un compte", font=("Comic sans MS", 20),
                           bg='#007FFF', fg='#40E0D0', activeforeground='#40E0D0', activebackground='#007FFF',
                           bd='1', command=lambda: [effacer(), creation_compte()])
    button_compte.pack(pady=5)

    # création bouton decoration
    button_deco1 = Button(frame, text="se créer un compte", font=("Comic sans MS", 20),
                          bg='#007FFF', fg='#40E0D0', activeforeground='#40E0D0', activebackground='#007FFF',
                          bd=500)
    button_deco1.pack(pady=5)


# fonction pour créer la page ou l'on peut créer son compte
def creation_compte():
    global var_mot_de_passe2
    global date
    global var_nom
    global var_prenom
    global sexe

    # création de la frame principale
    frame_crea = Frame(frame, bg='#41B77F')
    frame_crea2 = Frame(frame, bg='#41B77F')
    bottomframe = Frame(frame, bg='#41B77F')

    # ajout slogan prémiére page
    label_slogancrea = Label(frame_crea, text="La banque de tous les lycéens sauf les Littéraires",
                             font=("Damion", 20), bg='#41B77F')
    label_slogancrea.pack()

    # création images
    width1 = 100
    height1 = 100
    image1 = PhotoImage(file='data-science.png').zoom(5).subsample(32)
    canvas1 = Canvas(frame_crea, width=width1, height=height1, bg='#41B77F', bd=0, highlightthickness=0)
    canvas1.create_image(width / 2, height / 2, image=image1)
    canvas1.pack()

    # création du titre
    label_titlecrea = Label(frame_crea, text='Création du compte', bg='#41B77F',
                            font=("Damion", 25))
    label_titlecrea.pack()

    # texte
    texte = Label(frame_crea, text="Sexe", bg='#41B77F', font=("Damion", 15))
    texte.pack()
    # choix du sexe
    i = IntVar()
    check_homme = Radiobutton(frame_crea, text='Femme', value='1',
                              bg='#41B77F', variable=i)
    check_homme.pack()
    check_femme = Radiobutton(frame_crea, text='Homme', value='0',
                              bg='#41B77F', variable=i)
    check_femme.pack()

    if i.get() == 1:
        sexe = 'F'
    else:
        sexe = 'M'

    # nom/prénom/mot de passe
    var_nom = StringVar()
    label_nomcrea = Label(frame_crea, text="Nom", font=("Comic sans MS", 15),
                          bg='#41B77F')
    label_nomcrea.pack()

    nom_entry_creation = Entry(frame_crea, font=("Comic sans MS", 15),
                               textvariable=var_nom, bg='#41B77F', fg='black')
    nom_entry_creation.pack()

    var_prenom = StringVar()
    label_prenomcrea = Label(frame_crea, text="prenom", font=("Comic sans MS", 15),
                             bg='#41B77F')
    label_prenomcrea.pack()

    prenom_entry_creation = Entry(frame_crea, font=("Comic sans MS", 15), bg='#41B77F', fg='black',
                                  textvariable=var_prenom)
    prenom_entry_creation.pack()

    label_mot_de_passe = Label(frame_crea, text="mot de passe", font=("Comic sans MS", 15), bg='#41B77F')
    label_mot_de_passe.pack()

    var_mot_de_passe2 = StringVar()
    mot_de_passe_entry_creation = Entry(frame_crea, font=("Comic sans MS", 15),
                                        textvariable=var_mot_de_passe2,
                                        bg='#41B77F', fg='black', show='*')
    mot_de_passe_entry_creation.pack()

    # objet pour choisir date de naissance
    label = Label(frame_crea, text="Date de naissance",
                  font=("Comic sans MS", 20), bg='#41B77F')
    label.pack()

    # date de naissance
    texte_annee = Label(frame_crea2, text="Année", bg='#41B77F', font=("Damion", 15))
    texte_annee.grid(row=0, column=0)

    texte_mois = Label(frame_crea2, text="Mois", bg='#41B77F', font=("Damion", 15))
    texte_mois.grid(row=0, column=1)

    texte_jour = Label(frame_crea2, text="Jour", bg='#41B77F', font=("Damion", 15))
    texte_jour.grid(row=0, column=2)

    # crétion du truc pour demander la date de naissance
    annee_valeur = ["1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978",
                    "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987",
                    "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996",
                    "1997", "19998", "1999", "2000", "2001", "2002", "2003", "2004", "2005",
                    "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014",
                    "2015", "2016", "2017", "2018", "2019", "2020", "2021"]

    clicked_annee = StringVar()
    clicked_annee.set(annee_valeur[0])

    annee = OptionMenu(frame_crea2, clicked_annee, *annee_valeur)
    annee.grid(row=1, column=0)

    mois_valeur = ["01", "02", "03", "04", "05", "06", "07",
                   "08", "09", "10", "11", "12"]

    clicked_mois = StringVar()
    clicked_mois.set(mois_valeur[0])

    mois = OptionMenu(frame_crea2, clicked_mois, *mois_valeur)
    mois.grid(row=1, column=1)

    jour_valeur = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
                   "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25",
                   "26", "27", "28", "29", "30", "31"]

    clicked_jour = StringVar()
    clicked_jour.set(jour_valeur[0])

    jour = OptionMenu(frame_crea2, clicked_jour, *jour_valeur)
    jour.grid(row=1, column=2)

    # mise en place des variable pour créer le compte

    L = []
    L.append(str(clicked_annee))
    L.append(str(clicked_mois))
    L.append(str(clicked_jour))

    date = "-".join(L)

    # création du bouton de retour en arriéres
    button_retour = Button(bottomframe, text="retour",
                           font=("Comic sans MS", 15),
                           bg='#007FFF', fg='#40E0D0', activeforeground='#40E0D0',
                           activebackground='#007FFF', bd='1', command=lambda: [effacer(), page_compte()])
    button_retour.pack(side=RIGHT, padx=5)

    # création du bouton création du comte
    button_suite = Button(bottomframe, text="créer un compte",
                          font=("Comic sans MS", 15),
                          bg='#007FFF', fg='#40E0D0', activeforeground='#40E0D0',
                          activebackground='#007FFF', bd='1',
                          command=lambda: [effacer_crea(), connecte_crea()])
    button_suite.pack(side=LEFT)

    frame_crea.pack(expand=YES)
    frame_crea2.pack()
    bottomframe.pack(pady=9)


# fonction pour créer la pag du compte sur laquelle se trouve les info perso
def info():
    label_nom = Label(frame, text="Information a rajouter plus tard",
                      font=("Damion", 20), bg='#41B77F')
    label_nom.pack()


# fonction pour créer la page conenat les information sur le montant du compte
def compte():
    label_compte = Label(frame, text="Montant du compte a rajouter",
                         font=("Damion", 20), bg='#41B77F')
    label_compte.pack()


# fonction pour créer oa page pour envoyer de l'argent
def depense():
    label_receveur = Label(frame, text="Nom de la personne a qui envoyé de l'argent",
                           font=("Damion", 20), bg='#41B77F')
    label_receveur.pack()

    nom_entry_receveur = Entry(frame, font=("Comic sans MS", 20), bg='#41B77F', fg='black')
    nom_entry_receveur.pack()

    label_code = Label(frame, text="Identifiant du compte",
                       font=("Damion", 20), bg='#41B77F')
    label_code.pack()

    nom_entry_code = Entry(frame, font=("Comic sans MS", 20), bg='#41B77F', fg='black')
    nom_entry_code.pack()

    label_montant = Label(frame, text="Montant",
                          font=("Damion", 20), bg='#41B77F')
    label_montant.pack()

    nom_entry_montant = Entry(frame, font=("Comic sans MS", 20), bg='#41B77F', fg='black')
    nom_entry_montant.pack()

    button_envoie = Button(frame, text="Envoyer", font=("Comic sans MS", 20),
                           bg='#007FFF', fg='#40E0D0', activeforeground='#40E0D0', activebackground='#007FFF')
    button_envoie.pack()


# fonction pour créer la page servant a choisir la langue
def parametre():
    label = Label(frame, text="Choix de la langue: ",
                  font=("Damion", 20), bg='#41B77F')
    label.pack()

    button_francais = Button(frame, text='Francais', bg='#41B77F', font=("Comic sans MS", 15), )
    button_francais.pack(pady=5)

    button_anglais = Button(frame, text='Anglais', bg='#41B77F', font=("Comic sans MS", 15),
                            command=lambda: [effacer(), delete(), menu_anglais(), parametre_anglais()])
    button_anglais.pack(pady=5)

    button_espagnol = Button(frame, text='Espagnol', bg='#41B77F', font=("Comic sans MS", 15),
                             command=lambda: [effacer(), delete(), menu_espagnol(), parametre_espagnol()])
    button_espagnol.pack(pady=5)


# fontion qui crée la frame de la premiere page du compte lors de la connexion
def connecte():
    global mon_menu
    mon_menu = Menu(windows)
    windows.config(menu=mon_menu, bg='#41B77F')
    file_menu = Menu(mon_menu)
    mon_menu.add_cascade(label="Information personnelle", menu=file_menu)
    file_menu.add_command(label="Information personnelle", command=lambda: [effacer(), info()])

    menu_depense = Menu(mon_menu)
    mon_menu.add_cascade(label="Compte", menu=menu_depense)
    menu_depense.add_command(label="Compte", command=lambda: [effacer(), compte()])
    menu_depense.add_command(label="Dépense", command=lambda: [effacer(), depense()])

    menu_deco = Menu(mon_menu)
    mon_menu.add_cascade(label="Paramêtre", menu=menu_deco)
    menu_deco.add_command(label="Paramêtre", command=lambda: [effacer(), parametre()])
    menu_deco.add_command(label="Déconnexion", command=lambda: [effacer(), delete(), page_compte()])

    label_slogan1 = Label(frame, text="La banque de tous les lycéens sauf les Littéraires",
                          font=("Damion", 20), bg='#41B77F')
    label_slogan1.pack()

    width3 = 100
    height3 = 100
    image3 = PhotoImage(file='data-science.png').zoom(5).subsample(32)
    canvas3 = Canvas(frame, width=width3, height=height3, bg='#41B77F', bd=0, highlightthickness=0)
    canvas3.create_image(width / 2, height / 2, image=image3)
    canvas3.pack()

    label = Label(frame, text="Bienvenue Monsieur ...",
                  font=("Damion", 35), bg='#41B77F')
    label.pack()

    # création d'une animation
    can = Canvas(frame, height=400, width=1080, bg='#007FFF', bd=1)
    can.pack(pady=50)
    can.create_rectangle(50, 50, 1030, 350, fill='black')
    ball = can.create_oval(100, 100, 150, 150, fill='yellow')
    x = 1
    y = 2

    while True:
        try:
            can.move(ball, x, y)
            time.sleep(0.001)
            can.update()
            if can.coords(ball)[0] <= 50 or can.coords(ball)[2] >= 1030:
                x = x * -1
            elif can.coords(ball)[1] <= 50 or can.coords(ball)[3] >= 350:
                y = y * -1
        except:
            break


# -------------------------------------------------------------------------------------------------------------------------
# Partie du code pour le compte en Anglais
def depense_anglais():
    pass


def info_anglais():
    pass


def compte_anglais():
    pass


def delete_anglais():
    menu_anglais.delete("Personal information")
    menu_anglais.delete("Account")
    menu_anglais.delete("Settings")


def parametre_anglais():
    label_anglais = Label(frame, text="Choice of language: ",
                          font=("Damion", 20), bg='#41B77F')
    label_anglais.pack()

    button_francais1 = Button(frame, text='French', bg='#41B77F', font=("Comic sans MS", 15),
                              command=lambda: [effacer(), delete_anglais(), page_connecte(), parametre()])
    button_francais1.pack(pady=5)

    button_anglais1 = Button(frame, text='English', bg='#41B77F', font=("Comic sans MS", 15))
    button_anglais1.pack(pady=5)

    button_espagnol1 = Button(frame, text='Spanish', bg='#41B77F', font=("Comic sans MS", 15),
                              command=lambda: [effacer(), delete_anglais(), menu_espagnol(), parametre_espagnol()])
    button_espagnol1.pack(pady=5)


def menu_anglais():
    global menu_anglais
    menu_anglais = Menu(windows)
    windows.config(menu=menu_anglais, bg='#41B77F')
    file_anglais = Menu(menu_anglais)
    menu_anglais.add_cascade(label="Personal information", menu=file_anglais)
    file_anglais.add_command(label="Personal information", command=lambda: [effacer(), info_anglais()])

    menu_depense_anglais = Menu(menu_anglais)
    menu_anglais.add_cascade(label="Account", menu=menu_depense_anglais)
    menu_depense_anglais.add_command(label="Account", command=lambda: [effacer(), compte_anglais()])
    menu_depense_anglais.add_command(label="Spent", command=lambda: [effacer(), depense_anglais()])

    menu_deco_anglais = Menu(menu_anglais)
    menu_anglais.add_cascade(label="Settings", menu=menu_deco_anglais)
    menu_deco_anglais.add_command(label="Settings", command=lambda: [effacer(), parametre_anglais()])
    menu_deco_anglais.add_command(label="Déconnexion", command=lambda: [effacer(), delete_anglais(), page_compte()])


# -------------------------------------------------------------------------------------------------------------------------
# Partie du code pour le compte en Espagnom
def depense_espagnol():
    pass


def info_espagnol():
    pass


def compte_espagnol():
    pass


def delete_espagnol():
    menu_espagnol.delete("Informacion personal")
    menu_espagnol.delete("Cuenta")
    menu_espagnol.delete("Configuraciones")


def parametre_espagnol():
    label_espagnol = Label(frame, text="Datos personales: ",
                           font=("Damion", 20), bg='#41B77F')
    label_espagnol.pack()

    button_francais2 = Button(frame, text='Francés', bg='#41B77F', font=("Comic sans MS", 15),
                              command=lambda: [effacer(), delete_espagnol(), page_connecte(), parametre()])
    button_francais2.pack(pady=5)

    button_anglais2 = Button(frame, text='Inglés', bg='#41B77F', font=("Comic sans MS", 15),
                             command=lambda: [effacer(), delete_espagnol(), menu_anglais(), parametre_anglais()])
    button_anglais2.pack(pady=5)

    button_espagnol2 = Button(frame, text='Español', bg='#41B77F', font=("Comic sans MS", 15))
    button_espagnol2.pack(pady=5)


def menu_espagnol():
    global menu_espagnol
    menu_espagnol = Menu(windows)
    windows.config(menu=menu_espagnol, bg='#41B77F')
    file_espagnol = Menu(menu_espagnol)
    menu_espagnol.add_cascade(label="Informacion personal", menu=file_espagnol)
    file_espagnol.add_command(label="informacion personal", command=lambda: [effacer(), info_espagnol()])

    menu_depense_espagnol = Menu(menu_espagnol)
    menu_espagnol.add_cascade(label="Cuenta", menu=menu_depense_espagnol)
    menu_depense_espagnol.add_command(label="cuenta", command=lambda: [effacer(), compte_espagnol()])
    menu_depense_espagnol.add_command(label="gasto", command=lambda: [effacer(), depense_espagnol()])

    menu_deco_espagnol = Menu(menu_espagnol)
    menu_espagnol.add_cascade(label="Configuraciones", menu=menu_deco_espagnol)
    menu_deco_espagnol.add_command(label="configuraciones", command=lambda: [effacer(), parametre_espagnol()])
    menu_deco_espagnol.add_command(label="desconexión", command=lambda: [effacer(), delete_espagnol(), page_compte()])


# ------------------------------------------------------------------------------------------------------------------------
# page principalee
global windows
windows = Tk()
# personnalier la fenêtre
windows.title("Bank Terminale scientifique")
windows.geometry("1080x720")
windows.minsize(1080, 720)
windows.iconbitmap("")
windows.config(bg='#41B77F')

# creer frame principale
frame = Frame(windows, bg='#41B77F')
frame2 = Frame(windows, bg='#41B77F')

# ajout slogan prémiére page
label_slogan = Label(frame, text="La banque de tous les lycéens sauf les Littéraires",
                     font=("Damion", 20), bg='#41B77F')
label_slogan.pack()

# création images
width = 100
height = 100
image = PhotoImage(file='data-science.png').zoom(5).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='#41B77F', bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image)
canvas.pack()

# crétion du demandeur de compte(nom utilisateur )
label_title3 = Label(frame, text="Nom utilisateur", font=("Comic sans MS", 20),
                     bg='#41B77F', bd=0, highlightthickness=0)
label_title3.pack()

# creation de la zone de texte pour le nom
var_utilisateur = StringVar()
nom_entry1 = Entry(frame, font=("Comic sans MS", 20), textvariable=var_utilisateur,
                   bg='#41B77F', fg='black')
nom_entry1.pack()

# creation de la zone de texte pour le nom
var_mot_de_passe = StringVar()
label_title4 = Label(frame, text="mot de passe", font=("Comic sans MS", 20), bg='#41B77F',
                     bd=0, highlightthickness=0, textvariable=var_mot_de_passe)
label_title4.pack()

# creation de la zone de texte pour le mot de passe
nom_entry2 = Entry(frame, font=("Comic sans MS", 20), show='*', bg='#41B77F', fg='black')
nom_entry2.pack()

# création bouton connexion
button = Button(frame, text="connexion", font=("Comic sans MS", 20), bg='#007FFF',
                fg='#40E0D0', activeforeground='#40E0D0', activebackground='#007FFF', bd='1',
                command=lambda: [effacer(), connecte()])
button.pack(pady=5)

# création bouton création compte
button1 = Button(frame, text="se créer un compte", font=("Comic sans MS", 20),
                 bg='#007FFF', fg='#40E0D0', activeforeground='#40E0D0', activebackground='#007FFF',
                 command=lambda: [effacer(), creation_compte()])
button1.pack(pady=5)

# création bouton decoration
button_decoration = Button(frame, text="se créer un compte", font=("Comic sans MS", 20),
                           bg='#007FFF', fg='#40E0D0', activeforeground='#40E0D0', activebackground='#007FFF', bd=500, )
button_decoration.pack(pady=5)

# Ajout frame principale
frame.pack()
frame2.pack()

# afficher
windows.mainloop()
