file1 = open("C:\Users\Alexa\Downloads\CIS 2348\inputDates.txt",'r')
dates = file.readlines()

months = {"January":"1","February":"2","March":"3","April":"4","May":"5","June":"6","July":7,"August":"8","September":"9",
          "October": "10","November":"11","December":"12"}


for x in dates:
    if x =="-1":
        break

    try:
        y = x.split()
        num = len(y)
        if numb!=3:
            continue
        mon = y[0]
        day = y[1]
        year = y[2]
        d,comma = day.split(',')
        for a in range(12):
            if x.find(months[x]) >= 0:
                mo = x(a+1)
                solution = mo + '/' + d + '/' + y
                print(solution)
                break
    except ValueError:
        continue
file1.close()



















