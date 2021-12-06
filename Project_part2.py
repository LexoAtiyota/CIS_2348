#Alex Atiyota 1805848

import pandas

#Using Pandas to get a better look at the dataset/csv file


data = pandas.read_csv('FullInventory.csv')
print(type(data))

data_dict = data.to_dict()
data = pandas.DataFrame(data_dict) #To.dict shows it in a dictionary format
print(data)
print()
#This shows the csv file in column format
print('This is the current inventory of the items presented above')

#Taking the user's input for their choice of selection
inventory_list = open('FullInventory.csv' )
ask_user = input('Enter a manufacturer and the corresponding item you are currently looking for, or press q to exit the query\n')
while ask_user != 'q':
    item_guess = []
    ask_user_parts = ask_user.split('')
    for item in inventory_list:
        if ask_user_parts[0] == item[1]:
            if ask_user_parts[1] == item[2]:
                if item[0] not in inventory_list and item[4] != 'damaged\n':
                    item_guess.append(item) #This will add the item that they chose

    choice_of_item = len(item_guess)
    #This should determine the result
    if choice_of_item == 1:
        item = item_guess[0]
        print('The item you have chosen is ', item[0], item[1], item[2])
    elif choice_of_item == 0:
        print('This item is not in the current inventory shown above')


    #Have to create an alternate section for another item type
    alternate_user = ask_user_parts[1] + 'FullInventory.csv'
    choices = open(alternate_user)
    list_of_choices = choices.readlines()
    choices.close()


    for item in list_of_choices:
        if ask_user_parts[0] != item[1]:
            for another_item in inventory_list:
                if item[1] == another_item[1]:
                    print('Good choice. There are other alternate choices you can choose from the inventory like', item)
    
    another_input = input("Please enter a manufacturer and the corresponding item you are currently looking for or press q to exit the query\n")
