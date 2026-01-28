# This program is a to-do list application that allows users to displays, add, update, and delete tasks

import os

tdl = ["Do maths assignments","Do python project","Play Bgmi"]

def menu_bar():
    print("--------------   Menu   --------------")
    print("1. Display the to-do-list tasks")
    print("2. Update the to-do-list task")
    print("3. Delete task from to-do-list")
    print("4. Add a task to to-do-list")
    print("5. Exit")
    print("--------------------------------------")


def display_tdl(tdl):
    print("   *** To-Do-List ***   ")
    i = 1
    for li in tdl:
        print(f"{i} -> {li}")
        i = i+1

def update_tdl(tdl):
    display_tdl(tdl)
    n = int(input("Enter the task numenr to update - "))
    if n <= len(tdl):
        new_task = input("Enter the task to be updated with - ")
        tdl[n-1] = new_task
        print("Successfully Updated the task")
    else:
        print("You Entered the wrong number")

def delete_task(tdl):
    display_tdl(tdl)
    n = int(input("Enter the task number to delete - "))
    if n <= len(tdl):
        tdl.pop(n-1)
        print("Successfully Deleted the task from the list")
    else:
        print("Enter the correct task number")

def add_task(tdl):
    task = input("Enter the task to add - ")
    print("1. append")
    print("2. add at specific position")
    n = int(input("choose option - "))
    if n == 1:
        tdl.append(task)
        print("Task successfully added")
    elif n == 2:
        display_tdl(tdl)
        k = int(input("Enter the position to add - "))
        tdl.insert(k-1,task)
        print("Task successfully added")
    else:
        print("You Entered the wrong option")

def press_key_to_exit():
    key = input("\nPress Enter key to go to menu...")
    print("\n")



is_true = True
while is_true:
    menu_bar()
    n = int(input("Enter the Option - "))

    match n:
        case 1:
            display_tdl(tdl)
            press_key_to_exit()
            os.system("cls")
        case 2:
            update_tdl(tdl)
            press_key_to_exit()
            os.system("cls")
        case 3:
            delete_task(tdl)
            press_key_to_exit()
            os.system("cls")
        case 4:
            add_task(tdl)
            press_key_to_exit()
            os.system("cls")
        case 5:
            is_true = False
        case _:
            print("Please enter the correct option from the given menu")
            press_key_to_exit()
            os.system("cls")

