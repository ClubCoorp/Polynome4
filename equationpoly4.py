### Resolution des équation de dégré inférieure à 4
import os 
#******************************************************
## 1/ Equation de dégré 2 de la forme ax^2 + bx + c=0

def poly2(a, b ,c):
    if a==0:  ## notre équation devient bx+c=0
        return [-c/b]
    else:
        delta=b**2 - 4*a*c ## discriminant de notre equation
        x1= (-b+delta**(1/2))/(2*a)
        x2= (-b - delta**(1/2))/(2*a)
        return [x1,x2]

#*****************************************************
##Equation de dégrée 3 de la forme ax^3 + bx^2 + cx + d=0

###Nous allons procéder par trois etapes
###juste pour  créer autre foc=ntion donc peut avoir besion l' ultilisateur
    
#********************** ETAPE 1*************************************************
## Metons notre équation sous la forme X**3 + pX + q=0
def proce1(a,b,c ,d):
    if a==0:  ### Quoi de plus facile qu'un probleme déjà resolue
        return poly2(b,c,d)
    else :
        #par changement de variable on remplace  x par X=x+b/(3*a)
        #alors equation se met sous la forme X**3 + pX + q=0 TELS QUE:

        p=-b**2
        l=3*a**2
        p=p/l
        p=p+c/a
        q= 2*(b**3)/(27*(a**3)) - c*b/(3*(a**3)) + d/a
        return [p,q]
##Et voila enfin notre polynome sous la forme cherché

#************************* ETAPE 2**********************************************
##Déterminons une solution particulière 
# -*- coding: utf-8 -*-

def proce2(p,q):
    # Par suite on pose u et v rtels que X= u+v et uv=-p/3
    ## alors en remplacant X PAR u+v dans  X**3 + pX + q=0 on obtient
    ## u**3 + v**3= -q
    # En resolvant donc ce systeme on obtient finnalemant
        
    [u,v] = poly2(1,q,-p**3/27)
    u=u**(1/3)
    v=v**(1/3)
    ## comme sollution particulière de X**3 + pX + q=0
    z1= u + v
    return z1
###Surtout ne pas perdre de vue le fait que z1 n'est que solution de E**3 + pX + q=0

#************************* TROISIEME ETAPE *************************************
##Il sagit ici de déterminer la solution particulière de notre equation d'origine
##et de faire une division euclidienne 
def poly3(a,b,c,d):
    [p,q]=proce1(a,b,c,d)##on determine tout dabort les couple (p,q) 
    z1=proce2(p,q) - b/(3*a)##en suite une solution particuliere
    #Et la division euclidiène pour obtenir un polynome de degrée deux
    a1=a
    b1= a*z1 + b
    c1=-d/z1
    ##dans se cas , ax^3 + bx^2 + cx + d= (x-z1)(a1x² + b1x +c1)
    #La resolution de notre nouvelle équation se fait avec l'appel
    ## de la fonction poly2
    poly2(a1,b1,c1).append(z1)
    return [poly2(a1,b1,c1)[0],poly2(a1,b1,c1)[1],z1]



#*********************************************************************************************
##Equation de la forme ax^4 + bx^3 + cx^2 + dx + e=0
def poly4(a,b,c,d,e):
    if a ==0:
        return poly3(b,c,d,e)