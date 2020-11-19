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
        self.msg.append_utc_timestamp(60, header=True)
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
        self.msg.append_pair(38, data['quantity'])
        self.mss = self.msg.encode()
        self.parsed_msg.append_buffer(self.mss)
        # import ipdb; ipdb.set_trace()
        return self.parsed_msg.get_message()

class FixMessageValidator():

    def get_tags_from_fix(self, fix_message):
        message_pairs = fix_message.split('|')

        tags = [pair.split('=') for pair in message_pairs]
        # import ipdb; ipdb.set_trace()
        message_pairs_dict = dict(tags)
        return message_pairs_dict

    def isCheckSumValid(self, fix_message):
        fix_until_tail = fix_message.split('10=')[0] #to remove tag 10
        checksum_val = fix_message.split('=')[-1]
        bytes_fix = bytes(fix_until_tail, 'ascii')
        bytes_values = [val if val != 124 else 1 for val in bytes_fix]
        actual_checksum_val = str(sum(bytes_values) % 256)
        # import ipdb; ipdb.set_trace()
        return actual_checksum_val == checksum_val, actual_checksum_val, checksum_val

    def validate_new_cancel_request(self, fix_message):
        missing_pairs = []
        value_errors = []
        tags = self.get_tags_from_fix(fix_message)
        checksum_val = self.isCheckSumValid(fix_message)
        if checksum_val[0] == False:
            value_errors.append('{} is incorrect value for tag 10 (CheckSum). Expected value is {}'.format(
                checksum_val[2], checksum_val[1]
            ))
        if tags.get('35') != 'F':
            value_errors.append('{} is incorrect value for tag 35 (MsgType)'.format(tags.get('35')))
        # import ipdb; ipdb.set_trace()
        for tag_value in new_cancel_request.items():
            if str(tag_value[1]) not in tags.keys():
                missing_pairs.append(tag_value)
        return missing_pairs, value_errors

    def validate_new_order_request(self, fix_message):
        missing_pairs = []
        value_errors = []
        tags = self.get_tags_from_fix(fix_message)
        # import ipdb; ipdb.set_trace()
        if tags.get('35') != 'D':
            value_errors.append('{} is incorrect value for tag 35 (MsgType)'.format(tags.get('35')))
        for tag_value in new_order_single.items():
            if str(tag_value[1]) not in tags.keys():
                missing_pairs.append(tag_value)
        return missing_pairs, value_errors
