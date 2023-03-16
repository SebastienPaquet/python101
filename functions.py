def hello():
    name = input("Svp, Entrez votre nom: ")
    print("Bonjour {name}.") 

hello()

def add(x, y=8):    #default parameters go at the end of the function definition (ELSE ERROR)
    print(x+y)

add(10)
add(3,4)
add(x=3,y=10)
add(6,y=10)         #positional arguments go first if using both style in function call (positional and named arguments) (ELSE ERROR)

add = lambda x, y: x + y
print(add(5,7))

print((lambda x, y: x + y)(5, 7))

def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
doubled = [x * 2 for x in sequence]             #simplest using list comprehension
doubled = [double(x) for x in sequence]         #using list comprehension with a function to perform more complex operations

doubled_map = map(double, sequence)             #using map #like in other languages without list comprehension
#print(list(map(function,iterables)))           #to print, print() it has a list

#doubled = [(lambda x:x*2)(x) for x in sequence]    #ugly
doubled_map = map(lambda x:x*2, sequence)
