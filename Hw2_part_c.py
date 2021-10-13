
file1 = open("C:\Users\Alexa\Downloads\CIS 2348\inputDates.txt")
dates = file1.readlines()

months = {"January":"1","February":"2","March":"3","April":"4","May":"5","June":"6","July":7,"August":"8","September":"9",
          "October": "10","November":"11","December":"12"}

ct = 0
for x in dates:
    ct+1
    if x == '-1':
        break

    try:
        y = x.split()
        numbs = len(y)
        if numbs!=3:
            continue
        mon = y[0]
        day = y[1]
        year = y[2]
        d, comma = day.split(',')
        for a in range(12):
            if x.find(months[x])>=0:
             mo = str(x+1)
        solutions = mo +'/' + d + '/' + y
        if count>0:
            file2 = open('parsedDates.txt','a')
            file2.write('solutions\n')
            file2.close()
        else:
            file3 = open('parsedDates.txt''w')
            file3.write("solutions\n")
            file3.close()
            break
    except ValueError:
        continue
file1.close()