# -*- coding: "utf8" -*-
#New JessPro
#EwuationDégré1.py
#*****************************************************

#import -----------------------------------------------
import tkinter as tk
from math import *

#definition de class
class Resoldegree2():
    " " " Resolution des polynomes de dégrée 2" " "
    
    def __init__(self):
        
       
        self.x1 = float()
        self.x2 = float()
        self.root = tk.Tk()
        self.Resultat = tk.StringVar()
        self.Solution = tk.StringVar()
        self.ValeurA = tk.StringVar()
        self.ValeurA.set(0.0)
        self.ValeurB= tk.StringVar()
        self.ValeurB.set(1.0)
        self.ValeurC = tk.StringVar()
        self.ValeurC.set(0.0)
        self.label = tk.Label(self.root, text=  f"""Salut!!!!\n Nous voulons vous aider àrésoudre  tout vos polynômes
de dégée Inférieur à 4.\n Entrez les differents coefficients de votre polynome dégrée 2 .\n ax² + bx + c=0 """)
        self.label.pack()
        self.afficheSolution
        self.affiche
        self.entreevariable()
        self.root.mainloop()
        
        
    def affiche(self):
    	" " " Affiche les paramettre entrée par l' ultilisateur  " " "
    	self.Resultat.set(f'{self.ValeurA.get()}x² + {self.ValeurB.get()} x + {self.ValeurC.get()} = 0')
    
    def afficheSolution(self):
    	" " "Affichage des solutions" " "
    	
    	self.a = complex(self.ValeurA.get())
    	self.b = complex(self.ValeurB.get())
    	self.c = complex(self.ValeurC.get())
    	a,b,c = self.a, self.b, self.c
    	if a==0:  ## notre équation devient bx+c=0
        	self.Solution.set(f' la  racine double est :\n x={-c/b}')
    	else:
        	delta=b**2 - 4*a*c ## discriminant de notre equation
        	self.x1= (-b+delta**(1/2))/(2*a)
        	self.x2= (-b - delta**(1/2))/(2*a)
        	self.Solution.set(f' les solutions sont :\n x1={self.x1} \n x2 = {self.x2}')
    
    def  entreevariable(self):
        " " " Definition des differents coeficiants du polynome" " "
        
       #Frame enregistrant le coeficient a et contenant un bouton pour valider
        frameA = tk.Frame(self.root, relief = tk.GROOVE, bd = 3)
        frameA.pack()
        
        ## Entrée ((Entry))
        frame1 = tk.Frame(frameA, relief = tk.GROOVE, bd = 3)
        frame1.pack()
        self.labelA = tk.Label(frame1, text = f"Entrez la valeur de a")
        self.labelA.pack()
        #Entrée du parametre a
        
        self.entree1 = tk.Entry(frame1, textvariable= self.ValeurA, width = 30)
        self.entree1.pack()
        ##Le bouton (Valider a)
        bouton1 = tk.Button(frame1, text = "Valider a", command = self.affiche)
        bouton1.pack(side=tk.LEFT, pady=4)
        
        
        #Frame enregistrant le coeficient b et contenant un bouton pour valider
        frameB= tk.Frame(self.root, relief = tk.GROOVE, bd = 3)
        frameB.pack()
        self.labelB = tk.Label(frameB, text = f"Entrez la valeur de b")
        self.labelB.pack()
        
        ##Frame de b
        frame2= tk.Frame(frameB, relief = tk.GROOVE, bd = 3)
        frame2.pack()
        ##Entrée du parametre b	
        self.entree2 = tk.Entry(frame2, textvariable= self.ValeurB, width = 30)
        self.entree2.pack()
        ##Le bouton (Valider b)
        bouton2 = tk.Button(frameB, text = "Valider b", command = self.affiche)
        bouton2.pack(side=tk.LEFT, pady=4)
        
        
        #Frame enregistrant le coeficient c et contenant un bouton pour valider
        ##frame de c
        frameC= tk.Frame(self.root, relief = tk.GROOVE, bd = 3)
        frameC.pack()
        self.labelC = tk.Label(frameC, text = f"Entrez la valeur de C")
        self.labelC.pack()
        ##Entrée du parametre c
        
        ###frame du champ d'entree de '
        frame3= tk.Frame(frameC, relief = tk.GROOVE, bd = 3)
        frame3.pack()
        ###Champ d'entrée'
        self.entree3 = tk.Entry( frame3, textvariable= self.ValeurC, width = 30)
        self.entree3.pack()
        ###Le bouton (Valider b)
        bouton3 = tk.Button(frame3, text = "Valider b", command = self.affiche)
        bouton3.pack(side=tk.LEFT, pady=4)
        
 
        #Le bouton (Solution)
        ##Frame 
        frame = tk.Frame(self.root, relief = tk.GROOVE, bd = 3)
        frame.pack()
        ##bouton
        bouton = tk.Button(frame, text = "Solution", command = self.afficheSolution)
        bouton.pack(side=tk.LEFT, pady=4)
        
        #Affichage du polynome
        label4 = tk.Label( self.root, text='Votre polynnome est :' )
        label4.pack()
        
        self.affiche()
        label5 = tk.Label(self.root, textvariable= self.Resultat,  fg = 'red', bg = 'white')
        label5.pack()
        
        #Affichage des solutions
        self.afficheSolution()
        label6 = tk.Label(self.root, textvariable= self.Solution, fg = 'red', bg = 'white')
        label6.pack()
        
    	
    	
    	
 
         
#------------------------------------------------------------------------------------------------------------------------
#Autotext
if __name__ == "__main__":
    app = Resoldegree2()            
            
       
    
