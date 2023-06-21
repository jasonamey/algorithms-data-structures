def bubbleSort(array):
    for i in reversed(range(len(array))):
   
      for j in range(0, i):
         if(array[j] > max): 
            max = array[j]
            swap(i, j, array)
           
def swap(i, j, array):
   temp = array[i]
   array[i] = array[j]
   array[j] = temp 

a = [1,3,2,5,4,2,1,5]

bubbleSort(a)

print(a)