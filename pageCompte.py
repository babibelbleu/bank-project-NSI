import tkinter as tk

class Compte(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.creer_widgets()
   
    def creer_widgets(self):
        
        #création d la frame principale de la page
        self.frame = tk.Frame(self , bg ='#41B77F')
        self.frame.pack()
        
        #création du titre
        self.label_title = tk.Label(self.frame, text ='Création du compte',
                bg ='#41B77F',font = ("Damion",40))
        self.label_title.grid(row = 0, column =0)
                        
        #texte 
        self.texte = tk.Label(self.frame , text="Genre", bg ='#41B77F',
                font = ("Damion",20))
        self.texte.grid(row = 1, column = 0)
    
        #choix du sexe      
        check_homme = tk.Radiobutton(self.frame,text = 'Femme', value = '1',
                bg = '#41B77F')
        check_homme.grid(row = 2, column = 0)
        check_femme = tk.Radiobutton(self.frame,text = 'Homme', value = '0',
                bg = '#41B77F')
        check_femme.grid(row = 3, column = 0)
   
        #date de naissance
        self.label = tk.Label(self.frame, text = "Date de naissance", 
                font = ("Comic sans MS", 20), bg ='#41B77F')         
        self.label.grid(row = 4, column = 0)
    
        #crétion du truc pour demander la date de naissance
        self.label = tk.Label(self.frame, text = "jour", 
                font = ("Comic sans MS", 15), bg ='#41B77F')         
        self.label.grid(row = 5, column = 0)
        self.label = tk.Label(self.frame, text = "mois", 
                font = ("Comic sans MS", 15), bg ='#41B77F')         
        self.label.grid(row = 5, column = 1)
        self.label = tk.Label(self.frame, text = "année", 
                font = ("Comic sans MS", 15), bg ='#41B77F')         
        self.label.grid(row = 5, column = 2)

        #mois
        self.mois = tk.Listbox(self.frame, font = ("Comic sans MS", 15),
                height=3, width = 3)
        for values in range(12):
            self.mois.insert(values,values+1)
            self.mois.grid(row = 6, column = 1)
        #jour
        self.jour = tk.Listbox(self.frame, font = ("Comic sans MS", 15),
                height=3, width = 3)
        for values in range (31):
            self.jour.insert(values,values+1)
            self.jour.grid(row = 6, column = 0)
        #annee
        self.annee = tk.Listbox(self.frame ,font = ("Comic sans MS", 15),
                height=3, width = 5)
        for values in range(1950,2021):
            self.annee.insert(values,values+1)
            self.annee.grid(row = 6, column = 2)
            
        #zone de text nom
        
        
            
   
if __name__ == "__main__":
    creation = Compte()   #on en créer une nouvelle
    creation.title("Bank Terminale scientifique")
    creation.geometry("1080x720")
    creation.minsize(1080,720)
    creation.iconbitmap("")
    creation.config(background='#41B77F')
    creation.mainloop()
        
