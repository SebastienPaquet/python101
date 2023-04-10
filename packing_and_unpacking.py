##tuples
x = (5, 11)
y = 5, 11

#list
z = [5, 11]

#list with a tuple inside
a = ([5, 11])

#  parentheses are optional.. 
#..parentheses are needed when you want to explictly tell Python to treat some values as one tuple

##Destructuring collection
#(tuple) into his components
x, y = 2, 4 #short hand
t = 5, 11
x, y = t    #destructuring into his components
print("x:",x,",","y:",y)


#Destructuring collection
#(dict) in for loops --

student_grade = {"Rolf": 96, "Bob": 80, "Anne": 100}

for t in student_grade.items():
    print(t)

for student, grade in student_grade.items():
    print(f"étudiant:{student}, résultat:{grade}")


# -- Ignoring values with underscore --

person = ("Bob", 42, "Mechanic")
name, _, profession = person

print(name, profession)  # Bob Mechanic


## -- Collecting unstructured values into variable--

head, *tail = [1, 2, 3, 4, 5]
print(head)  # 1
print(tail)  # [2, 3, 4, 5] 


*head, tail = [1, 2, 3, 4, 5]
print(head)  # [1, 2, 3, 4]
print(tail)  # 5

head, *middle, tail = [1, 2, 3, 4, 5]
print(head)    # 1
print(middle)  # [2, 3, 4]
print(tail)    # 5

first, second, third, *rest = [1, 2, 3, 4, 5]

##destructuring collection into his components
head = [1, 2, 3, 4]
print(*head)  # 1 2 3 4


##packing and unpacking function arguments

# The asterisk takes all the arguments and packs them into a tuple.
def multiply(*args): #collect the arguments in a tuple
    print(args)
    total = 1
    for arg in args:
        total *= arg
    return total

print(multiply(1,3,5))

# The asterisk can be used to unpack sequences into arguments too!
def add(x, y):
    return x + y

nums = [3, 5]
print(add(*nums))  # instead of add(nums[0], nums[1])

#unpacking function keyword arguments
# Double asterisk packs or unpacks keyword arguments

def add(x, y):
    return x + y

nums = {"x": 15, "y": 25}

print(add(**nums))



# So this is a special bit of syntax in Python
# and what it means is collect all the positional arguments into this tuple args
# and also have a named argument at the end.
# This creates a required named argument.

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


#print(apply(1, 3, 5, "+"))  # Error
print(apply(1, 3, 6, 7, operator="+"))
print(apply(1, 3, 6, 7, operator="*"))


def named(**kwargs):    #**kwargs, used in function definition to collect/pack named arguments into a dictionary
    print(kwargs)

named(name = "Seb", age = 37)

details = {"name":"John Wayne", "age":30}
named(**details)       #**kwargs, used in function call to unpack a dictionary into named arguments

# -- Both args and kwargs --
def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Bob", age=25)
# This is normally used to accept an unlimited number of arguments and keyword arguments, such that some of them can be passed onto other functions.

"""
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
"""