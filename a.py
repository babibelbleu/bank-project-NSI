from tkinter import *

#création des commandes de bouton connexion
def page_compte():
    creation.destroy()
    page_compte = Tk()
    page_compte.title("Bank Terminale scientifique")
    page_compte.geometry("1080x720")
    page_compte.minsize(1080,720)
    page_compte.iconbitmap("")
    page_compte.config(bg='#41B77F')
    
    frame2 = Frame(page_compte,bg='#41B77F')                   
    label_1 = Label(frame2, text ='Page du compte', bg='#41B77F')
    label_1.pack()
    frame2.pack()


# créaton page si code ou nom utilisation est bon
def page_compte_erreur():
    page_erreur.title("erreur")
    page_erreur.geometry("200x200")
    page_erreur.minsize(200,200)
    page_erreur.iconbitmap("")
    page_erreur.config(background='#41B77F')
    Label (page_erreur, text ="le mot de passe ou l'identifiant sont incorrecte veuillez réssayer").pack()
    

#créatio des commandes du bouton cration compte
def creation_compte():
    windows.destroy() # on détruit la page d'avant
    creation = Tk()   #on en créer une nouvelle
    creation.title("Bank Terminale scientifique")
    creation.geometry("1080x720")
    creation.minsize(1080,720)
    creation.iconbitmap("")
    creation.config(background='#41B77F')
    
    # crétion de la frame principale 
    frame1 = Frame(creation, bg = '#41B77F')
    
    button_retour = Button(frame1, text = "retour",
                font = ("Comic sans MS", 5),
                bg = '#007FFF', fg = '#40E0D0', activeforeground= '#40E0D0',
                activebackground='#007FFF', bd = '1', command = page_compte)
    button_retour.grid(row = 0, column = 3)
    #création du titre
    label_titl = Label(frame1, text ='Création du compte', bg ='#41B77F',
                font = ("Damion",40))
    label_titl.grid(row = 1, column =0)
                        
    #texte 
    texte = Label(frame1 , text="Sexe", bg ='#41B77F',font = ("Damion",25))
    texte.grid(row = 0, column = 0)
    #choix du sexe      
    check_homme = Radiobutton(frame1,text = 'Femme', value = '1',
                bg = '#41B77F')
    check_homme.grid(row = 1, column = 0)
    check_femme = Radiobutton(frame1,text = 'Homme', value = '0',
                    bg = '#41B77F')
    check_femme.grid(row = 2, column = 0)
   
    #date de naissance
    label = Label(frame1, text = "Date de naissance",
                 font = ("Comic sans MS", 25), bg ='#41B77F')         
    label.grid(row = 3, column = 0)
    
    #crétion du truc pour demander la date de naissance
    annee = Listbox(frame1, font = ("Comic sans MS", 15),height=3, width = 3)
    for values in range(12):
        annee.insert(END,values+1)
    annee.grid(row = 4, column = 0)

    frame1.pack(expand = YES)


    




#------------------------------------------------------------------------------------------------------------------------
#page principale

#creer une interface
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
label_slogan = Label(windows, text = "La banque de tous les lycéens sauf les Littéraires",font = ("Damion", 20), bg = '#41B77F')
label_slogan.pack()

#création images
width = 100
height = 100
image = PhotoImage(file = "data-science.png").zoom(5).subsample(32)
canvas = Canvas(windows, width = width, height = height, bg= '#41B77F',bd = 0,highlightthickness = 0)
canvas.create_image(width/2, height/2, image = image)
canvas.pack()

#crétion du demandeur de compte(nom utilisateur )
label_title1 = Label(frame, text = "Nom utilisateur", font = ("Comic sans MS", 20), bg = '#41B77F', bd = 0, highlightthickness = 0)
label_title1.pack()

# creation de la zone de texte pour le nom
nom_entry1 = Entry(frame, font = ("Comic sans MS", 20), bg = '#41B77F', fg = 'black')
nom_entry1.pack()

# creation de la zone de texte pour le nom
label_title2 = Label(frame, text = "mot de passe", font = ("Comic sans MS", 20), bg = '#41B77F', bd = 0, highlightthickness = 0)
label_title2.pack()

# creation de la zone de texte pour le mot de passe
nom_entry2 = Entry(frame, font = ("Comic sans MS", 20),show='*' ,bg = '#41B77F', fg = 'black')
nom_entry2.pack()

#création bouton connexion
button = Button(frame, text = "connexion", font = ("Comic sans MS", 20), bg = '#007FFF', fg = '#40E0D0', activeforeground= '#40E0D0',activebackground='#007FFF', bd = '1', command = page_compte)
button.pack(pady = 5)

#création bouton création compte
button1 = Button(frame, text = "se créer un compte", font = ("Comic sans MS", 20), bg = '#007FFF', fg = '#40E0D0', activeforeground= '#40E0D0',activebackground='#007FFF', bd = '1', command = creation_compte)
button1.pack(pady= 5)

#création bouton decoration
button1 = Button(frame, text = "se créer un compte", font = ("Comic sans MS", 20), bg = '#007FFF', fg = '#40E0D0', activeforeground= '#40E0D0',activebackground='#007FFF', bd = 500)
button1.pack(pady= 5)

#Ajout frame principale
frame.pack(expand = YES)

#afficher
windows.mainloop()