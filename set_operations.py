#differences part1 - 
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local1 = friends.difference(abroad)
local2 = friends - abroad
#print("local friends: ")
print(local1)
print(local2)

ens_vide = abroad.difference(friends)
#print("ensemble vide: ")
print(ens_vide)

#union |
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

students1 = art.union(science)  # students = art | science
students2 = art | science
print(students1)
print(students2)

#intersection &
students_in_both1 = art.intersection(science)
students_in_both2 = art & science 
print(students_in_both1)
print(students_in_both2)

#differences part2 (A-B | B-A) = not(A & B)

s1 = {1, 3, 4, 5, 7, 8}
s2 = {2, 3, 4, 6, 8, 9}

s3 = s1.symmetric_difference(s2)
s4 = s1.difference(s2) | s2.difference(s1)      

print(s3)  # {1, 2, 5, 6, 7, 9}
print(s4)  # {1, 2, 5, 6, 7, 9}