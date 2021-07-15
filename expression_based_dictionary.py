import ast

i = input().split(" ")
d = input()
dic = ast.literal_eval(d)

if len(i) == 3 and (i.count('and') == 1 or i.count('or') == 1):
    a, operator, b = i
elif len(i) == 5 and (i.count('and') == 2):
    a, operator_one, b, operator_two, c = i 
elif len(i) == 5 and i.count('and') == 1 and i.count('or') == 1:
    i = ['A' if value=='(A' else value for value in i]
    i = ['A' if value=='A)' else value for value in i]
    i = ['B' if value=='(B' else value for value in i]
    i = ['B' if value=='B)' else value for value in i]
    i = ['C' if value=='C)' else value for value in i]
    i = ['C' if value=='(C' else value for value in i]
    i = ['D' if value=='D)' else value for value in i]
    i = ['D' if value=='(D' else value for value in i]

    a , operator_one, b, operator_two, c = i

elif len(i) == 7 and i.count('and') == 2 and i.count('or') == 1:
    i = ['A' if value=='(A' else value for value in i]
    i = ['A' if value=='A)' else value for value in i]
    i = ['B' if value=='(B' else value for value in i]
    i = ['B' if value=='B)' else value for value in i]
    i = ['C' if value=='C)' else value for value in i]
    i = ['C' if value=='(C' else value for value in i]
    i = ['D' if value=='(D' else value for value in i]
    i = ['D' if value=='D)' else value for value in i]
    a, operator_one, b, operator_two, c, operator_three, d = i

    
if len(i) == 3:
    if operator == 'and':
        print(f'{dic[a]}{dic[b]}')
    elif (operator == 'or'):
        try: 
            print(f'{dic[a] or {dic[b]}}')
        except KeyError:
            print(f'{dic[b] or dic[a]}')
elif len(i) == 5:
    if operator_one == 'and' and operator_two == 'and':
        print(f'{dic[a]}{dic[b]}{dic[c]}')
    elif operator_one == 'and' and operator_two == 'or':
        print(f'{dic[a]}{dic[b] or dic[c]}')

elif len(i) == 7:
    try:
        print(f'{dic[a]}{dic[b] or dic[c]}{dic[d]}')
    except KeyError:
        print(f'{dic[a]}{dic[c] or dic[b]}{dic[d]}')