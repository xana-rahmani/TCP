from segment import Segment
import threading
import socket
import pickle


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('localhost', 8002))

while True:
    # Wait for a connection
    print "\n ----------- listen server"
    segment, address = serverSocket.recvfrom(1024)
    segment = pickle.loads(segment)
    closeConnection = False
    print segment.source_port, address

    if segment.SYN == 'b1':
        res_seq = Segment(source_port=address[1], ACK='b1', SYN='b1', FIN='b0')
    elif segment.FIN == 'b1':
        res_seq = Segment(source_port=address[1], ACK='b1', SYN='b0', FIN='b0')
        res_seq = pickle.dumps(res_seq)
        serverSocket.sendto(res_seq, address)
        res_seq = Segment(source_port=address[1], ACK='b0', SYN='b0', FIN='b1')
    else:
        res_seq = Segment(source_port=address[1], ACK='b0', SYN='b0', FIN='b0')

    print "SYN: ", res_seq.SYN, "\tACK: ", res_seq.ACK
    res_seq = pickle.dumps(res_seq)
    serverSocket.sendto(res_seq, address)
