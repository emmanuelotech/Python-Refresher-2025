"""
IF STATEMENTS
Basically giving python a condition to evaluate then return
particular value if a particular condition is met.


"""
a = 2;
b = 2;

if a > b:
    print(str(a) + " is greater than " +str(b));
elif a == b:
    print("The numbers are equal");
else:
    print("You fucked up!! #Mustang");


name = "Emmanuelotech"
school = "Emmanuela";

if name == school or len(name) > len(school):
    print("The strings are equal bro");
elif name > school & len(school) != len(name):
    print("These shit ain't equal");
else:
    print("You fucked up again");
