#Combining the data from one list in to the other
countries = ["uganda","Jamaica"]
Fruits = ["Apples","Mangoes","Bananas"]

#Add one list to another
countries.extend(Fruits)
print(countries)

#make a copy of one list
cou_copy = countries.copy()
cou_copy.append("South Sudan")
countries.clear() #Clearing the elements in a list
print(cou_copy)
print(countries)
countries.append("South Africa");
print(countries)
print(cou_copy)
print(len(countries))
print(countries.index("South Africa")) #Finding out index of element
countries.append("True")
print(countries)
countries.pop(0) #Deletes value at specified index.
print(countries)

countries.clear() #Clear the list but it remains in program
print(countries)

countries.append("Emmauel")
countries.append("Okello")
print(countries)
del countries[0]
print(countries)

del countries
print(countries) #Del removes it completely from program