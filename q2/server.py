import pathlib
import socket
import struct
import threading

from cli import CommandLineInterface
from connection import Connection
from listener import Listener
from thought import Thought


cli = CommandLineInterface()


@cli.command
def run(address, data):
    if isinstance(address, str):
        ip, port = address.split(':')
    data_dir = pathlib.Path(data)
    listener = Listener(int(port), ip)
    listener.start()
    while True:
        try:
            connection = listener.accept()
            thread = threading.Thread(
                target = _handle_connection,
                args = (connection, data_dir),
                daemon = True
            )
            thread.start()
        except socket.timeout:
            continue


def _handle_connection(connection: Connection, data_dir):
    headers = connection.receive(Thought.header_size)
    _, _, size = struct.unpack(Thought.header_format, headers)
    data = connection.receive(size)
    thought = Thought.deserialize(headers + data)
    _handle_thought(data_dir, thought)
    connection. close()


def _handle_thought(data_dir: pathlib.Path, thought: Thought):
    timestamp = thought.file_formatted_timestamp
    dir_path = data_dir / thought.user_id
    dir_path.mkdir(parents=True, exist_ok=True)
    file_path = dir_path / f'{timestamp}.txt'
    if file_path.exists():
        thought = f'\n{thought.thought}'
    with file_path.open('a') as file:
        file.write(thought.thought)


if __name__ == '__main__':
    cli.main()
