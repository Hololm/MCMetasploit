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


def main():
  print("Hello user, enter your username below")
    """auth_token = authentication.AuthenticationToken()
    try:
        auth_token.authenticate(os.getenv("USERNAME"), os.getenv("PASSWORD"))
    except YggdrasilError as e:
        print(e)
        sys.exit()
    print("Logged in as %s..." % auth_token.username)
    connection = Connection(
        "ip here", 25565, auth_token=auth_token)"""
  print("exploit choices are-")
  input == str("which would you like to use")
  if input == "":
    print("")
  elif input == "":
    print("")
  elif input == "":
    print("")
  else:
    print("input invalid")

if __name__ == '__main__':
    main()
