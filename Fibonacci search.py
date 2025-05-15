def fibonacci_search(arr, n, key):
   offset = -1
   Fm2 = 0
   Fm1 = 1
   Fm = Fm2 + Fm1
   while (Fm < n):
      Fm2 = Fm1
      Fm1 = Fm
      Fm = Fm2 + Fm1
   while (Fm > 1):
      i = min(offset + Fm2, n - 1)
      if (arr[i] < key):
         Fm = Fm1
         Fm1 = Fm2
         Fm2 = Fm - Fm1
         offset = i
      elif (arr[i] > key):
         Fm = Fm2
         Fm1 = Fm1 - Fm2
         Fm2 = Fm - Fm1
      else:
         return i
   if (Fm1 == 1 and arr[offset + 1] == key):
      return offset + 1
   return -1
arr = [132, 170, 190, 245, 294, 606, 735, 801]
print("Elemen array adalah sebagai berikut")
for j in range(len(arr)):
   print(arr[j], end = " ")
n = len(arr)
key = 294
print("\nElemen yang dicari : ", (key))
index = fibonacci_search(arr, n, key)
if(index >= 0):
   print("Elemen ditemukan pada index : ", (index))
else:
   print("Elemen tidak ditemukan")