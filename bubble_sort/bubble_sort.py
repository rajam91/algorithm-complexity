def bubble_sort(arr):
    n = len(arr) #len determine la longueur du tableau
    for i in range (n): #le premier for va parcourir la liste
        for j in range (0, n-i-1): #le second `for` compare les éléments de la liste
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]=arr[j+1],arr[j]
    return arr

