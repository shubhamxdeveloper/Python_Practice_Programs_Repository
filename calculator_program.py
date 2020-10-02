print("Enter 1st Number")
num1=int(input())

print("Enter 2nd Number")
num2=int(input())

print("\n1-Add \n2-Sub \n3-Mul \n4-Div")
cal=int(input())

if(cal==1):
    res=num1+num2
    print("Sum of two numbers is:",res)
    
elif(cal==2):
    res=num1-num2
    print("Substraction of two numbers is:",res)
    
elif(cal==3):
    res=num1*num2
    print("Multiplication of two numbers is:",res)
    
elif(cal==4):
    res=num1/num2
    print("Division of two numbers is:",res)