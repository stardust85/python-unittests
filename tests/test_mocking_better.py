import unittest
from unittest.mock import Mock

import requests_mock

from app.mocking_better import CurrencyConvertor


class TestCurrency(unittest.TestCase):
    def test_get_exchange_rate_without_mocking(self):
        """
        Actually NOT a unit test but rather a system test (connecting to external third party service)
        """
        convertor = CurrencyConvertor()
        result = convertor.get_exchange_rate('EUR', 'CZK')
        self.assertIsInstance(result, float)

    def tet_get_exchange_rate_with_mocking(self):
        """
        Mocked version of previous test
        """
        mocked_response = """
                {
                    "base":"EUR",
                    "date":"2018-06-27",
                    "rates":{
                        "AUD":1.5725,
                        "BGN":1.9558,
                        "BRL":4.4152,
                        "CAD":1.5443,
                        "CHF":1.1536,
                        "CNY":7.6649,
                        "CZK":25.777
                    }
                }
                """

        convertor = CurrencyConvertor()

        with requests_mock.mock() as m:
            m.get('https://exchangeratesapi.io/api/latest?base=EUR', text=mocked_response)
            result = convertor.convert_currency('EUR', 'CZK', 100)

        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, 25.777)

    def test_convert_currency__mocking(self):
        convertor = CurrencyConvertor()
        convertor.get_exchange_rate = Mock(return_value=25.777)
        result = convertor.convert_currency('EUR', 'CZK', 100)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, 2577.7)