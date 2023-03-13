
#integer
x=1
y=10
y+=x
print(y)

#float
price = 9.99
discount =0.2
result = price* (1-discount)

print(result)

#string
name="Sébastien"
name+=" est le codeur actuel"
print(name)
nom = "Carl"
print(f"Bonjour {nom}")

nom = "Lenny"
salutation = "Bonjour {}"
print(salutation.format(nom))

#print(name*3)

#name =input("Enter your name: ") #returns a string
#print(name)

age_string =input("Enter your age: ") 
age = int(age_string)
age_months = age*12
print(f"your age ({age}) is {age_months} months")