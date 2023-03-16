import my_module
from my_module import divide as divide_from
from os import path

print("current file print()s: ")
print("(dunder file) __file__ :",__file__)
print(path.abspath(__file__))
print("(dunder name) __name__ :",__name__)

print("imported module function call: ")
my_module.print_file_n_name()

print(my_module.divide(10,2))
print(divide_from(200,20))