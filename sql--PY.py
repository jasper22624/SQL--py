# this code is for reading basic DB in python  by jasper guo


# imports
import sqlite3


def print_cars():
    db = sqlite3.connect('SQL--py.db')
    cursor = db.cursor()
    cursor.execute('select name,top_speed,horsepower,makers.maker_name from cars join makers on cars.maker_id = makers.maker_id order by name;')
    result = cursor.fetchall()
    print(" ______________________________________________________________________________")
    print("|name                               |topspeed|horsepower|  maker               |")
    for i in result:
        print(f"|{i[0]:<35}|  {i[1]:<6}|   {i[2]:<7}|  {i[3]:<20}|")
    print("|___________________________________|________|__________|______________________|")
    db.close()  # close the DB that opened


def print_cars_by_topspeed():
    db = sqlite3.connect('SQL--py.db')
    cursor = db.cursor()
    cursor.execute('select name,top_speed,horsepower,makers.maker_name from cars join makers on cars.maker_id = makers.maker_id order by top_speed desc;')
    result = cursor.fetchall()
    print(" ______________________________________________________________________________")
    print("|name                               |topspeed|horsepower|  maker               |")
    for i in result:
        print(f"|{i[0]:<35}|  {i[1]:<6}|   {i[2]:<7}|  {i[3]:<20}|")
    print("|___________________________________|________|__________|______________________|")
    db.close()  # close the DB that opened


def print_cars_by_horsepower():
    db = sqlite3.connect('SQL--py.db')
    cursor = db.cursor()
    cursor.execute('select name,top_speed,horsepower,makers.maker_name from cars join makers on cars.maker_id = makers.maker_id order by horsepower desc;')
    result = cursor.fetchall()
    print(" ______________________________________________________________________________")
    print("|name                               |topspeed|horsepower|  maker               |")
    for i in result:
        print(f"|{i[0]:<35}|  {i[1]:<6}|   {i[2]:<7}|  {i[3]:<20}|")
    print("|___________________________________|________|__________|______________________|")
    db.close()  # close the DB that opened


# main code
while True:
    user_input = input("\nWhat would you like to do?\n1.print all cars order by name\n2.print all cars order by top speed\n3.print all cars by horsepower\n4.exit\n")
    if user_input == '1':
        print_cars()
    elif user_input == '2':
        print_cars_by_topspeed()
    elif user_input == '3':
        print_cars_by_horsepower()
    elif user_input == '4':
        break
    else:
        print('That was not an option.\n')

