import socket
import threading

import pytest

from server.server import TCPServer


@pytest.fixture
def server():
    """Create a basic instance of the TCPServer (not running)."""
    return TCPServer()


def test_uppercase_response(server):
    """
    Test that a message sent to the server is converted to uppercase
    and returned to the client.
    """
    client_sock, server_sock = socket.socketpair()

    addr = ("127.0.0.1", 12345)

    thread = threading.Thread(target=server.handle_client, args=(server_sock, addr))
    thread.start()

    client_sock.sendall(b"hello test\n")
    response = client_sock.recv(1024).decode()

    assert response == "HELLO TEST"  # nosec B101

    client_sock.sendall(b"DESCONEXION\n")
    thread.join()

    client_sock.close()
