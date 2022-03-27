from minecraft.networking.connection import Connection
from minecraft.networking.packets import Packet
import minecraft.networking.packets


class BaseExploit:
    """Exploit schema"""
    def __init__(self, client: Connection = None):
        self.name = "Default Exploit"
        self.description = "Default Description",
        self.client = client
        self.joined = False

        if self.client:
            self.client.register_packet_listener(
                self.onJoin, minecraft.networking.packets.JoinGamePacket)  #: sends join game packet to server

            self.client.register_packet_listener(
                self.onLeave, minecraft.networking.packets.DisconnectPacket)  #: sends disconnect packet

    def addEvent(self, function, event: Packet):
        self.client.register_packet_listener(function, event)

    def onJoin(self, packet: minecraft.networking.packets.JoinGamePacket):  #: sends join game packet to server
        print('Connected to server. Gamemode: {}'.format(packet.game_mode))
        self.joined = True

    @staticmethod
    def onLeave(packet):
        print('Left:', packet)

    """def execute(self) -> tuple[bool, str]:
        return True, "Success in Message"""
