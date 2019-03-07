# -*- coding: "utf8" -*-
#New JessPro
#EwuationDégré3.py
#*****************************************************

#import -----------------------------------------------
import tkinter as tk
from math import *
from EquationDégré1 import Resoldegree2
import EquationDégré1 as deg1
#definition de class
class Resoldegree3(Resoldegree2):
    " " " Resolution des polynomes de dégrée 2" " "
    
    def __init__(self):
    	" " " initiateur " " "
    	self.listeSolution = [ 0,0,0]
    	
    	self.root= tk.Tk()
    	self.Resultat3= tk.StringVar()
    	self.Solution3 = tk.StringVar()
    	self.Valeur3A= tk.StringVar()
    	self.Valeur3A.set(0.0)
    	self.Valeur3B= tk.StringVar()
    	self.Valeur3B.set(1.0)
    	self.Valeur3C = tk.StringVar()
    	self.Valeur3C.set(0.0)
    	self.Valeur3D= tk.StringVar()
    	self.Valeur3D.set(0.0)
    	self.label = tk.Label(self.root, text=  f"""Salut!!!!\n Nous voulons vous aider àrésoudre  tout vos polynômes de dégée Inférieur à 4.\n Entrez les differents coefficients de votre polynome dégrée 2 .\n ax³ + bx²+ cx +d=0 """)
    	self.label.pack()
    	self.afficheSolution3
    	self.affiche3
    	self.entreevariable3()
    	self.root.mainloop()
    
    
    def affiche(self):
    	" " " Affiche les paramettre entrée par l' ultilisateur  " " "
    	self.Resultat.set(f'{self.ValeurA.get()}x³ + {self.ValeurB.get()} x² + {self.ValeurC.get()} x + {self.ValeurD.get()} = 0')
    	
    def listeSolution(self):
    	" " "Affichage des solutions" " "
    	
    	a = complex(self.Valeur3A.get())
    	b = complex(self.Valeur3B.get())
    	c = complex(self.Valeur3C.get())
    	d = complex(self.Valeur3D.get())
    	if a==0:
    	    ## notre équation devient bx²+cx+d=0
    	    ### Quoi de plus facile qu'un probleme déjà resolue
    		b, c, d = a, b,c
    		
    		deg1.VarleurA= a
    		self.VarleurB = b
    		self.ValeurC = c
    		return [Resoldegree2().x1, Resoldegree2().x2]
    	else:
        	
			##Equation de dégrée 3 de la forme ax³+ bx²+ cx + d=0, a<>0

			###Nous allons procéder par trois etapes
			###juste pour  créer autre foc=ntion donc peut avoir besion l' ultilisateur
    
			#********************** ETAPE 1*************************************************
			## Metons notre équation sous la forme X³+ pX + q=0
            
            #par changement de variable on remplace  x par X=x+b/(3*a)
            #alors equation se met sous la forme X² + pX + q=0 TELS QUE:
            p=-b**2
            l=3*a**2
            p=p/l
            p=p+c/a
            q= 2*(b**3)/(27*(a**3)) - c*b/(3*(a**3)) + d/a
            ##Et voila enfin notre polynome sous la forme cherché
            #************************* ETAPE 2**********************************************
            ##Déterminons une solution particulière 
            # Par suite on pose u et v rtels que X= u+v et uv=-p/3
            ## alors en remplacant X PAR u+v dans  X³ + pX + q=0 on obtient
            ## u³+ v³= -q
            # En resolvant donc ce systeme on obtient finnalemant
            self.ValeurA = 1
            self.VarleurB = q
            self.ValeurC = -p**3/27
            u =Resoldegree2().x1
            v  =Resoldegree2().x2
            u=u**(1/3)
            v=v**(1/3)
            ## comme sollution particulière de X**3 + pX + q=0
            z1  = u + v - b/(3*a)
            
			###Surtout ne pas perdre de vue le fait que z1 n'est que solution de (E): X³ + pX + q=0

			#************************* TROISIEME ETAPE *************************************
			##Il sagit ici de déterminer la solution particulière de notre equation d'origine
			##et de faire une division euclidienne
            ##en fin une solution particuliere
            #Et la division euclidiène pour obtenir un polynome de degrée 2
            a1=a
            b1= a*z1 + b
            c1=-d/z1
            ##dans se cas , ax³+ bx² + cx + d= (x-z1)(a1x² + b1x +c1)
            #La resolution de notre nouvelle 	équation se fait avec l'appel
            ## de la fonction Resoldegree2
            self.VarleurA= a1
            self.VarleurB = b1
            self.ValeurC = c1
            z2 = Resoldegree2().x1
            z3= Resoldegree2().x2
            return [ z1, z2, z3]
    		
    		
    		
    def affiche3(self):
        self.Resultat3.set( f'{self.Valeur3A.get()}x³+ {self.Valeur3B.get()} x² + {self.Valeur3C.get()} x + {self.Valeur3D.get()} = 0')
    	
    def afficheSolution3(self):
        
        if self.Valeur3A.get()== 0 :
            
            self.Solution3.set(f' les solutions sont :\n x1={self.listeSolution[0]} \n x2 = {self.listeSolution[1]}')
            
        else :
            self.Solution3.set(f' les solutions sont :\n x1={self.listeSolution[0]} \n x2 = {self.listeSolution[1]} \n x3 = {self.listeSolution[2]} ')
    
    def  entreevariable3(self):
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
        
        self.entree1 = tk.Entry(frame1, textvariable= self.Valeur3A, width = 30)
        self.entree1.pack()
        ##Le bouton (Valider a)
        bouton1 = tk.Button(frame1, text = "Valider a", command = self.affiche3)
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
        self.entree2 = tk.Entry(frame2, textvariable= self.Valeur3B, width = 30)
        self.entree2.pack()
        ##Le bouton (Valider b)
        bouton2 = tk.Button(frameB, text = "Valider b", command = self.affiche3)
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
        self.entree3 = tk.Entry( frame3, textvariable= self.Valeur3C, width = 30)
        self.entree3.pack()
        ###Le bouton (Valider c)
        bouton3 = tk.Button(frame3, text = "Valider c", command = self.affiche3)
        bouton3.pack(side=tk.LEFT, pady=4)
        
        #Frame enregistrant le coeficient d et contenant un bouton pour valider
        frameD = tk.Frame(self.root, relief = tk.GROOVE, bd = 3)
        frameA.pack()
        
        ## Entrée ((Entry))
        frame4 = tk.Frame(frameD, relief = tk.GROOVE, bd = 3)
        frame4.pack()
        self.labelD = tk.Label(frameD, text = f"Entrez la valeur de d")
        self.labelD.pack()
        #Entrée du parametre d
        
        self.entree4 = tk.Entry(frame4, textvariable= self.Valeur3A, width = 30)
        self.entree4.pack()
        ##Le bouton (Valider d)
        bouton4 = tk.Button(frame4, text = "Valider d", command = self.affiche3)
        bouton4.pack(side=tk.LEFT, pady=4)
        
        
 
        #Le bouton (Solution)
        ##Frame 
        frame = tk.Frame(self.root, relief = tk.GROOVE, bd = 3)
        frame.pack()
        ##bouton
        bouton = tk.Button(frame, text = "Solution", command = self.afficheSolution)
        bouton.pack(side=tk.LEFT, pady=4)
        
        #Affichage du polynome
        label5 = tk.Label( self.root, text='Votre polynnome est :' )
        label5.pack()
        
        self.affiche3()
        label6= tk.Label(self.root, textvariable= self.Resultat3,  fg = 'red', bg = 'white')
        label6.pack()
        
        #Affichage des solutions
        self.afficheSolution3()
        label7 = tk.Label(self.root, textvariable= self.Solution3, fg = 'red', bg = 'white')
        label7.pack()
        
    	
    	
    	
 
         
#------------------------------------------------------------------------------------------------------------------------
#Autotext
if __name__ == "__main__":
    app = Resoldegree3()            
            
       
    
