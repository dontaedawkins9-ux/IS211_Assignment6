import unittest
import conversions


class TestTemperatureConversions(unittest.TestCase):

    def testCelsiusToKelvin(self):
        self.assertEqual(conversions.convertCelsiusToKelvin(0), 273.15)
        self.assertEqual(conversions.convertCelsiusToKelvin(100), 373.15)
        self.assertEqual(conversions.convertCelsiusToKelvin(-273.15), 0)


if __name__ == '__main__':
    unittest.main()
