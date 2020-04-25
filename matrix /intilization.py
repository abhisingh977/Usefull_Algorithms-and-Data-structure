
print("Intilize 2d array and print it")
classroom=[]
for i in range(5):
    row=[]
    for j in range(4):
        row.append(j)
    classroom.append(row)
    

print(classroom)

# print( "Manupulating value of 2d array ")

# for i in range(2):
#     for j in range(4):
#         classroom[i][j]=1
# print(classroom)
 
        
print("Transposing matrix")




newclass=[] 
for i in range(len(classroom[0])):
    row=[]
    for j in range(len(classroom)):
        row.append(0)
    newclass.append(row)

print(newclass)

  
for i in range(len(classroom)):
    for j in range(len(classroom[0])):
        newclass[j][i]=classroom[i][j]

print(newclass)





# classroom=[]
# out=[[j for j in range(4)]for i in range(5)]
# print(out)