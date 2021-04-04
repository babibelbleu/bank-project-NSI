from tkinter import *

#création des commandes de bouton connexion
from tkinter import Tk


def page_compte():
    creation.destroy()
    global windows2
    windows2 = Tk()
    windows2.title("Bank Terminale scientifique")
    windows2.geometry("1080x720")
    windows2.minsize(1080,720)
    windows2.iconbitmap("")
    windows2.config(bg='#41B77F')

    # creer frame principale
    frame2 = Frame(windows2, bg='#41B77F')

    # ajout slogan premiére page
    label_slogan1 = Label(windows2, text="La banque de tous les lycéens sauf les Littéraires",
                          font=("Damion", 20),bg='#41B77F')
    label_slogan1.pack()

    # création images
    width2 = 100
    height2 = 100
    image2 = PhotoImage(file="data-science2.png").zoom(5).subsample(32)
    canvas2 = Canvas(windows2, width=width2, height=height2, bg='#41B77F', bd=0, highlightthickness=0)
    canvas2.create_image(width / 2, height / 2, image=image2)
    canvas2.pack()

    # crétion du demandeur de compte(nom utilisateur )
    label_title_comp = Label(frame2, text="Nom utilisateur", font=("Comic sans MS", 20), bg='#41B77F', bd=0,
                         highlightthickness=0)
    label_title_comp.pack()

    # creation de la zone de texte pour le nom
    nom_entry_txt = Entry(frame2, font=("Comic sans MS", 20), bg='#41B77F', fg='black')
    nom_entry_txt.pack()

    # creation de la zone de texte pour le nom
    label_title_txt= Label(frame2, text="mot de passe", font=("Comic sans MS", 20), bg='#41B77F', bd=0,
                         highlightthickness=0)
    label_title_txt.pack()

    # creation de la zone de texte pour le mot de passe
    nom_entry_txt = Entry(frame2, font=("Comic sans MS", 20), show='*', bg='#41B77F', fg='black')
    nom_entry_txt.pack()

    # création bouton connexion
    button_co = Button(frame2, text="connexion", font=("Comic sans MS", 20), bg='#007FFF', fg='#40E0D0',
                    activeforeground='#40E0D0', activebackground='#007FFF', bd='1', command=page_compte)
    button_co.pack(pady=5)

    # création bouton création compte
    button2 = Button(frame2, text="se créer un compte", font=("Comic sans MS", 20), bg='#007FFF', fg='#40E0D0',
                     activeforeground='#40E0D0', activebackground='#007FFF', bd='1', command=creation_compte)
    button2.pack(pady=5)

    # création bouton decoration
    button_deco2 = Button(frame2, text="se créer un compte", font=("Comic sans MS", 20),
                    bg='#007FFF', fg='#40E0D0',activeforeground='#40E0D0', activebackground='#007FFF', bd=500)
    button_deco2.pack(pady=5)

    # Ajout frame principale
    frame2.pack(expand=YES)


#créatio des commandes du bouton cration compte
def creation_compte():
    windows.destroy() # on détruit la page d'avant
    global creation
    creation = Tk()   #on en créer une nouvelle

    creation.title("Bank Terminale scientifique")
    creation.geometry("1080x720")
    creation.minsize(1080,720)
    creation.iconbitmap("")
    creation.config(background='#41B77F')
    
    # création de la frame principale
    frame1 = Frame(creation, bg = '#41B77F')
    sous_frame1_gauche = Frame(frame1, bg = '#41B77F')
    sous_frame1_droite = Frame(frame1, bg='#41B77F')
    

    # ajout slogan prémiére page
    label_slogan2 = Label(creation, text="La banque de tous les lycéens sauf les Littéraires",
                    font=("Damion", 20),bg='#41B77F')
    label_slogan2.pack()

    # création images
    width1= 100
    height1 = 100
    image1 = PhotoImage(file="data-science.png").zoom(5).subsample(32)
    canvas1 = Canvas(creation, width=width1, height=height1, bg='#41B77F', bd=0, highlightthickness=0)
    canvas1.create_image(width/2,height/2, image=image1)
    canvas1.pack()

    #création du titre
    label_titl = Label(creation, text ='Création du compte', bg ='#41B77F',
                font = ("Damion",25))
    label_titl.pack()
                        
    #texte 
    texte = Label(creation, text="Sexe", bg ='#41B77F',font = ("Damion",15))
    texte.pack()
    #choix du sexe
    check_homme = Radiobutton(creation,text = 'Femme', value = '1',
                bg = '#41B77F')
    check_homme.pack()
    check_femme = Radiobutton(creation,text = 'Homme', value = '0',
                    bg = '#41B77F')
    check_femme.pack()

    #nom/prénom/mot de passe
    label_nom = Label(creation, text = "Nom",font = ("Comic sans MS", 15), bg ='#41B77F')
    label_nom.pack()

    nom_entry_creation = Entry(creation, font=("Comic sans MS", 15), bg='#41B77F', fg='black')
    nom_entry_creation.pack()

    label_prenom = Label(creation, text="prenom", font=("Comic sans MS", 15), bg='#41B77F')
    label_prenom.pack()

    prenom_entry_creation = Entry(creation, font=("Comic sans MS", 15), bg='#41B77F', fg='black')
    prenom_entry_creation.pack()

    label_mot_de_passe = Label(creation, text="mot de passe", font=("Comic sans MS", 15), bg='#41B77F')
    label_mot_de_passe.pack()

    mot_de_passe_entry_creation = Entry(creation, font=("Comic sans MS", 15), bg='#41B77F', fg='black',show='*')
    mot_de_passe_entry_creation.pack()



    #date de naissance
    texte_annee = Label(frame1, text="Année", bg='#41B77F', font=("Damion", 15))
    texte_annee.grid(row = 0, column = 0)

    texte_mois = Label(frame1, text="Mois", bg='#41B77F', font=("Damion", 15))
    texte_mois.grid(row = 0, column = 1)

    texte_jour = Label(frame1, text="Jour", bg='#41B77F', font=("Damion", 15))
    texte_jour.grid(row=0, column=2)

    # objet pour choisir date de naissance
    label = Label(creation, text = "Date de naissance",
                 font = ("Comic sans MS", 20), bg ='#41B77F')
    label.pack()
    
    #crétion du truc pour demander la date de naissance
    annee = Listbox(frame1, font = ("Comic sans MS", 15),height=3, width = 4)
    for values in range(1970,2021):
        annee.insert(END,values)
    annee.grid(row= 1, column = 0)

    mois = Listbox(frame1, font=("Comic sans MS", 15), height=3, width=3)
    for values in range(12):
        mois.insert(END, values + 1)
    mois.grid(row=1, column=1)

    jour = Listbox(frame1, font=("Comic sans MS", 15), height=3, width=3)
    for values in range(31):
        jour.insert(END, values + 1)
    jour.grid(row=1, column=2)

    # création du bouton de retour en arriéres
    button_retour = Button(sous_frame1_droite, text="retour",
                           font=("Comic sans MS", 10),
                           bg='#007FFF', fg='#40E0D0', activeforeground='#40E0D0',
                           activebackground='#007FFF', bd='1', command=page_compte)
    button_retour.pack()

    # création du bouton création du comte
    button_retour = Button(sous_frame1_gauche, text="créer un compte",
                           font=("Comic sans MS", 10),
                           bg='#007FFF', fg='#40E0D0', activeforeground='#40E0D0',
                           activebackground='#007FFF', bd='1')
    button_retour.pack()

    frame1.pack()
    sous_frame1_gauche.grid(row=3, column = 0)
    sous_frame1_droite.grid(row=3, column = 2)

#------------------------------------------------------------------------------------------------------------------------
#page principale

#creer une interface
global windows
windows = Tk()

#personnalier la fenêtre
windows.title("Bank Terminale scientifique")
windows.geometry("1080x720")
windows.minsize(1080,720)
windows.iconbitmap("")
windows.config(background='#41B77F')
               
#crer frame principale
frame = Frame(windows , bg ='#41B77F')

#ajout slogan prémiére page
label_slogan = Label(windows, text = "La banque de tous les lycéens sauf les Littéraires",
                     font = ("Damion", 20), bg = '#41B77F')
label_slogan.pack()

#création images
width = 100
height = 100
image = PhotoImage(file = "data-science.png").zoom(5).subsample(32)
canvas = Canvas(windows, width = width, height = height, bg= '#41B77F',bd = 0,highlightthickness = 0)
canvas.create_image(width/2, height/2, image = image)
canvas.pack()

#crétion du demandeur de compte(nom utilisateur )
label_title1 = Label(frame, text = "Nom utilisateur", font = ("Comic sans MS", 20),
                     bg = '#41B77F', bd = 0, highlightthickness = 0)
label_title1.pack()

# creation de la zone de texte pour le nom
nom_entry1 = Entry(frame, font = ("Comic sans MS", 20), bg = '#41B77F', fg = 'black')
nom_entry1.pack()

# creation de la zone de texte pour le nom
label_title2 = Label(frame, text = "mot de passe", font = ("Comic sans MS", 20), bg = '#41B77F',
                     bd = 0, highlightthickness = 0)
label_title2.pack()

# creation de la zone de texte pour le mot de passe
nom_entry2 = Entry(frame, font = ("Comic sans MS", 20),show='*' ,bg = '#41B77F', fg = 'black')
nom_entry2.pack()

#création bouton connexion
button = Button(frame, text = "connexion", font = ("Comic sans MS", 20), bg = '#007FFF',
                fg = '#40E0D0', activeforeground= '#40E0D0',activebackground='#007FFF', bd = '1',
                command = page_compte)
button.pack(pady = 5)

#création bouton création compte
button1 = Button(frame, text = "se créer un compte", font = ("Comic sans MS", 20),
                 bg = '#007FFF', fg = '#40E0D0', activeforeground= '#40E0D0',activebackground='#007FFF',
                 bd = '1', command = creation_compte)
button1.pack(pady= 5)

#création bouton decoration
button_deco = Button(frame, text = "se créer un compte", font = ("Comic sans MS", 20),
                  bg = '#007FFF', fg = '#40E0D0', activeforeground= '#40E0D0',activebackground='#007FFF',bd = 500)
button_deco.pack(pady= 5)

#Ajout frame principale
frame.pack(expand = YES)

#afficher
windows.mainloop()