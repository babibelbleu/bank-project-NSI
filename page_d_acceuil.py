from tkinter import *


# creer une interface
windows = Tk()

# personnalier la fenêtre
windows.title("Bank Terminale scientifique")
windows.geometry("1080x720")
windows.minsize(1080,720)
windows.iconbitmap("bank.ico")
windows.config(background='#41B77F')

# créer frame principale
frame = Frame(windows, bg='#41B77F')


# création des commandes de bouton connexion
def page_compte():

    page_compte = Toplevel(windows)
    page_compte.title("Bank Terminale scientifique")
    page_compte.geometry("1080x720")
    Label(page_compte, text='fiu').pack()


label = Label(windows,
              text="B.T.S",
              font=("Courrier", 40),
              bg='#41B77F')
label.pack()


# créaton page si code ou nom utilisation
def page_compte_erreur():

    page_compte = Toplevel(windows)
    page_compte.title("erreur")
    page_compte.geometry("200x200")
    page_commpte.minsize(200,200)
    Label (page_compte,
           text='fiu').pack()


# création des commandes du bouton cration compte
def creation_compte():

    page_compte = Toplevel(windows)
    page_compte.title("Bank Terminale scientifique")
    page_compte.geometry("1080x720")
    page_commpte.minsize(180,720)
    Label(page_compte,
          text='fiu').pack()


# ajout slogan
label_slogan = Label(windows,
                     text="La banque de tous les lycéens sauf les Littéraires",
                     font=("Damion", 20),
                     bg='#41B77F')
label_slogan.pack()

# création images
width = 100
height = 100
image = PhotoImage(file="data-science.png").zoom(5).subsample(32)
print(image)
canvas = Canvas(windows,
                width=width,
                height=height,
                bg='#41B77F',
                bd=0,
                highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.pack()

# crétion du demandeur de compte(nom utilisateur )
label_title1 = Label(frame,
                     text="Nom utilisateur",
                     font=("Comic sans MS", 20),
                     bg='#41B77F',
                     bd=0,
                     highlightthickness=0)
label_title1.pack()

# creation de la zone de texte pour le nom
nom_entry1 = Entry(frame,
                   font=("Comic sans MS", 20),
                   bg='#41B77F',
                   fg='black')
nom_entry1.pack()

# création du demandeur de mot de passe
label_title2 = Label(frame,
                     text="mot de passe",
                     font=("Comic sans MS", 20),
                     bg='#41B77F',
                     bd=0,
                     highlightthickness=0)
label_title2.pack()

# creation de la zone de texte pour le mot de passe
nom_entry2 = Entry(frame,
                   font=("Comic sans MS", 20),
                   show='*',
                   bg='#41B77F',
                   fg='black')
nom_entry2.pack()

# création bouton connexion
button = Button(frame,
                text="connexion",
                font=("Comic sans MS", 20),
                bg='#007FFF',
                fg='#40E0D0',
                activeforeground='#40E0D0',
                activebackground='#007FFF',
                bd='1',
                command=page_compte)
button.pack(pady=5)

# création bouton création compte
button1 = Button(frame,
                 text="se créer un compte",
                 font=("Comic sans MS", 20),
                 bg='#007FFF',
                 fg='#40E0D0',
                 activeforeground='#40E0D0',
                 activebackground='#007FFF',
                 bd='1',
                 command=creation_compte)
button1.pack(pady=5)

# création bouton decoration
button1 = Button(frame,
                 text="se créer un compte",
                 font=("Comic sans MS", 20),
                 bg='#007FFF',
                 fg='#40E0D0',
                 activeforeground='#40E0D0',
                 activebackground='#007FFF',
                 bd=500)
button1.pack(pady=5)

# Ajout frame principale
frame.pack(expand=YES)

# afficher
windows.mainloop()
