#Add Two numbers program in Python....
#now i have to write this program in exception way
try:
    x=int(input("enter first num:"))
    y=int(input("enter second num:"))
    res=x+y
    print("res:",res)
except(ValueError):
    print("please give proper input")