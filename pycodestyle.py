#!/usr/bin/python3
"""A python programm that passes the pycodestyle"""
def show_name(name):

"""Parameter that is used to print someone's name.

:param name:The name that is to be printed
"""

print(f"Greetings, {name}!")

def main():
    user_name = "John"
    show__name(user_name)

if __name__ == '__main__':
    main()
