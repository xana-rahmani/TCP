from segment import Segment
import threading
import socket
import time
import pickle


class Client:
    """ client class """

    def __init__(self, ip, port):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.clientSocket.bind(('', 0))
        self.client_ip = self.clientSocket.getsockname()[0]
        self.client_port = self.clientSocket.getsockname()[1]
        self.destination_port = port
        self.destination_ip = ip
        self.establishConnection = False
        self.closingConnection = False
        self.sample = 0
        self.estimatedRTT = 1
        self.devRTT = 0

    def sendSeqment(self, seq):
        """ Send Seqment and check timeout """
        seq = pickle.dumps(seq)

        self.clientSocket.sendto(seq, (self.destination_ip, self.destination_port))
        start = time.time()
        res_seq, server = self.clientSocket.recvfrom(1024)
        end = time.time()

        res_seq = pickle.loads(res_seq)
        print '.......... time: ', end - start, "\n",
        return res_seq

    def handshake(self):
        while True:
            seq = Segment(source_port=self.client_port, SYN='b1', ACK='b1')
            res_seq = self.sendSeqment(seq)
            if res_seq.SYN == 'b1' and res_seq.ACK == 'b1':
                print 'send ACK for SYN'
                seq = Segment(source_port=self.client_port, SYN='b0', ACK='b1')
                self.sendSeqment(seq)
                self.establishConnection = True
                return
            else:
                continue

    def closingConnection(self):
        pass

    def setTimeOut(self):
        self.estimatedRTT = (0.875 * self.estimatedRTT) + (0.125 * self.sample)
        self.devRTT = (0.75 * self.devRTT) + (0.25 * (self.sample - self.estimatedRTT))
        timeout = self.estimatedRTT + 4 * self.devRTT
        return timeout

    def startConnection(self):
        while True:
            if not self.establishConnection:
                self.handshake()
            print "_______Agreeing to establish a connection_______"
            a = raw_input("_______stop______")


c = Client('localhost', 8002)
c.startConnection()
