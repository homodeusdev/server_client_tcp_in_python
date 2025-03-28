import logging
import socket


class TCPClient:
    """
    TCP Client that connects to the server and tries to have a meaningful (uppercase) conversation.

    Connects to localhost:5000 by default. Prompts the user for messages.
    Sends them to the server. Gets yelled back in UPPERCASE.
    """

    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 5000,
        disconnect_command: str = "DESCONEXION",
    ):
        """
        Initializes the TCPClient.

        Args:
            host (str): The server's address. Defaults to localhost because we're not THAT fancy.
            port (int): The port the server listens on. Default: 5000 (classic dev port).
            disconnect_command (str): Typing this ends the conversation.
            Like CTRL+C but polite.
        """
        self.host = host
        self.port = port
        self.disconnect_command = disconnect_command.upper()

        logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")
        self.logger = logging.getLogger("TCPClient")

    def run(self):
        """
        Starts the client, connects to the server,
        and loops until the user disconnects.

        It's a chat, not a rocket launch. Keep it simple.
        Prompt > Send > Receive > Repeat.
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((self.host, self.port))
                self.logger.info(f"📡 Connected to server at {self.host}:{self.port}")

                while True:
                    message = input("Enter a message: ").strip()

                    if not message:
                        print("Message can't be empty. Try again.")
                        continue

                    client_socket.sendall(message.encode())

                    if message.upper() == self.disconnect_command:
                        self.logger.info("👋 Disconnecting from server...")
                        break

                    response = client_socket.recv(1024).decode()
                    print(f"Server response: {response}")

        except ConnectionRefusedError:
            self.logger.error("🚫 Couldn't connect to server. Is it running?")
        except KeyboardInterrupt:
            self.logger.info("💥 Client closed manually (KeyboardInterrupt)")
        except Exception as e:
            self.logger.exception(f"🔥 Unexpected error: {e}")


if __name__ == "__main__":
    client = TCPClient()
    client.run()
