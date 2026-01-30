print("THE CALCULATOR FOR THE STUDENTS")
print("1.Additon")
print("2.Substraction")
print("3.Multiplication")
print("4.Divison")
print("5.Modules")
print("6.Average")
while True:
    print("Enter your choice for the artnematics operation:")
    choice=int(input("Choice:"))
    print("EXIT FROM THE PROGRAM PRESS \"7\"")
    if(choice==1):
        num1=int(input("Enter the first number: "))
        num2=int(input("Enter the Second number: "))
        sum=num1+num2
        print("THE ADDITION OF TWO NUMBER IS :",sum)
    elif(choice==2):
        num1=int(input("Enter the first number: "))
        num2=int(input("Enter the Second number: "))
        sub=num1-num2
        print("THE SUBSTRACTION OF TWO NUMBER IS :",sub)
    elif(choice==3):
        num1=int(input("Enter the first number: "))
        num2=int(input("Enter the Second number: "))
        mul=num1*num2
        print("THE MULTIPLICATION OF TWO NUMBER IS :",mul)
    elif(choice==4):
        num1=int(input("Enter the first number: "))
        num2=int(input("Enter the Second number: "))
        div=num1/num2
        print("THE DIVISON OF TWO NUMBER IS :",div)
    elif(choice==5):
        num1=int(input("Enter the first number: "))
        num2=int(input("Enter the Second number: "))
        mod=num1%num2
        print("THE MODULUS OF TWO NUMBER IS :",mod)
    elif(choice==6):
        num1=int(input("Enter the first number: "))
        num2=int(input("Enter the Second number: "))
        avg=num1+num2/2
        print("THE AVERAGE OF TWO NUMBER IS :",avg)
    else:
        print("EXIT")
        break
    
    
    
        