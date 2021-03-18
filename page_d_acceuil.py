from tkinter import *

#creer une interface
windows = Tk()

#personnalier la fenêtre
windows.title("Nom de l'application")
windows.geometry("1080x720")
windows.minsize(1080,720)
windows.iconbitmap("bank.ico")
windows.config(background='#41B77F')

#crer frame principale
frame = Frame(windows , bg ='#41B77F')

#ajout de composant
label_title = Label(windows,text = "Nom de l'application", font =("Courrier", 40), bg = '#41B77F')
label_title.pack()
#crétion du demandeur de compte(nom utilisateur )
label_title1 = Label(frame, text = "Nom utilisateur", font = ("Comic sans MS", 20), bg = '#41B77F', bd = 0, highlightthickness = 0)
label_title1.pack()

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
button = Button(frame, text = "connexion", font = ("Comic sans MS", 20), bg = '#007FFF', fg = '#40E0D0', activeforeground= '#40E0D0',activebackground='#007FFF', bd = '1')
button.pack(pady = 5)

##création bouton connexion
button1 = Button(frame, text = "se créer un compte", font = ("Comic sans MS", 20), bg = '#007FFF', fg = '#40E0D0', activeforeground= '#40E0D0',activebackground='#007FFF', bd = '1')
button1.pack(pady= 5)

#Ajout frame principale
frame.pack(expand = YES)

#afficher
windows.mainloop()