
#a
element = 1
months = {"January":"1","February":"2","March":"3","April":"4","May":"5","June":"6","July":7,"August":"8","September":"9",
          "October": "10","November":"11","December":"12"}
while element ==1:
    try:
        x = input(" Please enter the month day, year:")
    except SyntaxError:             #Using this just in case of parsing errors
        continue
    if x=="-1":
       break

    try:
        y = x.split()
        numb = len(y)
        if numb!=3:
            continue
        mon= y[0]               #Month is the first Variable
        day = y[1]              #Day is the second input variable
        year = y[2]
        d,comma = day.split(",")

        for a in range(12):
            if x.find(months[x])>=0:     #Using Find Function in the the months dictionary
                mths = x(a+1)
                solution = mths + '/' + d + '/ ' + y
                print(solution)
                break
    except ValueError:
        continue






