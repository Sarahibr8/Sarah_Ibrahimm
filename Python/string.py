string="doublequotes"
string='singlequotes'
string="""
multiplelines
"""
string="""
multiplelines
"""
empty=""
empty=''

print(" I'm Sarah")
print('She said "Hello"')
print('I\'m Sarah')
print("She said \"Hello\"")



print("Here is the first line \n Here is the second line")
print("Back \\ Slash ")
print(r"C\Users\Sara")

name = "Sarah"
age = 15
print(f"{name=} , {age=}")
print("{:.2f}".format(3.1446588))

print("Hello" + "Python ")
print("Hello" , "Python ")
print("Ha" * 10)
print("_" * 10)
word = "Python"
print(word[0])
print(word[-1])
print(word[len(word) -1])
print(word[3.5])
print(word[::-1])
print("Py" in word)
print("Pyssd" not in word)