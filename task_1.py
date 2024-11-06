def average(a):
   s = 0
   for i in range(len(a)):
         s += a[i] 
   return s / len(a)
                       
a = [1,2,3,4,5]
print(average(a))