from app.fix_engine import FixMessageGenerator
from django.test import TestCase
from app.fix_engine import FixMessageValidator


class TestFixEngine:

    fix_gen = FixMessageGenerator()
    fix_val = FixMessageValidator()

    def test_genOrderID(self):
        id = self.fix_gen.genOrderID()
        assert id == 1

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
