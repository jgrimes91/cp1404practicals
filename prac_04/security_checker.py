def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    user_name = input("Please enter your username: ")

    while user_name not in usernames:
        print("Access Denied")
        user_name = input("Please enter a valid username: ")
    else:
        print("Access Granted")


main()
