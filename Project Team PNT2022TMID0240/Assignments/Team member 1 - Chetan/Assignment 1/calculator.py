print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=",(num1+num2))

        elif choice == '2':
            print(num1, "-", num2, "=", (num1-num2))

        elif choice == '3':
            print(num1, "*", num2, "=", (num1*num2))

        elif choice == '4':
            print(num1, "/", num2, "=", (num1//num2))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
