s = input('expression: ')
tokens = []
while True:
    for i, ch in enumerate(s):
        if ch in {'+', '-', '*', '/'}:
            tokens.append(float(s[:i]))
            tokens.append(s[i])
            s = s[i+1:]
            break
    else:
        tokens.append(float(s))
        break

print(tokens)

for i in range(len(tokens) - 1, 0, -1):
    try:
        token = tokens[i]
        if token == '*':
            tokens[i-1] = tokens[i-1] * tokens[i+1]
            del tokens[i:i+2]
        if token == '/':
            tokens[i - 1] = tokens[i - 1] / tokens[i + 1]
            del tokens[i:i + 2]
        if token == '+':
            tokens[i-1] = tokens[i-1] + tokens[i+1]
            del tokens[i:i+2]
        if token == '-':
            tokens[i - 1] = tokens[i - 1] - tokens[i + 1]
            del tokens[i:i + 2]
    except IndexError:
        continue


print(*tokens) # = tokens[0]