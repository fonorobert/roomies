import unittest
from roomies import Balance


class TestRoomies(unittest.TestCase):

    def setUp(self):
        self.expenses = []
        self.expenses.append({"payer": "John", "owner": "Jill", "amount": 300})
        self.expenses.append({"payer": "Jill", "owner": "", "amount": 120})
        self.expenses.append({"payer": "John", "owner": "Joe", "amount": 900})

    def test_listing(self):
        b = Balance(self.expenses)
        exp_list = ["John", "Jill", "Joe"]
        self.assertCountEqual(b._list_ppl(self.expenses), exp_list)

    def test_balance_basic(self):
        b = Balance(self.expenses)
        exp_balace = {"John": 1160, "Jill": -260, "Joe": -940}
        self.assertEqual(b.getbalance(), exp_balace)

    def test_balance_invalid_input(self):
        expenses = self.expenses
        expenses.append({"payer": "", "owner": "Jill", "amount": 200})
        expenses.append({"payer": "John", "owner": "Jill", "amount": 0})
        expenses.append({"payer": "Jill", "owner": "John", "amount": "300"})

        b = Balance(expenses)
        exp_balace = {"John": 1160, "Jill": -260, "Joe": -940}
        #self.assertRaises(TypeError, b.getbalance)
        self.assertEqual(b.getbalance(), exp_balace)


if __name__ == '__main__':
    unittest.main()
