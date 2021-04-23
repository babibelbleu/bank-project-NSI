from tkinter import *
from tkinter import ttk

# functions pour supprimer tout les widget d'un page
from tkinter import Entry, Frame


def info():
    pass


def effacer():
    for widget in frame.winfo_children():
        widget.destroy()


def selected_mois():
    Label(frame, text=combobox_mois.get()).pack()


def selected_annee():
    Label(frame, text=combobox_annee.get()).pack()


def selected_jour():
    Label(frame, text=combobox_annee.get()).pack()


# def qui créer page principales
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
                       command=lambda: [effacer(), page_connecte()])
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


# création des commandes du bouton creation compte
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
                          activebackground='#007FFF', bd='1')
    button_suite.pack(side=LEFT)

    frame_crea.pack(expand=YES)
    frame_crea2.pack()
    bottomframe.pack(pady=9)

    windows.mainloop()


# création page quand on est connecté
def page_connecte():

    # création  menu
    mon_menu = Menu(windows)
    windows.config(menu=mon_menu, bg='#41B77F')
    file_menu = Menu(mon_menu)
    mon_menu.add_cascade(label="info perso", menu=file_menu)
    file_menu.add_command(label="Truc", command=info)

def connecté():

    label_connecté = Label(frame, text="La banque de tous les lycéens sauf les Littéraires",
                       font=("Damion", 20), bg='#41B77F')
    label_connecté.pack()

    width_root = 100
    height_root = 100
    image_root = PhotoImage(file="data-science.png").zoom(5).subsample(32)
    canvas_root = Canvas(frame, width=width_root, height=height_root, bg='#41B77F', bd=0, highlightthickness=0)
    canvas_root.create_image(width / 2, height / 2, image=image_root)
    canvas_root.pack()



    frame.pack()
    windows.mainloop()


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
image = PhotoImage(file="data-science.png").zoom(5).subsample(32)
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
                command=lambda: [effacer(), page_connecte(),connecté()])
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
