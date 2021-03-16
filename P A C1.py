#fontion factorielle
def fact (nbr):
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
for i in range (3,11):
    for j in range (3,6):
        if i>=j :
           print ((  i,j ) , "    P=",perm( i) , "        A=", arran (i,j) ,     "       C= ", combi (i,j))
