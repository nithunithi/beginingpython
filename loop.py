#loops
#for 
name="karthic"
for letters in name :
    print(letters)

#checking the word contains or not 

for my in "h-a-p-p-y":
    if my=='a':
        print("a is present")
    else :
        print("a is not present")   

# break it stop the progress when its finds the word 

for my in "h-a-p-p-y":
    if my=='a':
        print("a is present")
        break
    else :
        print("a is not present")   

#continue _it go back to the starting loop
for my in "h-a-p-p-y":
    if my=='a':
        print("a is present")
        continue
    else :
        print("a is not present") 

#while loop 
number = 1
while number < 7:
    print(number) 
    number +=1    #incrementing the value
else :
    print("over")  
    





