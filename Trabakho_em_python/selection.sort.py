
array = [64, 25, 12, 22, 11, 1, 99, 34, 8, 45, 72, 3, 50, 18, 9]


for i in range(len(array)):
    
    
    min_idx = i
    
   
    for j in range(i + 1, len(array)):
        
        
        if array[min_idx] > array[j]:
            
           
            min_idx = j
            
  
    array[i], array[min_idx] = array[min_idx], array[i]


print("Array ordenado com Selection Sort:")
print(array)