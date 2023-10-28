#tuples -(),can't change value,&can't add list and tuples
fruits=("apple","orange","grapes")
print(fruits.count('apple'))

#check item exists
fruits=("apple","orange","grapes")
print("banana"in fruits)
print("apple"in fruits)

#conditional statement 
age=17
if age >18:
    print("u can vote in election")
elif age ==18: 
    print("apply for vote ID")
else :
    print("you have to wait till 18")       

#and
a,b=66,24
if a==66  and b==24:
    print("correct")
else:
    print("incorrect")
if b==24:
    print("hello")
else:
    print("bye")    

#or
if a==1 and b==24:
    print("correct")
else:
    print("incorrect")
if b==224:
    print("hello")
else:
    print("bye")    
