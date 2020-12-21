side = {
    'Buy':1,
    'Sell':2,
}

order_type = {
    'Market':1,
    'Limit':2,
    'Stop':3,
    'Stop limit': 4,
}

header = {
    'BeginString':8,
    'BodyLength':9,
    'MsgType':35,
    'SenderCompID': 49,
    'TargetCompID': 56,
    'MsgSeqNum': 34,
    'SendingTime': 52,
    'TestReqID':112
}

footer = {
    'CheckSum':10
}

new_order_single = {
    'Symbol': 55,
    'Side': 54,
    'ClOrdID': 11,
    'TransactTime': 60,
    'OrderQty': 38,
    'OrderType': 40
}
new_order_single.update(header)
new_order_single.update(footer)

"""Cancel request"""
new_cancel_request = {
    'OrigClOrdID': 41,
    'ClOrdID': 11,
    'Symbol': 55,
    'Side': 54,
    'TransactTime': 60,
    'OrderQty': 38,
}

new_cancel_request.update(header)
new_cancel_request.update(footer)
