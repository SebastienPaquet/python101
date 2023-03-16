empty_list = []
empty_tuple = ()
one_item_tuple = (1,)
empty_set = set()
empty_dict = {}

list1 = ["Peter","Joe","Cleveland"]
tuple1 = ("Peter","Joe","Cleveland") #immutable list
set1 = {"Peter","Joe","Cleveland","Peter"}   #unordered, no-duplicated_values-allowed
print(list1[0])     #subscript notation (to access elements of a list or tuple)

print("1er de la liste : " + list1[0])
print("1er du tuple : " + tuple1[0])

print(list1)
print(tuple1)
print(set1)

list1[2]="Kevin"
print(list1)

list1.append("Clyde")
print(list1)

list1.append(12)
print(list1)

list1.remove("Joe")
print(list1)

set1.add("Peter")
set1.add("Jim")
print(set1)