from django.test import TestCase

from .dataTypeConversion import binaryConversion

class TestSmartObjectCase(TestCase):
    def test_binary_conversion(self):
        self.assertEqual(binaryConversion(1, "boolean"), b'\x01')
        self.assertEqual(binaryConversion(0, "boolean"), b'\x00')

        self.assertEqual(binaryConversion('0', "boolean"), b'\x00')
        self.assertEqual(binaryConversion('', "boolean"), b'\x00')
        self.assertEqual(binaryConversion([], "boolean"), b'\x00')
        self.assertEqual(binaryConversion({}, "boolean"), b'\x00')

        self.assertEqual(binaryConversion('asdfgag', "boolean"), b'\x01')

