#fontion factorielle
def fact (nbr):
    if nbr == 0 or nbr==1:
        return 1
    res=1
    for i in range (2,nbr+1):
        res = res *i
    return res    
    
#fonction permutation
def perm (n):
    p= fact(n)
    return p
#fontion arrangement
def arran (n,p):
    a=fact(n)//fact(n-p)
    return a
#foction combinaison
def combi (n,p):
    c=fact(n)//(fact(n-p)*fact(p))
    return c
#debut du programme
for i in range (3,11):                                  #comptage du nombre d'objet
    print(" n =",i,",Permutation =",perm(i),end="")     #affichage de nombre avec le calcul de la permutation  
    for j in range (3,6):                               #comptage du nombre de tirage
        if i>=j :                                       # il faut que le nombre de tirage soit inferieur ou egale au nombre d'objet
           print (" ,pour p =",j,",Arrangement =",arran (i,j),", Combinaison =",combi (i,j)) #affichage de calcul d'arrangement et combinaison relatifs au nombre d'objet
    print("--------------------------------------------------------------------------------")
