#Add Two numbers program in Python....
#Division those two numbers also
#now i have to write this program in exception way
try:
    x=int(input("enter first num:"))
    y=int(input("enter second num:"))
    add=x+y
    div=x/y
except(ValueError):
    print("please give proper input")
else:
    print("addion of two numbers is",add)
    print("Division of two numbers is:",div)
