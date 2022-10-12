from re import X
from tkinter import N

#print("entrer votre nom svp")
#name = input()
#print("ok bye ", name,"!")

#prixtotal = float()
#print("donner le prix HT du produit ")
#prix = float(input())
#print("le nombre d'article")
#nombreDarticle = int(input())
#print("quelle est le taux tva")
#tva = (float(input()))2.
#prixtotal = nombreDarticle * ( prix + ((prix / 100 ) * tva))  
#print("le prix total est ",prixtotal)

#print("donner un entier")
#number = int(input())
#if number%3 == 0  : print( number , "est divisible par 3 ")
#else : print (number , "n est pas divisible par 3")
print("entrer un nombre : ")
nombre = float(input())
if nombre == 0 : print("nombre nul")
elif  nombre > 0 : print("nombre positif ")
else : print("nombre negatif")





prix = float()
print("ecrire entrer le nombre de photocopie")
nombrePhotocopie = int(input())
if (nombrePhotocopie < 10) and (nombrePhotocopie >0): 
     prix = nombrePhotocopie * 0.5 
     print("le prix est ",prix)
elif (nombrePhotocopie > 10 ) and ( (nombrePhotocopie < 20)  or (nombrePhotocopie == 20 )) :
                prix = 0.4 * nombrePhotocopie 
                print("le prix est ",prix)
elif (nombrePhotocopie > 20 ) : 
     prix = 0.3 * nombrePhotocopie 
     print("le prix est ",prix)
        
else : print("entrer un nombre positif")






print("entrer un nombre")
n = int(input())
i = 0
print("les 10 nombre suivant sont ")
for i in range(10) :
    i = i + 1 
    print( n + i)





puiss = float()
x = float()
n = int()
puiss = 1
print("entrer un nombre x")
x=int(input())
print("entrer un nombre n")
n = int(input())
puiss = 1
for i in range(n) :
    puiss = puiss * x
print ( "la valeur de n puissance x est", puiss)









som = int(0)
print("entrer un nombre")
nbr = int(input())
for i in range(1,nbr + 1):
    som = som + i    
    print(  i, " + ")

print("somme ", som)