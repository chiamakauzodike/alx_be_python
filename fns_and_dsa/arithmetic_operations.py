#arithmetic operator
def perform_operation(num1, num2, operation):
    if opation =='add':
        return num1 + num2
    elif operation == 'subtract':
        return num1-num2
    elif operation == 'divide':
        if num2 == 0:
            return "Division be zero error"
        else:
            return num1/num2
    else:
        return "Invalid Operation"
