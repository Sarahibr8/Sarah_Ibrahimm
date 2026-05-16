import math , random

Number = -5
print(f"Print The Absolute Value Of ({Number}): {abs(Number)}") 

Number = 2.503
print(f"Round The Number ({Number}) is: {round(Number)}")

Number = 5
print(f"The Power Of ({Number}): {pow(Number, 2)}")

print(f"The Minimum Value In (3,5,-1,10,2) is: {min(3,5,-1,10,2)}") #the lower

print(f"The Maximum Value In (3,5,-1,10,2) is: {max(3,5,-1,10,2)}")

print(f"The Sum Value In (3,5,-1,10,2) is: {sum([3,5,-1,10,2])}") # the all number + togther 

print(f"The Mod Value Of (17,5) is: {divmod(17,5)}")

Number = 3.9
print(f"Convert ({Number}) to int: {int(Number)}")

Number = 3
print(f"Convert ({Number}) to float: {float(Number)}")

print(f"The Binary Value Of ({Number}) is: {bin(Number)}")

print(f"The Octal Value Of ({Number}) is: {oct(Number)}")

print(f"The Hex Value Of ({Number}) is: {hex(Number)}")

Number = 16
print(f"The Square Root Of ({Number}) is: {math.sqrt(Number)}")

Number = 3.6
print(f"The Rounded Down Value Of ({Number}) is: {math.floor(Number)}")

Number = 3.1
print(f"The Rounded Up Value Of ({Number}) is: {math.ceil(Number)}")

Number = 3.7
print(f"The Truncate Value Of ({Number}) is: {math.trunc(Number)}")

Number = 5
print(f"The factorial  Of ({Number}) is: {math.factorial(Number)}")

print(f"This is a random integer {random.randint(1,100)}")
print(f"This is a random float {random.uniform(1.0 ,10.0)}")

Number1, Number2 = 5, 8 
print(f"{Number1} , {Number2}")
Number1, Number2 = Number2, Number1
print(f"{Number1} , {Number2}")