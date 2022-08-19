
stack = []
print("Press 1 for Insertion")
print("Press 2 for deletion")
i = int(input("enter the choice"))

if i == 1:
    num1 = int(input("Enter the Number you want to Enter"))
    stack.append(num1)
    print("The",num1,"was successfully added ")
    
elif i==2:
    if(stack.__len__ == 0):
        print("the list is empty")
    else:
        stack.pop()
else:
    print("Not a wvalid input")