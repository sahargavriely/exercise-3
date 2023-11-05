import socket


class Connection:
    def __init__(self, socket: socket.socket):
        self._socket = socket

    def __repr__(self):
        cls_name = self.__class__.__name__
        from_ip, from_port = self._socket.getsockname()
        to_ip, to_port = self._socket.getpeername()
        return f'<{cls_name} from {from_ip}:{from_port} to {to_ip}:{to_port}>'

    def send(self, data):
        self._socket.sendall(data)

    def receive(self, size):
        chunks = []
        while size > 0:
            chunk = self._socket.recv(size)
            if not chunk:
                raise RuntimeError('Incomplete data')
            chunks.append(chunk)
            size -= len(chunk)
        return b''.join(chunks)

    def close(self):
        self._socket.close()
