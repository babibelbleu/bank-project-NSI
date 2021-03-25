import tkinter as tk

class Acceuil(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.creer_widgets()
        
    def creer_widgets(self):
       
        #création frame
        self.frame = tk.Frame(self , bg ='#41B77F')
        self.frame.pack()
        
        self.label = tk.Label(self.frame,
                 text = "B.T.S",font = ("Damion", 30),
                 bg = '#41B77F')        
        self.label.pack()
       
        #ajout slogan prémiére page
        self.label = tk.Label(self.frame,
                 text = "La banque de tous les lycéens sauf les Littéraires",
                 font = ("Damion", 20),
                 bg = '#41B77F')        
        self.label.pack()
        
        #création images
        width = 100
        height = 100
        self.image = tk.PhotoImage(file = "data-science.png").zoom(5).subsample(32)
        self.canvas = tk.Canvas(self.frame, width = width, height = height, 
                 bg= '#41B77F',bd = 0,highlightthickness = 0)
        self.canvas.create_image(width/2, height/2, image = self.image)
        self.canvas.pack()
        
        #crétion du demandeur de compte(nom utilisateur )
        self.label_title1 = tk.Label(self.frame, text = "Nom utilisateur",
                 font = ("Comic sans MS", 20), 
                 bg = '#41B77F', bd = 0, highlightthickness = 0)
        self.label_title1.pack()
       
        # creation de la zone de texte pour le nom
        self.nom_entry1 = tk.Entry(self.frame, font = ("Comic sans MS", 20),
                bg = '#41B77F', fg = 'black')
        self.nom_entry1.pack()
        
        # creation de la zone de texte pour le nom
        self.label_title2 = tk.Label(self, text = "mot de passe",
                font = ("Comic sans MS", 20),
                bg = '#41B77F', bd = 0, highlightthickness = 0)
        self.label_title2.pack()
        
        # creation de la zone de texte pour le mot de passe
        self.nom_entry2 = tk.Entry(self, font = ("Comic sans MS", 20),show='*',
                bg = '#41B77F', fg = 'black')
        self.nom_entry2.pack()
        
        #création bouton connexion
        self.button = tk.Button(self, text = "connexion",
                font = ("Comic sans MS", 20), bg = '#007FFF', fg = '#40E0D0',
                activeforeground= '#40E0D0',activebackground='#007FFF', bd = '1')
        self.button.pack(pady = 5)
        
        #création bouton création compte
        self.button1 = tk.Button(self, text = "se créer un compte",
                font = ("Comic sans MS", 20), bg = '#007FFF', fg = '#40E0D0',
                activeforeground= '#40E0D0',activebackground='#007FFF', bd = '1')
        self.button1.pack(pady= 5)

        #création bouton decoration
        self.button2 = tk.Button(self, text = "se créer un compte", 
                font = ("Comic sans MS", 20), bg = '#007FFF', fg = '#40E0D0',
                activeforeground= '#40E0D0',activebackground='#007FFF', bd = 500)
        self.button2.pack(pady= 5)
        
if __name__ == "__main__":
    windows = Acceuil()
    windows.title("Bank Terminale scientifique")
    windows.geometry("1080x720")
    windows.minsize(1080,720)
    windows.iconbitmap("")
    windows.config(background ='#41B77F')
    windows.mainloop()               
               
               
               
               