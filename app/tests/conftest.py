import pytest

@pytest.fixture
def new_order_fix():
    return '8=FIX.4.4|9=117|35=D|34=1|52=20201118-05:27:11.398|60=20201118-05:27:11.398|49=SENDER|56=TARGET|112=TEST|11=1|55=AAPL|54=1|38=1|40=1|10=168'

@pytest.fixture
def new_cancel_fix():
    return '8=FIX.4.4|9=117|35=F|34=1|52=20201118-05:29:30.495|60=20201118-05:29:30.495|49=SENDER|56=TARGET|112=TEST|41=1|11=2|55=AAPL|54=1|38=1|10=174'

@pytest.fixture
def invalid_fix_message():
    return '8=FIX.4.4|9=117'

@pytest.fixture
def invalid_checksum_message():
    return '8=FIX.4.4|9=117|35=D|34=1|52=20201118-05:27:11.398|60=20201118-05:27:11.398|49=SENDER|56=TARGET|112=TEST|11=1|55=AAPL|54=1|38=1|40=1|10=000'

@pytest.fixture
def data_dict():
    return {'stock_symbol':'TEST',
            'quantity':1,
            'side':'Buy',
            'order_type':'Market'}

@pytest.fixture
def new_cancel_url_():
    return 'http://localhost:8000/fixmessage/?message_type=Order+Cancel+Request&stock_symbol=AAPL&quantity=1&side=Buy&order_type=Market'

@pytest.fixture
def new_order_url_():
    return 'http://localhost:8000/fixmessage/?message_type=New+Order+Single&stock_symbol=AAPL&quantity=1&side=Buy&order_type=Market'

@pytest.fixture
def api_serve_result_test_data():
    return {"message_type": "New Order Single",
                   "stock_symbol": "AAPL",
                   "quantity": 1,
                   "price": 123,
                   "side": "Buy",
                   "order_type": "Market"}
