def addition(value1, value2):
    return value1 + value2

def subtraction(value1, value2):
    return value1- value2

def multiplication(value1, value2):
    return value1* value2


def division(value1, value2):
    return value1/ value2


print(" select the  operation :")
print(
   "a. Addition\n"\
   "b. Subtraction\n" \
   "c. Multiplication\n" \
   "d. Division\n")

operation = input("Enter the operation a/b/c/d:")

value1= int(input("Enter the first value : "))
value2= int(input("Enter the second value : "))

if operation == "a":
    print(value1, "+", value2, "=",
          addition(value1, value2))

elif operation == "b":
    print(value1, "-", value2, "=",
          subtraction(value1, value2))

elif operation == "c":
    print(value1, "*", value2, "=",
          multiplication(value1, value2))

elif operation == "d":
    print(value1, "/", value2, "=",
          division(value1, value2))
else:
    print("Invalid input")