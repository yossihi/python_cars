# car garage: model, brand, color, license
# print, add, 

from enum import Enum
import os
import json

class Commands(Enum):
    PRINT= 1
    ADD = 2
    SEARCH = 3
    DELETE = 4
    EXIT = 5

myCars = []
my_cars_file = 'myCar.json'

def menu():
    for x in Commands:
        print(f"{x.value} - {x.name}")
    return Commands(int(input('what is you selection:')))

def display():
    for car in myCars:
        print(car)

def add_car():
    myCars.append({"brand":input("Enter car brand:"),"model":input("Enter car model:"),"color":input("Enter car color:"),"license":input("Enter car license:")})



def exit_func():
    print("test")
    json_string = json.dumps(myCars)

    with open(my_cars_file, 'w') as filesave:
        filesave.write(json_string)
    print('good bye')
    exit()

def load_json():
    global myCars
    try:
        with open(my_cars_file, 'r') as fileLoad:
            json_string = fileLoad.read()
        myCars = json.loads(json_string)
    except: return myCars
        
def searchCar():
    license_search = int(input("what's the license number: "))
    for car in myCars:
        if int(car.get("license")) == license_search:
            print(f"\nbrand: {car.get("brand")} \nmodel: {car.get("model")} \ncolor: {car.get("color")}\n ")

def del_cer():
    del_license = int(input("whats the license number of the car that you want to delete: "))
    for car in range(len(myCars)):
        if int(myCars[car].get("license")) == del_license:
            commit = int(input("the car is in the list, would you like to delete it? \n1-YES \n2-NO "))
            if commit == 1:
                print(f"this car has been removed: {myCars[car]}")
                car_del = myCars.pop(car)
                return
                



def main():
    os.system('cls')
    load_json()
    
    while(True):
        userselection = menu()
        if userselection == Commands.EXIT: exit_func()
        if userselection == Commands.PRINT: display()
        if userselection == Commands.ADD: add_car()
        if userselection == Commands.SEARCH: searchCar()
        if userselection == Commands.DELETE: del_cer()


if __name__ == "__main__":
    main()
