# Bubble Sort

Le langage utilisé pour la méthode bubble Sort est python.

La fonction `bubble sort` est un algorithme de tri, simple et efficace, qui nous permettra de trier une liste ou un tableau.

###### Méthode de tri : 
Cette fonction va comparer le premier éléments du tableau avec le deuxième si celui ci est petit alors il échange les deux éléments, et va faire de même avec tous les éléments du tableau.

Pour résumer elle compare les éléments adjacents et de les échanger si nécessaire.

##### Voici comment tester la méthode bubble sort :

```python
array: [int] = [8, 4, 12, 6, 2]
result: [int] = bubble_sort(array)
print(f"Given array: {array}")
print(f"Result: {result}")
```

La compléxité de cette algorithme est O(n^2), où n est la taille de l'algorithme à trier

La première boucle effectue n itérations, la deuxième boucle fait n-i-1, car le plus grand éléments est déjà à sa place , on a donc moins de boucle à faire.

En multipliant le nombre d'itération de la première boucle par celle de la deuxième boucle on a n x (n-1)/2
Ce qui nous donnes n^2/2

Dans l'analyse de compléxité, on ignore les termes constants car ils n'ont aucun impact sur le comportement asymptotique de notre algorithme.