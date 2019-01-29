from django.test import TestCase
from object_collector.models import Operator

from .operatorUtils import compare

class TestSmartObjectCase(TestCase):

    def test_comparator_number_equal(self):
        equal_operator = Operator.objects.get(name="EQUAL")
        self.assertEqual(compare(equal_operator.name, 5, 5), True)
        self.assertEqual(compare(equal_operator.name, 5, 4.9), False)
        self.assertEqual(compare(equal_operator.name, 4, 4.9), False)


    def test_comparator_number_lte(self):
        less_than_equal_operator = Operator.objects.get(name="LTE")
        self.assertEqual(compare(less_than_equal_operator.name, 5, 5), True)
        self.assertEqual(compare(less_than_equal_operator.name, 6, 5), False)
        self.assertEqual(compare(less_than_equal_operator.name, 5, 8), True)

    def test_comparator_number_gte(self):
        greater_than_equal_operator = Operator.objects.get(name="GTE")
        self.assertEqual(compare(greater_than_equal_operator.name, 5, 5), True)
        self.assertEqual(compare(greater_than_equal_operator.name, 6, 5), True)
        self.assertEqual(compare(greater_than_equal_operator.name, 5, 8), False)


