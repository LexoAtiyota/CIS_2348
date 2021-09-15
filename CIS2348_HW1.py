name = input("Please enter your name: ")
print('Hello', name, '!')

print("Let's calculate your birthday", name)


print('This is the birthday calculator')

#This is the current date prompt

print('Please enter the curent date respectively!')
print('Current Date')

cd_month = int(input('Month: '))
cd_day = int(input('Day: '))
cd_year = int(input('Year: '))

#This is the birthday prompt
print('Please enter your birthday respectively!')
print('Birthday')
bd_month = int(input('Month: '))
bd_day = int(input('Day: '))
bd_year = int(input('Year: '))

year_difference = cd_year - bd_year

#In case birthday and current date match
if cd_month==bd_month and cd_day==bd_day:
    print('Happy Birthday', name, '!')

print("You are ", year_difference, 'years old!')