"""
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S is made only of the following characters: '(', '{', '[', ']', '}' and/or ')'."""

def solution(S):
 
    stack = [0] * len(S)
    size = 0

    if S == "":
        return 1
    
    if S[0] == "}" or S[0] == "]" or S[0] == ")":
        return 0

    for i in range(len(S)):

        if S[i] == "{":
            stack[size] = 1
            size += 1

        if S[i] == "[":
            stack[size] = 2
            size += 1

        if S[i] == "(":
            stack[size] = 3
            size += 1

        if S[i] == ")" and stack[size-1] == 3:
            size -= 1

        if S[i] == "]" and stack[size-1] == 2:
            size -= 1

        if S[i] == "}" and stack[size-1] == 1:
            size -= 1

    if size == 0:
        print(1)
    
    else:
        print(0)
        
solution("{[()]}")
