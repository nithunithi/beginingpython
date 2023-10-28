#SIMPLE  CALCULATOR 
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
print (""" select operation
1.add
2.sub
3.mul
4.div
""")

choice=int(input("enter your choice")) #we cant add string so we converting into integer
a=int(input("enter number 1"))
b=int(input("enter number 2"))
if choice  ==   1:
    print(add(a, b))
elif choice == 2:
    print(sub)(a, b)
elif choice == 3:
    print(mul(a, b))
elif choice == 4:
    print(div(a, b))     
else:
    print("enter correct choice")       

       



