from app.fix_mapping import *


class TestMappings:

    def test_side_mappings(self):
        assert side == {
            'Buy':1,
            'Sell':2,
        }

    def test_order_type_mappings(self):
        assert order_type == {
            'Market':1,
            'Limit':2,
            'Stop':3,
            'Stop limit': 4,
        }

    def test_new_order_single_mappings(self):
        assert new_order_single == {
            'Symbol': 55,
            'Side': 54,
            'TransactTime': 60,
            'OrderQty': 38,
            'ClOrdID': 11,
            'OrderType': 40,
            'BeginString':8,
            'BodyLength':9,
            'MsgType':35,
            'SenderCompID': 49,
            'TargetCompID': 56,
            'MsgSeqNum': 34,
            'SendingTime': 52,
            'CheckSum': 10,
            'TestReqID': 112
        }

    def test_new_cancel_single_mappings(self):
        assert new_cancel_request == {

            'OrigClOrdID': 41,
            'ClOrdID': 11,
            'Symbol': 55,
            'Side': 54,
            'TransactTime': 60,
            'OrderQty': 38,
            'BeginString':8,
            'BodyLength':9,
            'MsgType':35,
            'SenderCompID': 49,
            'TargetCompID': 56,
            'MsgSeqNum': 34,
            'SendingTime': 52,
            'CheckSum': 10,
            'TestReqID': 112
        }
