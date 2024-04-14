prime=0
a = int(input("Enter a number: "))
for i in range(2, a):
    if a % i == 0:
        prime = 1
if prime == 1 or a == 1 :
    
    print("Not a Prime")
else:
    print("Entered number",a," is Prime Number.")
