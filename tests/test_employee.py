import unittest
from unittest.mock import patch

from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
    #

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Neha', 'Pandey', 50000)
        self.emp_2 = Employee('abc', 'xyz', 60000)

    def tearDown(self):
        print('tearDown\n')
        pass

    def test_email(self):
        print('test_email\n')
        # self.emp_1 = Employee('Neha', 'Pandey', 50000)
        # self.emp_2 = Employee('abc', 'xyz', 60000)

        self.assertEqual(self.emp_1.email(), 'Neha.Pandey@email.com')
        self.assertEqual(self.emp_2.email(), 'abc.xyz@email.com')

        self.emp_1.first = 'aaa'
        self.emp_2.first = 'bbb'

        self.assertEqual(self.emp_1.email(), 'aaa.Pandey@email.com')
        self.assertEqual(self.emp_2.email(), 'bbb.xyz@email.com')

    def test_fullname(self):
        print('test_fullname\n')
        # self.emp_1 = Employee('Neha', 'Pandey', 50000)
        # self.emp_2 = Employee('abc', 'xyz', 60000)

        self.assertEqual(self.emp_1.fullname(), 'Neha Pandey')
        self.assertEqual(self.emp_2.fullname(), 'abc xyz')

        self.emp_1.first = 'aaa'
        self.emp_2.first = 'bbb'

        self.assertEqual(self.emp_1.fullname(), 'aaa Pandey')
        self.assertEqual(self.emp_2.fullname(), 'bbb xyz')

    def test_apply_raise(self):
        print('test_apply_raise\n')
        # self.emp_1 = Employee('Neha', 'Pandey', 50000)
        # self.emp_2 = Employee('abc', 'xyz', 60000)

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://verisk.com/Pandey/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://verisk.com/xyz/June')
            self.assertEqual(schedule, 'Bad Response!')



    @patch('employee.Employee.email')
    @patch('employee.Employee.fullname')
    def test_employee_detail(self, mock_fullname, mock_email):
        mock_fullname.return_value = 'Verisk Analytics'
        mock_email.return_value = 'xyz@email.com'
        expected_result = {
            "fullname": mock_fullname.return_value,
            "email": mock_email.return_value
        }
        actual_result = self.emp_1.employee_detail()
        self.assertEqual(actual_result, expected_result)



if __name__ == '__main__':
    unittest.main()

