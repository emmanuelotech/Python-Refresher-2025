#For loop is used for iterating over a sequence, it can be anything either in a list et.c
#Very much used in python especially when we have large amounts of data.

myList = ["Ji","Ju",'jo']

for letter in "Hello":
    print(letter);

for x in myList:
    print(x) #x is just a variable. it is just a placeholder for the value being picked for loop

for values in myList:
    print(values);


#Dictionary project:
mydict = {
    "name": "John",
    "home": "Kampala",
    "age": 28,
    "Category": "Master",
    "Level": "Atomic",
    "Status": "Molecular"

            }

for values in mydict:
    if values == "age" or values == "Category":
        pass;
    print(mydict[values]);


#For loop loops through the values of a certain object.
#While loop keeps running a certain block of code as long as the condition still holds as tree



#LOOPING THROUGH A RANGE

for x in range(4):
    print(x); #prints from 0 -> value-1 0,1,2,3

print("################3")
for x in range(3,7):
    print(x);


#We can also use the else statement

for x in range(7):
    print(x);
else:
    print("Finished looping") #Finish a loop #iterating over a sequence then does something else
