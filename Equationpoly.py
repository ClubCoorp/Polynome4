# -*- coding : UTF-8 -*-

#New Jesspro
#
#*****************************************************

import tkinter as tk
from math import *
from EquationDégré1 import *
from Équationpoly3 import *

#Class
class Acceuilpoly :
    #Application pour la résolution d'équations De dégré maximum 4
    
    def __init__(self):
        " " " Initiateur /Lanceur de la fenêtre de base " " "
        self.root = tk.Tk()
        self.root.title("Résolution d'équations de degré 4")
        self.root.config(relief = tk.RAISED)
        
        self.makewidgets()
        self.menubar()
        self.root.mainloop()
        
    def menubar(self):
        " " " Configuration du menu" " "
        menu1 = tk.Menu(self.root)
        menu1.add_command(label = "Acceuil")
        
        menu1.add_command(label = f"degrée 1", command = self.makewidgets)
        menu1.add_command(label = f"degrée 2", command = Resoldegree2)
        menu1.add_command(label = f"degrée 3", command = Resoldegree3)
        menu1.add_command(label = f"degrée 4", command = self.makewidgets)
        menu1.add_separator()
        self.root.config(menu= menu1)
        
    def    makewidgets(self):
        " " " Configuration et positionnement des widgets " " "
       
        self.label = tk.Label(self.root, text = f"""Salut!!!!\n Nous voulons vous aider àrésoudre  tout vospolynôme
de dégée Inférieur à 4.\n Sélectionez le dégrée du polynome ici dessous:
""", bd= 15)
        self.label.pack()
        
         #Frame "selection du dégrée" avec un bouton de validation
        frame = tk.Frame( self.root, relief=tk.GROOVE, bd=5)
        frame.pack()
        
        self.scroll = tk.Scrollbar(frame)
        self.listchoix = tk.Listbox(frame,height=6 )
        self.listchoix.pack()
        
        #Remplissage de la listbox
        for i in range(4):
            self.listchoix.insert(1, f"dégrée {i}")
        
        #Frame bouton pour valider
        frameB = tk.Frame(self.root, relief= tk.GROOVE, bd = 3)
        frameB.pack()
        
        b = tk.Button(frameB, text = "Valider")
        b.pack(side=tk.LEFT, pady=2)
        
    def Valider(self):
        pass
        
        
#------------------------------------------------------------------------------------------------------------------------
#Autotext
if __name__ == "__main__":
    app = Acceuilpoly()
