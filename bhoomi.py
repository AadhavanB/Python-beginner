fruitsnveg={"banana","apple","tomato"}
ip=str(input("Write a fruit."))
for x in fruitsnveg:
    print("This fruit is accesible for buying")
fruitsnveg.add(ip)
for x in fruitsnveg:
    print("This fruit is accesible for buying" + x)
