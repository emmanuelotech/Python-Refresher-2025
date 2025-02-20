#2D is like having multiple lists inside a list variable



my_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# print(my_list);
# print(my_list[2][2]); #Result 9 -> 2 D list Rows and columns.

#Nested Loops--> is where you have a loop inside a loop. specifically for loop in for loop

for lists in my_list:
    for column in lists:
        sqr_value = column*column;
        print(column," sqred", sqr_value)
        
   
