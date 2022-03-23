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

load_dotenv()


class Exploit:
    """Exploit schema"""
    def __init__(self, client: Connection):
        self.name = "Exploit name here"
        self.description = "exploit description here",
        self.client = client

    def execute(self) -> tuple[bool, str]:
        return True, "Success in Message"


def main():
    auth_token = authentication.AuthenticationToken()
    try:
        auth_token.authenticate(os.getenv("USERNAME"), os.getenv("PASSWORD"))
    except YggdrasilError as e:
        print(e)
        sys.exit()
    print("Logged in as %s..." % auth_token.username)
    connection = Connection(
        "ip here", 25565, auth_token=auth_token)


if __name__ == '__main__':
    main()
