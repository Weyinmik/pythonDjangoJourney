"""
IF...ELIF...ELSE Statements

Definition:
An IF statement can be combined with an ELSE statement

An ELSE statement contains the block of code that executes if the conditional expression
in the IF statement resolves to a FALSE value

The ELSE is an optional statement to the IF

The ELIF statement allows you to check multiple expressions for TRUE value
Similar to the ELSE, the ELIF statement is an optional statement

The can be a number of ELIF statements which are following an IF statement.
E.g:
if expression1:
    statement(s)
elif expression2:
    statements(s)
elif expression3:
    statement(s)
else:
    statement(s)
"""

# if...elif...else statements

if 3>2:
 print("Right")             #Result:Right

if 4>7:
 print("Right")             # No output
else:
    print("Wrong")          #Result:Wrong
    
a = 3
b = 5

if a > b:
    print("Yes, it is right!!!")
else:
    print("Try again")


drink = "Tea"

if drink == "Coffee":
    print("Humanity runs on Coffee")
else:
    print("Where there is a Tea, there is hope")


drink = "Tea"

if drink == "Coffee":
    print("Humanity runs on Coffee")
else:
    print("Where there is a Tea, there is hope")
    
drink = "Tea"

drink = "Coke"

if drink == "Coffee":
    print("Humanity runs on Coffee")
elif drink == "Water":
    print("Water is the soul of Earth!!")
elif drink == "Coke":
    print("Coke is the new fuel for the Programmer!!!")
else:
    print("Where there is a Tea, there is hope")