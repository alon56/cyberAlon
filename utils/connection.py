from __future__ import annotations

import socket


class Connection:
    def __init__(self, sock: socket.socket, recv_buf: int = 4096, timeout: float = 10.0):
        self._sock = sock
        self.recv_buf = recv_buf
        self._sock.settimeout(timeout)


    def recv(self) -> bytes:
        return self._sock.recv(self.recv_buf)


    def send(self, data: bytes):
        self._sock.sendall(data)


    def close(self):
        try:
            self._sock.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        finally:
            self._sock.close()


    def __enter__(self) -> Connection:
        return self


    def __exit__(self):
        self.close()
