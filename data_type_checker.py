Value = input("Input a value: ");

if type(Value) == str:
    print(Value + "Is a string");
elif type(Value) == int:
    print(Value + " Is an integer");
else:
    print("We don't know the data type of " + Value);