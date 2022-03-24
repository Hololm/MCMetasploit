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
    modules: list = []

    for i in x:
        if i[-3:] == ".py":  #: checks if file contains .py
            y = importlib.import_module('modules.%s' % i[:-3])  #: removes .py from the file
            try:
                if inspect.isclass(y.Exploit):  #: checks if class 'Exploit' is in file
                    modules.append(y)
            except (AttributeError, NameError):
                pass

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

    print("Logged in as %s..." % auth_token.username)
    time.sleep(1)

    table = []
    for y in modules:
        k = y.Exploit()
        table.append([k.name, k.description])
    print(tabulate(table, headers=['ID', 'Name', 'Description'], showindex="always", tablefmt="fancy_grid"))

    id = int(input('Choose an exploit: '))
    exploit = modules[id]
    params = []
    funcparams = [i for i in inspect.getmembers(exploit.Exploit()) if not i[0].startswith('_') if not inspect.ismethod(i[1])]

    serverip = input('MC Server IP: ')
    serverport = int(input('MC Server Port: '))

    for x in funcparams:
        if x[0] == "client":
            params.append(Connection(serverip, serverport, auth_token=auth_token))
            continue

        if x[1] is None:
            data = input('{}: '.format(x[0]))
            params.append(data)

    success, message = exploit.Exploit(*tuple(params)).execute()
    print(success, message)


if __name__ == '__main__':
    main()
