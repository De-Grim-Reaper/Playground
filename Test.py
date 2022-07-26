import math
import time
import random
import os
import shutil

# print("Hey man, I got a gift for you... open it?")
# ans = input("Enter yes to open gift: ")
# ans_1 = ans.lower()

# while ans_1 != "yes":
#    print("Type yes, i know you wouldn't regret it")
#    ans = input("Enter yes to open gift: ")
#    ans_1 = ans.lower()

# if ans_1 == "yes":
#    print(
#      "Congrats, you'll receive your gift in the next 20s. Wait patiently...")

# for seconds in range(20, 0, -1):
#     print(seconds)
#     time.sleep(1)


# print("HAHA! GOT YOU Nigga!!!")

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# sapa = int(input("how much sapa?: "))
# symbols = input("Enter a symbol: ")

# for i in range(rows):
#    for j in range(columns):
#        for k in range(sapa):
#            print(symbols, end="")
#    print()

# while True:
#    name = input("Enter your name: ")
#    if name != "":
#        break

# print(name + " You sure are one son of a bitch!")
# phone_number = "+234617162823-8738783-9393-67889"

# for i in phone_number:
#    if i == "-" or i == "+":
#        continue
#    print(i, end="")

# for i in range(30, 0, -1):
#    if i == 11 or i == 13 or i == 17:
#        continue
#    else:
#        print(i)

# print("Enter your favorite food in order:")
# food = [input("<i>: "), input("<ii>: "), input("<iii>: "), input("<iv>: ")]

# food.append("fish")
# food.sort()

# for i in food:
#    if i == "a":
#        break
#    print(i, end=", ")

# student = ("Male", 21, "Stupid")
#
# for i in student:
#    print(i)

# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "cup", "plate", "knife"}

# utensils.add("napkin")
# names.remove("fade")
# dishes.update(utensils)

# for i in dishes:
#    print(i)

# states = {'Ondo': 'Akure',
#          'Lagos': 'Ikeja',
#          'Oyo': 'Ibadan',
#          'Ogun': 'Abeokuta'}

# states.update({'Plateau': 'Jos'})
# states.update({'Oyo': 'Iwo')})
# states.pop('Ogun')
# states.clear()

# print(states['Oyo'])
# print(states.get('Ondo'))
# print(states.keys())
# print(states.values())
# print(states.items())

# for key, value in states.items():
#    print(key, value)

# name = input("What is your name? ")

# while name[:10].isdigit():
#    print("Type in alphabets bitch!")
#    name = input("What is your name? ")

# if name[:5].islower() or name[:5].isupper():
#    name = name.capitalize()

# print("Sup " + name + "!")

# def middle(x, y):
#    print("Fuck you " + x + y)
#    print("You are Stupid, " + x + y)


# myname = input("What's your name bitch! ")
# exclaim = "!"
# if myname[:5].islower() or myname[:5].isupper():
#    myname = myname.capitalize()
# middle(myname, exclaim)

# def multiply(x, y):
#    result = x - y
#    return result


# no_1 = int(input("Enter a number: "))
# no_2 = int(input("Enter a number: "))

# cum = multiply(y=no_1, x=no_2)

# print(cum)

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)

# print(num)

# print(round(abs(float(input("Enter a whole positive number: ")))))

# def display_name():
#    name = "Fish"
#    return name


# name = "smelly"
# print(name)
# print(display_name())

# def add(*args):  # *args = a parameter that will pack all arguments into a tuple
#                           useful so that a function can accept a varying amount of arguments
#                          Note: the word 'args' isn't definite! Only '*' is necessary
#    sum = 0
#    for i in fish:
#        sum += i
#    return sum


# print(add(3, 2, 3))

# def hello(**kwargs):  # **kwargs = a parameter that will pack all arguments into a dictionary
#                                    useful so that a function can accept a varying amount of key arguments
#                                    Note: the word 'kwargs' isn't definite! Only '**' is necessary
#    print("Hello " + kwargs['first'] + " " + kwargs['last'])
#    print("Hello", end=" ")
#    for key, value in kwargs.items():
#        print(value, end=" ")


# hello(first="Bitch", middle="Ass", last="Motherfucker")

# animal = input("Enter an animal: ")
# item = "moon"

# print("The " + animal + " jumped over the " + item)
# print("The {} jumped over the {}.".format(animal, item))
# print("The {1} jumped over the {0}.".format(animal, item))  #positiional argument
# print("The {animal} jumped over the {item}.".format(animal=input("Enter an animal: "), item="moon")) #keyword argument

# text = "The {} jumped over the {}"
# print(text.format(animal, item))

# name = input("Enter your name: ")

# print("Hello, my name is {:10}.Nice to meet ya".format(name))
# print("Hello, my name is {:<10}.Nice to meet ya".format(name))
# print("Hello, my name is {:>10}.Nice to meet ya".format(name))
# print("Hello, my name is {:^10}.Nice to meet ya".format(name))

# number = 3.14159
# print("The number pi is {:.2f}".format(number))

# number = 10000000000000
# print("The number is {:,}".format(number))
# print("The number is {:b}".format(number))
# print("The number is {:o}".format(number))
# print("The number is {:x}".format(number))
# print("The number is {:e}".format(number))

# x = random.randint(1, 10)
# y = random.random()

# myList = ["Rock", "Paper", "Scissors"]
# z = random.choice(myList)

# cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
# random.shuffle(cards)

# print(cards)

# exception = events detected during execution that interrupts the flow of a program

# try:
#    numerator = int(input("Enter a number to be divided: "))
#    denominator = int(input("Enter a number to divide by: "))
#    result = numerator / denominator
#    print(result)

# except ValueError as e:
#    print("--{}".format(e))
#    print("~You entered the wrong value idiot!")
# except ZeroDivisionError as e:
#    print("--{}".format(e))
#    print("~You can't divide by zero fool!")
# except Exception as e:
#    print("--{}".format(e))
#    print("~Something went wrong :(")
# else:
#    print(result)
# finally:
#    print("This will always execute.")

# folder = "C:\\Users\\Sammy\Desktop\\test.txt"
# if os.path.exists(folder):
#    print("Location exists!")
#    if os.path.isfile(folder):
#        print("That is a file!")
#    if not os.path.isfile(folder):
#        print("That is not a file!")
#    elif os.path.isdir(folder):
#        print("That is a directory!")
# else:
#    print("Location doesn't exist!")

# try:
#    with open('Test.txt') as e:
#        print(e.read())
# except FileNotFoundError as er:
#    print(er)
#    print('File not found :(')
# print(e.closed)

# text = "\nSee ya!"

# with open('test', 'a') as file:
#    file.write(text)


# copyfile() = copies contents of a file
# copy() =     copyfile() + permission mode + destination can be a directory
# copy2() =    copy() + copies meta data (file's creation and modification times)

# shutil.copyfile('test', 'text.s') #src,dst

# source = 'text.s'
# destination = 'C:\\Users\\Sammy\\Desktop\\TEXT'

# try:
#    if os.path.exists(destination):
#        print("There is already a file there!")
#    else:
#        os.replace(source, destination)
#        print(source+" Was moved.")

# except FileNotFoundError as e:
#    print(e)
#    print(source+" Was not found!")


# try:
#    os.remove('test')        #     deletes a file
#    os.rmdir('Empty_Folder') #     deletes an empty directory
#    shutil.rmtree('Folder')  #     deletes a directory and everything within
# except FileNotFoundError:
#    print("File was not found")
# except PermissionError:
#    print("--You do not have permission to delete that")
# except OSError:
#    print("--You cannot delete that using that function")
# else:
#    print("~Task accomplished successfully.")

# x = input("Input a number ")

# while x.isalpha() or len(x) == 0:
#    print("~Don't you know how to read?")
#    print("~Don't be dumb.\n")
#    x = input("Input a number ")

help('modules')
