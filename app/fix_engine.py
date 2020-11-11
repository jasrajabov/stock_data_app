import simplefix
from app.fix_mapping import *


class FixMessageGenerator():

    orderID = 0
    execID = 0
    msgSeqNum = 0

    def __init__(self):
        self.msg = simplefix.FixMessage()
        self.parsed_msg = simplefix.FixParser()

    def genOrderID(self):
    	self.orderID = self.orderID+1
    	return self.orderID

    def genExecID(self):
    	self.execID = self.execID+1
    	return self.execID

    def genMsgSeqNum(self):
        self.msgSeqNum = self.msgSeqNum+1
        return self.msgSeqNum

    def create_header(self):
        self.msg.append_pair(8, "FIX.4.4")
        self.msg.append_pair(49, "SENDER")
        self.msg.append_pair(56, "TARGET")
        self.msg.append_pair(112, "TEST")
        self.msg.append_pair(34, self.genMsgSeqNum(), header=True)
        self.msg.append_utc_timestamp(52, header=True)
        return self.msg

    def create_new_order_single(self, data):
        # import ipdb; ipdb.set_trace()
        self.msg = self.create_header()
        self.msg.append_pair(35, "D")
        self.msg.append_pair(11, self.genOrderID())
        self.msg.append_pair(55, data['stock_symbol'])
        self.msg.append_pair(54, side.get(data['side']))
        self.msg.append_pair(38, data['quantity'])
        self.msg.append_pair(40, order_type.get(data['order_type']))
        self.mss = self.msg.encode()
        self.parsed_msg.append_buffer(self.mss)
        return self.parsed_msg.get_message()

    def create_cancel_order_request(self, data):
        self.msg = self.create_header()
        self.msg.append_pair(35, "F")
        self.msg.append_pair(41, self.genOrderID())
        self.msg.append_pair(11, self.genOrderID())
        self.msg.append_pair(55, data['stock_symbol'])
        self.msg.append_pair(54, side.get(data['side']))
        self.msg.append_utc_timestamp(60, header=True)
        self.mss = self.msg.encode()
        self.parsed_msg.append_buffer(self.mss)
        return self.parsed_msg.get_message()

class FixMessageValidator():

    def get_tags_from_fix(self, fix_message):
        message_pairs = fix_message.split('|')
        tags = [pair.split('=')[0] for pair in message_pairs]
        return tags

    def validate_new_cancel_request(self, fix_message):
        missing_pairs = []
        tags = self.get_tags_from_fix(fix_message)
        for tag_value in new_cancel_request.items():
            if str(tag_value[1]) not in tags:
                missing_pairs.append(tag_value)
        return missing_pairs
