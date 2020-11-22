from app.fix_engine import FixMessageGenerator
from django.test import TestCase
from app.fix_engine import FixMessageValidator


class TestFixEngine:

    fix_gen = FixMessageGenerator()
    fix_val = FixMessageValidator()

    def test_genOrderID(self):
        id = self.fix_gen.genOrderID()
        assert id == 'FXID1'

    def test_tag35_in_cancel_message(self):
        missing, value_err = self.fix_val.validate_new_cancel_request('35=X')
        assert 'incorrect' in value_err[0]
        assert missing != []

    def test_tag35_in_new_message(self):
        missing, value_err = self.fix_val.validate_new_cancel_request('35=X')
        assert 'incorrect' in value_err[0]
        assert missing != []

    def test_validate_new_order_request_validation(self, new_order_fix):
        missing, val = self.fix_val.validate_new_order_request(new_order_fix)
        assert missing == []
        assert val == []

    def test_validate_new_cancel_request_validation(self, new_cancel_fix):
        missing, val = self.fix_val.validate_new_cancel_request(new_cancel_fix)
        assert missing == []
        assert val == []

    def test_validate_new_order_request_validation_invalid_data(self, invalid_fix_message):
        missing, val = self.fix_val.validate_new_order_request(invalid_fix_message)
        assert missing != []
        assert val != []

    def test_validate_new_cancel_request_validation_invalid_data(self, invalid_fix_message):
        missing, val = self.fix_val.validate_new_cancel_request(invalid_fix_message)
        assert missing != []
        assert val != []

    def test_validate_checksum_valid_data(self, new_order_fix):
        result = self.fix_val.isCheckSumValid(new_order_fix)
        assert result[0] == True

    def test_validate_checksum_invalid_data(self, invalid_checksum_message):
        result = self.fix_val.isCheckSumValid(invalid_checksum_message)
        assert result[0] == False

    def test_create_header(self):
        header = self.fix_gen.create_header()
        # import ipdb; ipdb.set_trace()
        assert header.begin_string == b'FIX.4.4'
        assert header.get(49) == b'SENDER'
        assert header.get(56) == b'TARGET'
        assert header.get(112) == b'TEST'
        assert header.get(34) == b'1'
        assert header.get(52) is not None

    def test_validate_new_order_creation(self, data_dict):
        message = self.fix_gen.create_new_order_single(data_dict)
        assert message.get(35) == b'D'
        assert message.get(11) == b'FXID2'
        assert message.get(55) == b'TEST'
        assert message.get(54) == b'1'
        assert message.get(38) == b'1'
        assert message.get(60) is not None
        assert message.get(40) == b'1'

    def test_validate_new_cancel_creation(self, data_dict):
        message = self.fix_gen.create_cancel_order_request(data_dict)
        # import ipdb; ipdb.set_trace()
        assert message.get(35) == b'F'
        assert message.get(41) == b'OriginalID'
        assert message.get(11) == b'FXID2'
        assert message.get(55) == b'TEST'
        assert message.get(54) == b'1'
        assert message.get(38) == b'1'
        assert message.get(60) is not None
