# Projet de NSI e terminale 2021 Quentin Kimppienne, Bodin Bastien
# Projet : création d'une fausse application bancaire ave une monnai fictive

from tkinter import *
from tkinter import ttk
from tkinter import Entry, Frame
import time


# functions pour supprimer tout les widget d'un page
def effacer():
    for widget in frame.winfo_children():
        widget.destroy()


# fonction pour supprimer le menu
def delete():
    mon_menu.delete("Information personnelle")
    mon_menu.delete("Compte")
    mon_menu.delete("Paramêtre")


# fonction pour definir la colonne pour choisir le moi de sa date de naissance
def selected_mois():
    Label(frame, text=combobox_mois.get()).pack()


# fonction pour definir la colonne pour choisir l'annee de sa date de naissance
def selected_annee():
    Label(frame, text=combobox_annee.get()).pack()


# fonction pour definir la colonne pour choisir le jour de sa date de naissance
def selected_jour():
    Label(frame, text=combobox_annee.get()).pack()


# fonction pour créer page principales
def page_compte():
    # creer frame principale
    frame1 = Frame(frame, bg='#41B77F')

    # ajout slogan prémiére page
    label_slogancompte = Label(frame1, text="La banque de tous les lycéens sauf les Littéraires",
                               font=("Damion", 20), bg='#41B77F')
    label_slogancompte.pack()

    # création images
    width2 = 100
    height2 = 100
    image2 = PhotoImage(file="data-science.png").zoom(5).subsample(32)
    canvas2 = Canvas(frame1, width=width2, height=height2, bg='#41B77F', bd=0, highlightthickness=0)
    canvas2.create_image(width / 2, height / 2, image=image2)
    canvas2.pack()

    # crétion du demandeur de compte(nom utilisateur )
    label_titlecompte = Label(frame1, text="Nom utilisateur", font=("Comic sans MS", 20),
                              bg='#41B77F', bd=0, highlightthickness=0)
    label_titlecompte.pack()

    # creation de la zone de texte pour le nom
    nom_entrycompte = Entry(frame1, font=("Comic sans MS", 20), bg='#41B77F', fg='black')
    nom_entrycompte.pack()

    # creation de la zone de texte pour le nom
    label_titlecompte = Label(frame1, text="mot de passe", font=("Comic sans MS", 20), bg='#41B77F',
                              bd=0, highlightthickness=0)
    label_titlecompte.pack()

    # creation de la zone de texte pour le mot de passe
    nom_entrycompte2 = Entry(frame1, font=("Comic sans MS", 20), show='*', bg='#41B77F', fg='black')
    nom_entrycompte2.pack()

    # création bouton connexion
    button_co = Button(frame1, text="connexion", font=("Comic sans MS", 20), bg='#007FFF',
                       fg='#40E0D0', activeforeground='#40E0D0', activebackground='#007FFF', bd='1',
                       command=lambda: [effacer(), page_connecte(), connecte()])
    button_co.pack(pady=5)

    # création bouton création compte
    button_compte = Button(frame1, text="se créer un compte", font=("Comic sans MS", 20),
                           bg='#007FFF', fg='#40E0D0', activeforeground='#40E0D0', activebackground='#007FFF',
                           bd='1', command=lambda: [effacer(), creation_compte()])
    button_compte.pack(pady=5)

    # création bouton decoration
    button_deco1 = Button(frame1, text="se créer un compte", font=("Comic sans MS", 20),
                          bg='#007FFF', fg='#40E0D0', activeforeground='#40E0D0', activebackground='#007FFF',
                          bd=500)
    button_deco1.pack(pady=5)

    # Ajout frame principale
    frame1.pack(expand=YES)

    # afficher
    windows.mainloop()


# fonction pour créer la page ou l'on peut créer son compte
def creation_compte():
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
    image1 = PhotoImage(file="data-science.png").zoom(5).subsample(32)
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
    check_homme = Radiobutton(frame_crea, text='Femme', value='1',
                              bg='#41B77F')
    check_homme.pack()
    check_femme = Radiobutton(frame_crea, text='Homme', value='0',
                              bg='#41B77F')
    check_femme.pack()

    # nom/prénom/mot de passe
    label_nomcrea = Label(frame_crea, text="Nom", font=("Comic sans MS", 15), bg='#41B77F')
    label_nomcrea.pack()

    nom_entry_creation = Entry(frame_crea, font=("Comic sans MS", 15), bg='#41B77F', fg='black')
    nom_entry_creation.pack()

    label_prenomcrea = Label(frame_crea, text="prenom", font=("Comic sans MS", 15), bg='#41B77F')
    label_prenomcrea.pack()

    prenom_entry_creation = Entry(frame_crea, font=("Comic sans MS", 15), bg='#41B77F', fg='black')
    prenom_entry_creation.pack()

    label_mot_de_passe = Label(frame_crea, text="mot de passe", font=("Comic sans MS", 15), bg='#41B77F')
    label_mot_de_passe.pack()

    mot_de_passe_entry_creation = Entry(frame_crea, font=("Comic sans MS", 15), bg='#41B77F', fg='black', show='*')
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
    annee = ["1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982",
             "1983",
             "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996",
             "1997",
             "19998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010",
             "2011",
             "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", ]
    combobox_annee = ttk.Combobox(frame_crea2, value=annee)
    combobox_annee.current(0)
    combobox_annee.bind("<<CombobocSelected>>", selected_annee)
    combobox_annee.grid(row=1, column=0)

    mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre",
            "Decembre"]

    combobox_mois = ttk.Combobox(frame_crea2, value=mois)
    combobox_mois.current(0)
    combobox_mois.bind("<<ComboboxSelected>>", selected_mois)
    combobox_mois.grid(row=1, column=1)

    jour = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
            "20", "21",
            "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

    combobox_jour = ttk.Combobox(frame_crea2, value=jour)
    combobox_jour.current(0)
    combobox_jour.bind("<<ComboboxSelected>>", selected_jour)
    combobox_jour.grid(row=1, column=2)

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
                          activebackground='#007FFF', bd='1', command=lambda: [effacer(), page_connecte(), connecte()])
    button_suite.pack(side=LEFT)

    frame_crea.pack(expand=YES)
    frame_crea2.pack()
    bottomframe.pack(pady=9)

    windows.mainloop()


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
    label = Label(frame, text="Cette page servira a choisir la langue (francais, anglais, espagnol) ",
                  font=("Damion", 20), bg='#41B77F')
    label.pack()


# fonction du menu sur la prémiére page du compte lots de la connexion
def page_connecte():
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


# fontion qui crée la frame de la premiere page du compte lors de la connexion
def connecte():
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



    #création d'une animation
    can = Canvas(frame, height = 100, width = 1080,  bg='#41B77F', bd= 0 )
    ball = can.create_oval(10, 10, 100, 100, fill='yellow')
    can.pack(pady = 150)

    flag = 0
    while True:
        if flag == 0:
            for i in range(0,100):
                time.sleep(0.06)
                can.move(ball, 10, 0)
                can.update()
                flag = 1
        else:
            for i in range(0,100):
                time.sleep(0.05)
                can.move(ball, -10,0)
                can.update()
            flag = 0


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
nom_entry1 = Entry(frame, font=("Comic sans MS", 20), bg='#41B77F', fg='black')
nom_entry1.pack()

# creation de la zone de texte pour le nom
label_title4 = Label(frame, text="mot de passe", font=("Comic sans MS", 20), bg='#41B77F',
                     bd=0, highlightthickness=0)
label_title4.pack()

# creation de la zone de texte pour le mot de passe
nom_entry2 = Entry(frame, font=("Comic sans MS", 20), show='*', bg='#41B77F', fg='black')
nom_entry2.pack()

# création bouton connexion
button = Button(frame, text="connexion", font=("Comic sans MS", 20), bg='#007FFF',

                fg='#40E0D0', activeforeground='#40E0D0', activebackground='#007FFF', bd='1',
                command=lambda: [effacer(), page_connecte(), connecte()])
button.pack(pady=5)

# création bouton création compte
button1 = Button(frame, text="se créer un compte", font=("Comic sans MS", 20),
                 bg='#007FFF', fg='#40E0D0', activeforeground='#40E0D0', activebackground='#007FFF',
                 bd='1', command=lambda: [effacer(), creation_compte()])
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
