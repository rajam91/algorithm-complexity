def add_them_all(array: [int]) -> int: # fonction qui additionne tout les éléments dans un tableau
    if not array: #si la liste est vide
        return 0
    else :
        return array[0] + add_them_all(array[1:]) 
    
print(add_them_all) #affiche la fonction 



    
    