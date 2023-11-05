import datetime as dt
import socket

from cli import CommandLineInterface
from connection import Connection
from thought import Thought


cli = CommandLineInterface()


@cli.command
def upload(address, user, thought):
    if isinstance(address, str):
        ip, port = address.split(':')
        address = ip, int(port)
    sock = socket.socket()
    sock.connect(address)
    connection = Connection(sock)
    thought = Thought(int(user), dt.datetime.now(), thought)
    connection.send(thought.serialize())
    connection.close()
    print('done')


if __name__ == '__main__':
    cli.main()
