x= int(input("put value of first number:"))
y= int(input("put value of second number:"))
z= int(input("put value of third number:"))
# checking which one is greates and smallest
if(x>y and x>z):
    print(f"x is greatest")
elif(y>x and y>z):
    print("y is greatest")
else:
    print("z is greatest")

if(x<y and x<z):
    print(f"x is smallest")
elif(y<x and y<z):
    print("y is smallest")
else:
    print("z is smallest")
