#Creates empty stack
def create_stack():
    stack = []
    return stack

#Checking empty stack
def check_empty(stack):
    return len(stack) == 0

#Adding items to stack
def push(stack, item):
    stack.append(item)

#Removing from the stack
def pop(stack):
    if (check_empty(stack)):
        return "Stack is empty"
    return stack.pop()

#Getting max value of stack
def maxValue(stack,n1):
    if check_empty(stack):
        return 0
    value = 0
    max_value = 0
    
    #Checking for max value of stack
    for i in range(n1):
        element = int(stack[i])
        value += element
        if element > max_value:
            max_value = element
    return max_value

#Getting Sum of All Elements in Stack
def sumAll(stack, n1):
    sum = 0
    for ele in range(0, n1):
        val = int(stack[ele])
        sum += val
    return sum

#Getting Mutliplication of Elements in Stack
def multiply(stack, n1):
    total = 1
    for p in range(0, n1):
        multi = int(stack[p])
        total *= multi
    return total

#Main Code
stack = create_stack()

#Input for Stack
while True:    
    
    #Asks user to add items to stack
    item = input("Enter an item to push onto the stack (or 'q' to quit): ")
    
    #Breaks loop
    if item == 'q':
        break
    
    #Add the item to the stack
    push(stack, item)

n1 = len(stack)

print("Max Value of Stack: " + str(maxValue(stack, n1)))
print("Total sum of elements: " + str(sumAll(stack,n1)))
print("Multiplaction of all elements: " + str(multiply(stack, n1)))
