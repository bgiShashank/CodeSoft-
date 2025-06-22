print("========Calculator========")
print("1. Addition" ,
      "\n2. Subtraction" ,
       "\n3. Multiplication" ,
       "\n4. Division"
       )
choice = int(input("Enter your choice : "))

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number :"))

if choice == 1 :
    print("Result :" , num1 + num2)
elif choice == 2 :
    print("Result :" , num1 - num2)
elif choice == 3 :
    print("Result :" , num1 * num2)
elif choice == 4 :
    if num1 != 0:
        print("Result :" , num1 / num2)
    else: 
        print("Error . Division by 0 is not allowed")
else:
    print("Invalid choice . Please choose a valid option")
