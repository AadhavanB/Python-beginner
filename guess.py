import random
i=0
ii=0
print("-------------------------")
print("Computer generation output")
print("You may enter the game.")
print("--------------------------")
a=str(input("Set your game password:",))
no=int(input("Enter the number of chances you want:",))
while i<=no:
    b=str(input("Enter your game password:",))
    if a==b:
        print("You may enter the game.")
    else:
        print("wrong password!")
        reset=int(input("type 1 if you want to rewrite password"))
        if reset==1:
            continue
        else:
            break
    while i<=no:
        num=int(input("Write a random number between 0 and 5:",))
        cnum=random.randint(0, 5)
        if num==cnum:
            ii+=1
            print("you win the game!")
            print("you have",ii,"points")
            break
        elif num>5 or num<0:
            print("This number is invalid. Try again you have",no-i,"chances left")
        else:
            print("You are wrong! The number was",cnum)
            i+=1
            if i==no-1:
                print("You have 1 chance left")
            else:
                print("You have",no-i,"chances left")
        if i==no:
            print("You have no chances left")
            print("you have",ii,"point(s)")
            break
    if num==cnum:
        restart=int(input("Enter 1 if you want to resume:"))
        if restart==1:
            i=0
            continue
        else:
            break
    if i==no:
        restart=int(input("Enter 1 if you want to restart:"))
        if restart==1:
            i=0
            continue
        else:
            break
print("A game by XXɅ) 2∅24")
