import unittest
from unittest.mock import patch
import io
import employee_tracker

class TestEmployeeTracker(unittest.TestCase):

    @patch('employee_tracker.input', side_effect=['1', 'John Doe', 'menu'])
    @patch('employee_tracker.print')
    def test_manipulate_string_uppercase(self, mock_print, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            employee_tracker.manipulate_string()
            output = fake_out.getvalue().strip()
        self.assertIn('JOHN DOE', output)

    @patch('employee_tracker.input', side_effect=['2', 'John Doe', 'menu'])
    @patch('employee_tracker.print')
    def test_manipulate_string_lowercase(self, mock_print, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            employee_tracker.manipulate_string()
            output = fake_out.getvalue().strip()
        self.assertIn('john doe', output)

    @patch('employee_tracker.input', side_effect=['3', 'john doe', 'menu'])
    @patch('employee_tracker.print')
    def test_manipulate_string_capitalize(self, mock_print, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            employee_tracker.manipulate_string()
            output = fake_out.getvalue().strip()
        self.assertIn('John doe', output)

    @patch('employee_tracker.input', side_effect=['4', 'john doe', 'john', 'johnny', 'menu'])
    @patch('employee_tracker.print')
    def test_manipulate_string_replace(self, mock_print, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            employee_tracker.manipulate_string()
            output = fake_out.getvalue().strip()
        self.assertIn('johnny doe', output)

    @patch('employee_tracker.input', side_effect=['5'])
    @patch('employee_tracker.print')
    def test_manipulate_string_return_to_menu(self, mock_print, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            employee_tracker.manipulate_string()
            output = fake_out.getvalue().strip()
        self.assertNotIn('JOHN DOE', output)  # Ensure it returns to menu

    @patch('employee_tracker.save_data')
    @patch('employee_tracker.input', side_effect=['34', 'emp1', 'John Doe', '8', '8', '8', '8', '8', 'menu'])
    def test_add_employee(self, mock_input, mock_save_data):
        data = {}
        employee_tracker.add_employee(data)
        self.assertIn('emp1', data)
        self.assertEqual(data['emp1']['name'], 'John Doe')
        self.assertEqual(data['emp1']['week'], '34')
        self.assertEqual(data['emp1']['hours'], [8.0, 8.0, 8.0, 8.0, 8.0])
        mock_save_data.assert_called_once_with(data)

    @patch('employee_tracker.load_data', return_value={'emp1': {'name': 'John Doe', 'week': 34, 'hours': [8, 8, 7, 8, 6]}})
    @patch('employee_tracker.print')
    def test_read_employees(self, mock_print, mock_load_data):
        employee_tracker.read_employees({})
        mock_print.assert_called()  # Ensure print was called

    @patch('employee_tracker.save_to_csv')
    @patch('employee_tracker.print')
    def test_save_to_csv(self, mock_print, mock_save_to_csv):
        data = {'emp1': {'name': 'John Doe', 'week': 34, 'hours': [8, 8, 7, 8, 6]}}
        employee_tracker.save_to_csv(data)
        mock_save_to_csv.assert_called_once_with(data)
        mock_print.assert_called()  # Ensure print was called

    @patch('employee_tracker.load_data', return_value={'emp1': {'name': 'John Doe', 'week': 34, 'hours': [8, 8, 7, 8, 6]}})
    @patch('employee_tracker.print')
    def test_generate_weekly_report(self, mock_print, mock_load_data):
        employee_tracker.generate_weekly_report({})
        mock_print.assert_called()  # Ensure print was called

if __name__ == '__main__':
    unittest.main()
