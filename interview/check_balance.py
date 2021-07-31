from stack import Stack

def check_balance(string):
    pairs = {')': '(',
             '}': '{',
             ']': '['}
    stack = Stack()
    for bracket in string:
        if bracket in pairs.keys() and stack.peek() == pairs[bracket]:
            stack.pop()
        else:
            stack.push(bracket)
    if stack.is_empty():
        print('Сбалансированно')
        return True
    else:
        print('Несбалансированно')
        return False