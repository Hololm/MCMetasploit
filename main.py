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


load_dotenv()


def main():
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

    #: do loading and formatting here

    #connection = Connection("ip here", 25565, auth_token=auth_token)


if __name__ == '__main__':
    main()
