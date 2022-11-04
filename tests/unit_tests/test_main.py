import unittest
from src.services.print_service import Printer

from mock import Mock


class TestMain(unittest.TestCase):
    def test_print_func_returns_value(self):
        # arrange
        mock_str = str(Mock)
        printer = Printer(True)

        # act
        ret_val = printer.print_func(mock_str)

        # assert
        self.assertEqual(mock_str, ret_val)
