import simplefix
s = 'as'


class FixMessageGenerator():

    orderID = 0
    execID = 0
    msgSeqNum = 0

    def __init__(self):
        self.msg = simplefix.FixMessage()

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
        self.msg.append_time(52, header=True)
        return self.msg

    def create_new_order_single(self):
        self.msg = self.create_header()
        self.msg.append_pair(35, "D")
        return self.msg

m = FixMessageGenerator()
print(m.create_new_order_single())
p = FixMessageGenerator()
print(p.create_new_order_single(), p.create_new_order_single() )
