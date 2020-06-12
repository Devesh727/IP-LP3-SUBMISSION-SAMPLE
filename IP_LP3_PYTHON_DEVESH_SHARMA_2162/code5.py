#code5
def removeDuplicate(str, n): 
       
    index = 0                                  # Used as index in the modified string
      
    for i in range(0, n):                     # Traverse through all characters 
            
        for j in range(0, i + 1):               # Check if str[i] is present before it
            if (str[i] == str[j]): 
                break
                   
        if (j == i):                             # If not present, then add it to 
                                                 # result.
            str[index] = str[i] 
            index += 1
              
    return "".join(str[:index]) 
  
# Driver code 
str= input("Enter the string:")
n = len(str) 
print(removeDuplicate(list(str), n)) 
  
