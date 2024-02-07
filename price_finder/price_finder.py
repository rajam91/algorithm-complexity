import math

price_min = 1
price_max = 500

def price_finder(price: int) -> int:
    if price < price_min or price > price_max:
        return -1
    arr: [int] = list(range(price_min, price_max+1)) 
    found = -1
    while found != price:  # remplacer par found == price 
        size: int = len(arr)
        index: int = math.floor(size/2) # remplacer par size // 2 
        found = arr[index]
        if found < price:
            arr = arr[index:]
        else:
            arr = arr[:index]
    return found