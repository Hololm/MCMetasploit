import getpass
import os
import sys
import re
from optparse import OptionParser
from minecraft import authentication
from minecraft.exceptions import YggdrasilError
from minecraft.networking.connection import Connection
from minecraft.networking.packets import Packet, clientbound, serverbound
from dotenv import load_dotenv
import time
from tabulate import tabulate
import importlib
import inspect


load_dotenv()  #: loads variables from .env


def main():

    x: list = os.listdir("modules")  #: lists all files in the modules folder
    x.remove("schema.py")
    modules = []

    for i in x:
        if i[-3:] == ".py":  #: checks if file contains .py
            y = importlib.import_module('modules.%s' % i[:-3])  #: removes .py from the file
            try:
                if inspect.isclass(y.Exploit):  #: checks if class 'Exploit' is in file
                    modules.append(y)
            except (AttributeError, NameError):
                print("no module in file", i)

    table = []
    for y in modules:
        k = y.Exploit()
        table.append([k.name, k.description])
    print(tabulate(table, headers=['ID', 'Name', 'Description'], showindex="always", tablefmt="fancy_grid"))

    #: exploits: litebans sql dump, holographics dir traversal, log4j
    print("Logging in...")

    auth_token = authentication.AuthenticationToken()
    try:
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")
        auth_token.authenticate(email, password)
    except YggdrasilError as e:
        print(e)
        sys.exit()

    os.system('clear')
    print("Logged in as %s..." % auth_token.username)
    time.sleep(1)
    os.system('clear')


if __name__ == '__main__':
    main()
