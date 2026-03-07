


input = ["[{{()}}]", "[[[}}()" ,"[{}()]" ]

def is_valid_parenthesis(input):
    brackets_map = {"}": "{", ")": "(", "]": "["}
    res = []
    for i in input:
        stack = []
        for j in i:
            if j not in brackets_map:
                stack.append(j)
            else:
                if not stack or (stack.pop() != brackets_map[j]):
                    break

        res.append(len(stack)==0)
    return res

print(is_valid_parenthesis(input))


