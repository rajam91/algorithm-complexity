# Search in array

Le langage utilisé pour faire l'algorithme est Python.

Une fonction a été définit, `search_in_array`.
 La fonction 'search_in_array' est une fonction qui prends deux paramètres un tableau et un nombre. Le nombre correspond au nombre recherché.
La fonction parcours la liste pour rechercher un nombre. Si le nombre est dans la liste il faut qu'il renvoie l'index du nombre, si ce n'est pas le cas , la fonction retourne -1.


##### Voici comment tester la fonction :

```python
array: [int] = [4, 7, 1, 2, 9]
number: int = 1
result: int = search_in_array(array, number)
print(f"Given array: {array}")
print(f"Index of {number}: {result}")
```

La compléxité de l'algorithme est linéaire.