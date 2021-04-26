#%%
palindrome = lambda word: word == "".join(reversed(word))
palindrome('kenny')
#%%
# Área del triangulo
base = int(input('Base del triángulo: '))
high = int(input('Altura del triángulo: '))
surf = lambda b, a: (b*a)/2
surf(base, high)
# %%
import numpy as np
import random
import math
from functools import reduce

#%%
arr = [random.random()*100 for _ in range(1,51)]
arr_sort = arr.sort()
arr = list(map( lambda x: math.ceil(x), arr))

# %%
arr
# %%
arr_minus = list(filter( lambda x : x % 3 != 0, arr))
arr_minus
# %%
arr_sum = reduce( lambda a,b: a+b, arr_minus)
arr_sum
# %%
