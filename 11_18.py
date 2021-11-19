user_input = input()
user_split = user_split.split(user_input)
user_split.sort()
for ordered_integers in user_split:
    if int(ordered_integers) >=0:
        print(ordered_integers, end= " ")
