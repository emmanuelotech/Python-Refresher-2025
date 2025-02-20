#spreadsheet
#Document
#txt files et.c
#We want to know how to read that file

coun_file = open('countries.txt',"r") #Second parameter it takes shows what we want to do
#r = read, w=edit or write to it, a =append to the file.r+ means we want to do both reading and writing#fullcap
#Save it to a variable let me say cou_file.
# print(coun_file.readable()); #We want to check if the file is readable. returns 'boo' True
# print(coun_file.readline()) ; #Print the first line of the file.
# print(coun_file.readline());#prints first file and second one.
# print(coun_file.readline())

#print(coun_file.readlines()) ->#.readlines() puts them into  a list
for each_line in coun_file:
    print(each_line);


# for each in coun_file.readlines():
#     print(each);

coun_file.close() #Everytime we open the file we have to close it. In between we can do what
#ever we want with the file.

