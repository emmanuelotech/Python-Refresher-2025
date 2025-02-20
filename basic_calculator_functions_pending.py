"""
Activities:
    Take user Input: number 1: Number 2
    Take user Ops:
    Dispaly answer:
"""

def take_user_input():
    number_1 = input("number 1: ");
    number_2 = input("number 2: ");


def operation():
    ops = str(input("Choose[*+/%]: "));
    while ops not in ["+","*","/","%"]:
        print("Wrong Operation:")
        ops = input("Choose Again: [*+/%]: ");
    return ops

def computing_answer():
    pass;

take_user_input();
operation();
print(operation())
