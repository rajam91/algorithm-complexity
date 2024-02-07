#Consigne:
#Create a simple function `search_in_array` that takes as parameter 
#an array of numbers and a number to find in the array. 
#Also it must return the index of found value or `-1` if not found. 

def search_in_array(array: [int], nb: int) -> int : 
    n = len(array) #len est la longueur de la liste
    for i in range (n):
        if array[i] == nb : #comparaison entre la valeur de la liste et la valeur rechercher
            return i
    else :
     return -1
    






    