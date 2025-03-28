import logging
import socket
import threading


class TCPServer:
    """
    Basic TCP server for localhost communication.

    Listens on a port, handles clients one by one (well, in threads), and yells back their messages in UPPERCASE.
    """

    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 5000,
        disconnect_command: str = "DESCONEXION",
    ):
        """
        Set up the server with some sensible defaults.

        Args:
            host (str): The address to bind to. Defaults to localhost.
            port (int): The port to listen on. Should not already be in use 🤞.
            disconnect_command (str): The secret word that makes clients go away.
        """
        self.host = host
        self.port = port
        self.disconnect_command = disconnect_command.upper()

        logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")
        self.logger = logging.getLogger("TCPServer")

    def start(self):
        """
        Start the server and wait for clients to connect.

        This method blocks forever — which is either great or terrible, depending on your life choices.
        Spawns a new thread per client so we don't just freeze after one conversation.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((self.host, self.port))
            server_socket.listen()
            self.logger.info(f"🚀 Server listening on {self.host}:{self.port}")

            while True:
                conn, addr = server_socket.accept()
                thread = threading.Thread(
                    target=self.handle_client, args=(conn, addr), daemon=True
                )
                thread.start()

    def handle_client(self, conn: socket.socket, addr: tuple):
        """
        Talk to a client. Respond in ALL CAPS, or say goodbye if they drop the magic word.

        Args:
            conn (socket.socket): The socket for the connected client.
            addr (tuple): The client's IP address and port. Hopefully not a bot.
        """
        self.logger.info(f"🔌 New connection from {addr}")
        with conn:
            while True:
                try:
                    data = conn.recv(1024)
                    if not data:
                        break

                    message = data.decode().strip()
                    self.logger.info(f"📩 Received from {addr}: {message}")

                    if message.upper() == self.disconnect_command:
                        self.logger.info(f"🔒 Disconnecting client {addr}")
                        break
                    else:
                        response = message.upper()
                        conn.sendall(response.encode())
                        self.logger.info(f"📤 Sent to {addr}: {response}")
                except ConnectionResetError:
                    self.logger.warning(f"⚠️ Connection reset by client {addr}")
                    break

        self.logger.info(f"❌ Connection with {addr} closed")


if __name__ == "__main__":
    server = TCPServer()
    server.start()
