from app.fix_engine import FixMessageGenerator
from django.test import TestCase


class TestFixEngine(TestCase):

    def setUp(self):
        self.fix = FixMessageGenerator()

    def test_genOrderID(self):
        id = self.fix.genOrderID()
        assert id == 1
