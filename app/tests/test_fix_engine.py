from app.fix_engine import FixMessageGenerator
from django.test import TestCase
from app.fix_engine import FixMessageValidator


class TestFixEngine(TestCase):

    def setUp(self):
        self.fix_gen = FixMessageGenerator()
        self.fix_val = FixMessageValidator()

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
