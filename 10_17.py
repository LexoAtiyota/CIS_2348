user_input = input().split()

for i in range(len(user_input)):
    user_input[i] = int(user_input[i])

user_input.sort()

for num in user_input:
    if num >= 0:
        print(num, end=' ')