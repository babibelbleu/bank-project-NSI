# Importations des bibliothèques
from tkinter import *

# Créer une interface
windows = Tk()

# Personnalier la fenêtre
windows.title("Nom de l'application")
windows.geometry("1080x720")
windows.minsize(1080,720)
windows.iconbitmap("bank.ico")
windows.config(background='#41B77F')

<<<<<<< HEAD
#crer frame principale
frame = Frame(windows , bg ='#41B77F')

#ajout de composant
label_title = Label(windows,text = "Nom de l'application", font =("Courrier", 40), bg = '#41B77F')
=======
# Créer frame principale
frame = Frame(windows, bg='#E10BB1')

# Ajout de composant
label_title = Label(windows, text="Nom de l'application", font=("Courrier", 40), bg='#E10BB1')
>>>>>>> 7f4241a3b7bf629a274d13db6448fedb9b69dc49
label_title.pack()
#crétion du demandeur de compte(nom utilisateur )
label_title1 = Label(frame, text = "Nom utilisateur", font = ("Comic sans MS", 20), bg = '#41B77F', bd = 0, highlightthickness = 0)
label_title1.pack()

<<<<<<< HEAD
# creation de la zone de texte pour le nom
nom_entry1 = Entry(frame, font = ("Comic sans MS", 20), bg = '#41B77F', fg = 'black')
nom_entry1.pack()

# création du demandeur de mot de passe
label_title2 = Label(frame, text = "mot de passe", font = ("Comic sans MS", 20), bg = '#41B77F', bd = 0, highlightthickness = 0)
label_title2.pack()

# creation de la zone de texte pour le mot de passe
nom_entry2 = Entry(frame, font = ("Comic sans MS", 20),show='*' ,bg = '#41B77F', fg = 'black')
nom_entry2.pack()

#création bouton connexion
button = Button(frame, text = "connexion", font = ("Comic sans MS", 20), bg = 'white', fg = '#41B77F', activeforeground= '#41B77F')
button.pack(pady = 5)

##création bouton connexion
button1 = Button(frame, text = "se créer un compte", font = ("Comic sans MS", 20), bg = 'white', fg = '#41B77F', activeforeground= '#41B77F')
button1.pack(pady= 5)

#Ajout frame principale
frame.pack(expand = YES)
=======
# Création de la zone de texte pour le nom
nom_entry1 = Entry(frame, font=("Comic sans MS", 20), bg='#E10BB1', fg='black')
nom_entry1.grid(row=100, column=0, sticky=W)

# Création de la zone de texte pour le mot de passe
nom_entry2 = Entry(frame, font=("Comic sans MS", 20), show='*', bg='#E10BB1', fg='black')
nom_entry2.grid(row=300, column=0, sticky=W)

# Création du demandeur de compte(nom utilisateur)
label_title1 = Label(frame, text="Nom utilisateur", font=("Comic sans MS", 20), bg='#E10BB1')
label_title1.grid(row=0, column=0, sticky=W)

# Création du demandeur de mot de passe
label_title2 = Label(frame, text="mot de passe", font=("Comic sans MS", 20), bg='#E10BB1')
label_title2.grid(row=200, column=0 , sticky=W)

# Création bouton connexion
button = Button(frame, text="connexion", font=("Comic sans MS", 20), bg='#0B2FE1')
button.grid(row=400, column=0, sticky=N)

# Création bouton connexion
button1 = Button(frame, text="se créer un compte", font=("Comic sans MS", 20), bg='#0B2FE1')
button1.grid(row=500, column=0, sticky=N)

# Ajout frame principale
frame.pack(expand=YES)
>>>>>>> 7f4241a3b7bf629a274d13db6448fedb9b69dc49

# Afficher la fenêtre
windows.mainloop()