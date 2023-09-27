try:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    opp = input("Enter Opp, Eg * or + or / or - : ")

    if opp == "+":
        print(num1 + num2)
    elif opp == "-":
        print(num1 - num2)
    elif opp == "/":
        print(num1 / num2)
    elif opp == "*":
        print(num1 * num2) #print(int(num1 * num2)) this converts the result to an int ie casting
    else:
        print("Invalid, Enter opp: * or + or / or -")

except ValueError:
    print('please enter a number')
except:
    print('please enter a number')
