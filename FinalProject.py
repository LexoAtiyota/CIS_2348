"""
Alex Atiyota
1805848
"""

import csv
from datetime import datetime

class InventoryO:
    def __init__(self, i_list):
        my.i_list = i_list

    def max(self):
        with open("C:\Users\Alexa\Downloads\CIS 2348\FullInventory.csv","w") as file:
            items = self.i_list
            keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer'])
            for item in keys:
                id = item
                man_n = items[item]['manufacturer']
                type_of_item = items[item]['item type']
                price = items[item]['price']
                damaged = items[item]['damaged']
                date_of_service = items[item]['service date']
                file.write('{},{},{},{},{},{}\n'.format(id,man_n,type_of_item,price,damaged,date_of_service))

    def diff_type(self):
        items = self.i_list
        diff_types = []
        keys = sorted(items.keys())
        for item in items:
            type_of_item = items[item]['item type']
            if type_of_item not in diff_types:
                diff_types.append(type_of_item)

        for type in diff_types:
            file_name = type.capitalize() + 'Inventory.csv'
            with open('./output_files/'+file_name, 'w') as file:
                for item in keys:
                    id  = item
                    man_n = items[item]['manufacturer']
                    price = items[item]['price']
                    damaged = items[item]['damaged']
                    date_of_service = items[item]['service date']
                    type_of_item = items[item]['item type']
                    if type == type_of_item:
                        file.write('{},{},{},{},{},{}\n'.format(id,man_n,type_of_item,price,damaged,date_of_service))


    def expired_service(self):
        items = self.i_list
        diff_types = []
        keys = sorted(items.keys(), key=lambda x: datetime.striptime(items[x]['service date'], '%m/%d%Y').date(), reverse=True)
        with open("C:\Users\Alexa\Downloads\CIS 2348\PastServiceDateInventory.csv", 'w') as file:
            for item in keys:
                id = item
                man_n = items[item]['manufacturer']
                price = items[item]['price']
                damaged = items[item]['damaged']
                date_of_service = items[item]['service date']
                type_of_item = items[item]['item type']
                day = datetime.now().date()
                expire_service = datetime.striptime(date_of_service, '%m/%d/%Y').date()
                expired = expire_service < day
                if expired:
                    file.write('{},{},{},{},{},{}\n'.format(id, man_n, type_of_item, price, damaged, date_of_service))


    def damage(self):


        items = self.i_list
        keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)
        with open("C:\Users\Alexa\Downloads\CIS 2348\DamagedInventory.csv",'w') as file:
            for item in keys:
                id = item
                man_n = items[item]['manufacturer']
                type_of_item = items[item]['item type']
                price = itmes[item]['price']
                date_of_service = items[item]['service date']
                damaged = items[item]['damaged']
                if damaged:
                    file.write('{},{},{},{},{}\n'.format(id, man_n, type_of_item,price,date_of_service))




if __name__ == '__main__':
    items = {}
    files = ['ManufactureList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for lines in csv_reader:
                item_id = lines[0]
                if file == files[0]:
                    items[item_id] = {}
                    man_n = lines[1]
                    type_of_item = lines[2]
                    damaged = lines[3]
                    items[item_id]['manufacturer'] = man_n.strip()
                    items[item_id]['item type'] = type_of_item.strip()
                    items[item_id]['damaged'] = damaged
                elif file == files[1]:
                    price = lines[1]
                    items[item_id]['price'] = price
                elif file == files[2]:
                    date_of_service = lines[1]
                    items[item_id]['service date'] = date_of_service


            inventory = InventoryO(items)
            inventory.max()
            inventory.diff_type()
            inventory.expired_service()
            inventory.damage()

            diff_types = []
            manufacturers = []
            for item in items:
                confirm_manufacturer = items[item]['manufacturer']
                confirmed_type = items[item]['item type ']
                if confirm_manufacturer not in diff_types:
                    manufacturers.append(confirm_manufacturer)
                if confirmed_type not in diff_types:
                    diff_types.append(confirmed_type)

            user_prompt = None
            while user_prompt != 'x':
                user_prompt = input("\nEnter a manufacturer and the type of item (ex: Dell Laptop) or enter 'x' to exit:\n")
                if user_prompt == 'x':
                    break
                else:
                    picked_manufacturer = None
                    picked_type = None
                    user_prompt = user_prompt.split()
                    invalid_input = False
                    for word in user_prompt:
                        if word in manufacturers:
                            if confirm_manufacturer:
                                invalid_input = True
                            else:
                                confirm_manufacturer = word
                        elif word in diff_types:
                            if confirmed_type:
                                invalid_input = True
                            else:
                                confirmed_type = word
                    if not confirm_manufacturer or not confirmed_type or invalid_input:
                        print("This is not in the inventory")
                    else:
                        keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)

                        match_items = []
                        similar_items = {}
                        for item in keys:
                            if items[item]['item type'] == confirmed_type:
                                day = datetime.now().date()
                                day_of_service = items[item]['item type']
                                expired_service = datetime.strptime(day_of_service, "%m%d%Y").date()
                                expired = expired_service < day
                                if items[item]['manufacturer'] == confirm_manufacturer:
                                    if not expired and not items[item]['damaged']:
                                        match_items.append((item, items[item]))
                                else:
                                    if not expired and not items[item]['damaged']:
                                        similar_items[item] = items[item]

                        if match_items:
                            item = match_items[0]
                            item_id = item[0]
                            man_n = item[1]['manufacturer']
                            type_of_item = item[1]['item type']
                            price = item[1]['price']
                            print('The item is: {}, {}, {}, {}\n'.format(item_id, man_n, type_of_item, price))

                            if similar_items:
                                similar_price = price

                                identical_item = None
                                closest_price_diff = None
                                for item in similar_items:
                                    if closest_price_diff == None:
                                        identical_item = similar_items[item]
                                        if closest_price_diff == None:
                                            closest_price_diff = abs(int(similar_price) - int(similar_items[item]['price']))
                                            item_id = item
                                            man_n = similar_items[item]['manufacturer']
                                            type_of_item = similar_items[item]['item type']
                                            price = similar_items[item]['item type']
                                            continue
                                        money_diff = abs(int(similar_price) - int(similar_items[item]['price']))
                                        if money_diff < closest_price_diff:
                                            identical_item = item
                                            closest_price_diff = money_diff
                                            item_id = item
                                            man_n = similar_items[item]['item type']
                                            price = similar_items[item]['price']
                                print("Rather, consider: {}, {}, {}, {}\n".format(item_id, man_n, type_of_item, price))

                            else:
                                print("This item is not in our inventory")



