from pathlib import Path


def create_file(command):
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


def delet_file(command):
    file_path = command[1]
    if Path(file_path).exists():
        Path(file_path).unlink()
        print(f"{file_path} DELETED")
    else:
        print("ERROR")
    start()


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


def start():
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


if __name__ == "__main__":
    start()
