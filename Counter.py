list=["a","b","s","a","c","b","w","q"]   #Create a list 
dict1=dict()                             #Create a empty dict
for i in range(len(list)):               #Itirate the list
    if list[i] not in dict1:              
        dict1[list[i]]=1                 #If the key does not exist and create it and give it a value 1.
    else:
        dict1[list[i]]+=1                #If the key already exist then increse the value of key by 1.
print(dict1)                             # Print the dict1


# Output = {'a': 2, 'b': 2, 's': 1, 'c': 1, 'w': 1, 'q': 1}