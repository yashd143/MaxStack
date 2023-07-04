def create_stack():
    stack = []
    return stack

# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0

# Adding items to stack
def push(stack, item):
    stack.append(item)

# Removing from the stack
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
    total = 0
    for ele in range(0, n1):
        val = int(stack[ele])
        total += val
    return total


#Driver Code
stack = create_stack()
n1 = len(stack)

#Input for Stack
while True:    
    # Asks user to add items to stack
    item = input("Enter an item to push onto the stack (or 'q' to quit): ")
    
    # Add the item to the stack
    push(stack, item)
    
    #Breaks loop
    if item == 'q':
        break

print("Max Value of Stack: " + str(maxValue(stack, n1)))
print("Total sum of elements: " + str(sumAll(stack,n1)))