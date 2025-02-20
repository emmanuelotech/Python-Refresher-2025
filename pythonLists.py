countries = ["United Kingdom","Uganda","Ghana","Nigeria","Australia"]
print(type(countries))
print(countries)

for each_country in countries:
    print(each_country)

#Accessing a particular index value in the list.
print("Am from ", countries[0])


#List indexing.
print(countries[3]) #Printing Nigeria

#List splicing.
print(countries[1:4]) #Returning values from 1 to 4-1.

#Obtaining list of countries from the first to the end.
#Printing all values from the start.
print("#################################")
print(countries[1:])

#Obtaining list type
print("Type of List:", type(countries))

#Replacing the value in the first index with the country 
# #Germany thus the new value at index 0 will be Germany not USA
countries[0]="Germany";
print(countries)

countries[4]="Cameroon";
print(countries)
print(countries[-1:])

#Obtaining the lenght which is the total number of items.
print(len(countries))