#Functions are bunch of code that perform particular task
#Is just a block of code that perform particular task.
#When you need to use it you just call it.
#Key word def.
#Python automatically indents in the function.
#Indention shows that the code in within that block.
#One indentation = four spaces.
#We can some parameter (Variable) to make it interesting

def greetings(name):
    print("Welcome "+ str(name))

#Call the function to use it
#Pass in a positional urgument
greetings("Emmanuel")
greetings(24)

#We can pass in more thatn one parameter

def greetings_2(name,age):
    print("Welcome" + name)
    print(f"You are {age} years old")

greetings_2("Emmanuel",28);

#passing in various values
def students(*names):
    print("Hello," + names[-1])

students("Emmanuel","24","James","Kevin");

greetings_2(name="James sneider",age = 36);


#ASKING THE USER FOR THE VALUES;

name = input("Enter Name: ");
age = input("Enter age: ");

def greet_user(name, age):
    print("Hi " + name);
    print(f"You look {age} years old");

greet_user(name, age);