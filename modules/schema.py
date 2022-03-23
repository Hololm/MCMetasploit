from minecraft.networking.connection import Connection


class Exploit:
    """Exploit schema"""
    def __init__(self, client: Connection):
        self.name = "Exploit name here"
        self.description = "exploit description here",
        self.client = client

    def execute(self) -> tuple[bool, str]:
        return True, "Success in Message"
