#Tuples are data types that are immutable.
#Once created can not be changed.

#Tuple declaration
three_numbers =(1,2,3,3333)
print(type(three_numbers))
print(three_numbers)
print(three_numbers[0]) #Index
#three_numbers[0] = 24;
#print(three_numbers) #Type Error.--> Does not support item assignment


print(three_numbers)

strings = ("Emmanuel","Chemistry","Biology")
print(strings)

boo = (True, False, True, True)
print(boo)

mixed = (1, "Seven", True, 24.33)
print(mixed)
print(type(mixed[0]))
print(mixed[2:])

#Using Tuple constructor.

numbers = tuple((1,2,3,4))
print(numbers)
