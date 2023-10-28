#list -[] ,can't change the value in list  
fruits =["apple","orange","grapes"]
print(fruits[0])


#length
fruits =["apple","orange","grapes"]
print("list:",fruits)
print("no of fruits:",len (fruits))

#rappend ,#insert- adding new value 
fruits=["apple","orange","grapes"]
fruits.append("banana") 
print("append:",fruits)

#removing &changing 
fruits=["apple","orange","grapes"]
fruits[2]="banana"
print(fruits)

#remove
fruits=["apple","orange","grapes","banana"]
fruits.remove('banana')
print(fruits)

#multiply the items
fruits=["apple","orange","grapes","banana" ]
fruits =[fruits*2 for n in range (8)]
print(fruits)

