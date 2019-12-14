import numpy as np


class Segment:
    """ p
    acket structure """
    def __init__(self, source_port, ACK, SYN, FIN='b0'):
        self.source_port = source_port
        # self.destination_port = destination_port
        # self.sequence_number = sequence_number
        # self.ACK_number = ACK_number
        # self.header_length = header_length
        # self.reservd = reserved
        # self.URG = URG
        self.ACK = ACK
        # self.PSH = PSH
        # self.PST = PST
        self.SYN = SYN
        self.FIN = FIN
        # self.window = window
        # self.check_sum = check_sum
        # self.urgent_pointer = urgent_pointer
        # self.option = option
        # self.data = data

# , destination_port, sequence_number, ACK_number, header_length, reserved,
#                  URG, ACK, PSH, PST, SYN, FIN, window, check_sum, urgent_pointer, option, data
