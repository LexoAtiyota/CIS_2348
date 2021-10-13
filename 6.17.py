pw = input()
result = ""

a = 0
while a < len(pw):
    variable = pw[a]
    if variable == 'i':
        result += '!'
    elif variable == 'a':
        result += '@'
    elif variable == 'm':
        result += 'M'
    elif variable == 'B':
        result += '8'
    elif variable == 'o':
        result += "."
    else:
        result += variable
    a += 1

result += "q*s"
print(result)
