open_list = ['[','{','(']
close_list = [']','}',')']
def well_bracketed(mystr):
    try:
        stack = []
        for i in mystr:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                pos = close_list.index(i)
                if ((len(stack) > 0) and open_list[pos] == stack[len(stack) - 1]):
                    stack.pop()
                else:
                    return False
                return len(stack) == 0
    except Exception as e:
        print(f"An error occured:{e}")
        return False
    
expression = input("Enter an expression.")
if well_bracketed(expression):
    print("The expression is well bracketed.")
else:
    print("The expression is not well braketed.")
        