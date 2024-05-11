# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME
# EMAIL
# STUDENT ID

from pathlib import Path
from profile import Profile
administrator_mode = False


def mode():
    global administrator_mode
    mode  = input("Enter  Mode: ")
    if 'admin' in mode:
        administrator_mode = True
    else:
        administrator_mode  = False
    return administrator_mode



def read_file(command):
    file_path = command[1]
    if Path(file_path).exists():
        with open(file_path, 'r')as file:
            lines = file.readlines()
            if lines:
                for line in lines:
                    print(line)
            else:
                print("EMPTY")
                start()
    else:
        print("ERROR")
    start()


def delet_file(command):
    file_path = command[1]
    if Path(file_path).exists():
        Path(file_path).unlink()
        print(f"{file_path} DELETED")
    else:
        print("ERROR")
    start()


def start():
    if administrator_mode:
        command = input("Please Enter Command: ")
        command_list = command.split(' ')
        type = command_list[0]
        if type == 'C':
            create_file(command_list)
        elif type == 'R':
            read_file(command_list)
        elif type == 'D':
            delet_file(command_list)
        else:
            print("Please Enter Correct Command")
            start()
    else:
        command = input("Please Enter Command: ")
        if command == 'c' or 'C':
            create_file()


def create_file(command = None):
    if administrator_mode:
        dir_path = command[1]
        command_extention = command[2]
        file_name = command[3]
        file_path = f"{dir_path}\\{file_name}.dsu"
        if Path(file_path).exists():
            print("file already exists")
        else:
            Path(file_path).touch()
            print(f'{file_path}')
        start()
    else:
        directory = input("input directory path: ")
        name = input("input file name: ")
        file_path = f"{directory}\\{name}"
        if Path(file_path).exists():
            print("file already exists")
        else:
            Path(file_path).touch()
            print(f"file: {name}.dsu created at {file_path}")
        username = input("Enter username: ") 
        password = input("Enter password: ")
        bio = input("Enter bio: ")
        profile = Profile(username = username, password = password, bio = bio)
        profile.save_profile(path = file_path)
        start() 
    

if __name__ == "__main__":
    mode()
    if not administrator_mode:
         print("""
        List of Commands:
        C - create file
        R - read file
        D - delete file
        """)
    start()