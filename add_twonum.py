#Add Two numbers program in Python....
#Division those two numbers also
#now i have to write this program in exception way
try:
    x=int(input("enter first num:"))
    y=int(input("enter second num:"))
    add=x+y
    if y==0:
        print("ZeroDivisionError")
    div=x/y
except(ValueError):
    print("please give proper input")
except(ZeroDivisionError):
    print()
else:
    print("addion of two numbers is",add)
    print("Division of two numbers is:",div)
    