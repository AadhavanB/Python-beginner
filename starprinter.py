a=int(input("Write the number of stars needed:",))
b=str(input("Write the type of symbol:",))
for i in range(1,(a+1)):
    print(b*((a-i)+1))
for j in range(1,a+1):
    print(b*j)
