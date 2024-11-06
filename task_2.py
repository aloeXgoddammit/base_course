import numpy as np

def prod(a):
   s = 1
   for i in range(len(a)):
         s *= a[i] 
   return s
                       
a = [1,2,3,4,5]
print(prod(a))