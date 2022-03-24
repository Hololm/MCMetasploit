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


load_dotenv()


def main():

    x: list = os.listdir("modules")
    x.remove("schema.py")
    modules = []
    for i in x:
        if i[-3:] == ".py":
            y = importlib.import_module('modules.%s' % i[:-3])
            try:
                if inspect.isclass(y.Exploit):
                    modules.append(y)
            except (AttributeError, NameError):
                print("no module in file", i)

    for y in modules:
        k = y.Exploit()
        table = [[k.name, k.description]]
        print(tabulate(table))



    #: exploits: litebans sql dump, holographics dir traversal, log4j
    print("Logging in...")

    auth_token = authentication.AuthenticationToken()
    try:
        auth_token.authenticate(os.getenv("USERNAME"), os.getenv("PASSWORD"))
    except YggdrasilError as e:
        print(e)
        sys.exit()

    os.system('clear')
    print("Logged in as %s..." % auth_token.username)
    time.sleep(1)
    os.system('clear')


    #connection = Connection("ip here", 25565, auth_token=auth_token)


if __name__ == '__main__':
    main()
