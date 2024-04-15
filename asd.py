a=int(input("Write the first number:",))
b=int(input("Write the second number:",))
c=int(input("Write a number for a function: 1 for addition, 2 for subtraction, 3 for remainder with division, 4 for division, 5 floor division, 6 for multiplication."))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
    print(b-a)
elif c==3:
    print(a%b)
elif a==4:
    print(a/b)
elif c==5:
    print(a//b)
elif c==6:
    print(a*b)
else:
    print("Invalid")

print("salary")
a=int(input("Basic salary per month"))
print(a+((20/100)*a))
    
print("leap year identifier")
a=int(input("Enter the present year"))
if a%4==0:
    print("leap year,")
else:
    print("not leap year")

print("voter")
a=int(input("Enter age"))
if a>17:
    print("valid voter")
else:
    print("invalid")
