import unittest
from roomies import Balance

class TestRoomies(unittest.TestCase):

    def setUp(self):
        self.expenses = [{"payer": "John", "owner": "Jill", "amount": 300}, {"payer": "Jill", "owner": "", "amount": 130}]
        self.expenses.append({"payer": "John", "owner": "Joe", "amount": 900})
        self.b = Balance(self.expenses)

    def test_listing(self):
        b = self.b
        self.assertEqual(b._list_ppl(self.expenses), ["John", "Jill", "Joe"])


if __name__ == '__main__':
    unittest.main()