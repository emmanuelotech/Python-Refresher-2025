#try except in python
#USES:
#Prevents an error from occuring or catches the error exception
#Errors most of the time just stops our program from operating
#It automatically gets an error and prints whatever we want to tell the user.


# try:  #Try running this code
#     user_input = int(input("Enter: "))

#     print(user_input);
# #Incase it does not run well do the following.
# except ValueError:
#     print("Value not an integer...")
#     print("Something went wrong..please try again" +name);

def try_except_else():
    try:
        x = int(input("Enter integer: "));
    except:
        print("Something went wrong...");
    else:
        print("Program ran successfully!")


#Will run whether there's a problem or not 
try:
    x = int(input("Enter integer: "));
except:
    print("Something went wrong...");
else:
    print("..else running")
finally:
    print("Am running whether ther's problem or not")