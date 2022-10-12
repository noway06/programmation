from distutils.command import check
from http.client import SWITCHING_PROTOCOLS
from re import X
from sys import setswitchinterval
from tkinter import N



    

#print("entrer un nombre ")
#n= int(input())
#while n > 3  or n < 1 :
#    print("la reponse ne convienne pas , entrer un nv nombre")
 #   n =int( input())

#print("le nombre est bon")



# print("entrer un nombre ")
# n= int(input())
# while n < 10  or n > 20 :
#     if n < 10 :
#         n =int( input("la reponse ne convienne pas , entrer un nombre plus grand  "))
#     else :
#         n = int(input("entrer un nombre plus petit "))
    

# print ("nombre ok bravo ")
# n = int()
# pos = int()
# max = int(0)
    
# for i in range (1,21) :
#     print("donner le nombre numero " , i)
#     n = int(input( ))
#     if n > max : 
#         max = n
#         pos = i 
# print("le nombre le plus grand est :", max,"sa position est ", pos)

# x = int(1)
# print("donner un nombre")
# nbr = int(input())
# if nbr == 0 : print("la factorielle est nul")
# else : 
#     for i in range(2,nbr+1) :
#         x = x * i
    

# print ("la facorielle est egal ", x) 

# def categAge(age):
#     match age :
#         case 1|2|3|4|5|6|7: print("poussin")
#         case 7|8|9: print("pupille")
#         case 10|11 : print("minime")
#     if (age) > 11 : print("cade")
#     else : print("donner un age correct")

# categAge(45) 

# def impot(age , sexe) :
#     if (sexe == 'H') :
#         if(age >= 20 ) :
#              print("homme plus 20 ans imposable ")
#         else : print("homme moin de 20 ansn'est pas imposable")

#     elif (sexe == 'F') :
#         if(age > 18)  and (age < 35 ) : 
#             print("femme entre 18 35 est imposable")
#         else : print("femme moin 18 ou plus 35 non imposable")

# impot(45, 'F')


def is_prime(n) :
 
    if n < 2 :
 
        return False
 
    i = 2
 
    while i < n and n%i != 0 :
 
        i += 1
     
    return i == n


def sommePremier(n):
    somme = int()
    for i in range(2,n+1):
        if(is_prime(i)): somme = somme + i 
    print("la somme des nombre premier ",somme)

    

sommePremier(11)




