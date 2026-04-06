#function 
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return"error:divide by zero is impossible"
    else:
        return a/b
def calculator():
    while True:
        print("\n==calculator menu ==")
        print("1.add")
        print("2.subtract")
        print("3.multiply")
        print("4.divide")
        print("5.exit")
        
#user to to choose an operation
        choice = input("Choose operation (1-5): ")

        if choice == "5":
            print("Thanks to data_science! Goodbye")
            break 

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            # if user enters non-numeric input it display INVALID
            print("Invalid number inpu:enter again.")
            continue
#to perform choosen operation
        if choice =="1":
            print("Result:",add(num1,num2))
        elif choice =="2":
            print("Result:",subtract(num1,num2))  
        elif choice =="3":
            print("Result:",multiply(num1,num2)) 
        else:
            print("Result:",divide(num1,num2)) 
calculator()