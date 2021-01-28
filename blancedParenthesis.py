blanced = "{[]}"
blanced2 = "{[]{}}"
unblanced2 = "{[]{}}}"
open_parenthesis = ["(","{","["]
closed_parenthesis = [")","}","]"]


def is_blanced(inputStr):
    stack = []

    for i in inputStr:
        if i in open_parenthesis:
            stack.append(i)
        elif i in closed_parenthesis:
            if ((len(stack) > 0) and (open_parenthesis[closed_parenthesis.index(i)] == stack[len(stack) -1])) :
                stack.pop()
            else:
                return "Unbalanced"
 
    if len(stack) == 0: 
        return "Balanced"
    else: 
        return "Unbalanced"
        
print(is_blanced(unblanced2))

