#CODE10
def selectionSort(n):
   for replace in range(len(n)-1,0,-1):
       maxpos=0
       for location in range(1,replace+1):
           if n[location]>n[maxpos]:
               maxpos = location

       temp = n[replace]
       n[replace] = n[maxpos]
       n[maxpos] = temp

n = [14,46,43,27,57,41,45,21,70]
selectionSort(n)
print(n)
