def search_in_2d_array(arr: [[int]], nb: int) -> (int, int): 
    n=len(arr) 
    m=len(arr[0]) #m est la longueur de la liste
    for i in range(n): 
        for j in range(m): #le second for compare les éléments de la liste
            if arr[i][j] == nb: #comparaison entre la valeur de la liste et la valeur rechercher
                return(i,j)
    else:
      return(-1,-1)    


# cette fonction renvoie la valeur et la position de la valeur rechercher dans la liste 
# elle renvoie (-1,-1) si la valeur n'est pas dans la liste 
# elle renvoie (i,j) si la valeur est dans la liste où i est la ligne et j la colonne