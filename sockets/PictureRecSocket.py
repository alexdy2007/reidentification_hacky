import socket
import pickle
import numpy as np
import atexit

class SocketClient(object):
    def __init__(self):
        #host = '192.168.0.48'
        host = '10.42.0.192'
        port = 5560
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.connect((host, port))


    def get_picture(self):

        self.soc.sendall(str.encode("length"))
        pic_length = self.soc.recv(1024)
        pic_length = int(pic_length.decode("utf-8"))
        self.soc.sendall(str.encode("picture"))
        picture = self._recvall(self.soc,pic_length)
        picture_array = pickle.loads(picture)
        return picture_array

    def kill_server(self):
        self.soc.send(str.encode("kill"))

    def exit_server(self):
        self.soc.send(str.encode("exit"))


    def listen_for_pictures(self, conn):
        while True:
            with conn:
                length = self._recvall(conn, 16)
                pic_data = self._recvall(conn, int(length))
                print(pic_data[1:10])


    def _recvall(self, soc, count):

        buf = b''
        while count:
            newbuf = soc.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    def __del__(self):
        self.kill_socket()

    def kill_socket(self):
        self.soc.close()

if __name__ == "__main__":
    ss = SocketClient()
    ss.get_picture()
    ss.exit_server()
