import unittest
import conversions


class TestTemperatureConversions(unittest.TestCase):

    def testCelsiusToKelvin(self):
        test_cases = [
            (0.0, 273.15),
            (100.0, 373.15),
            (-273.15, 0.0),
            (300.0, 573.15),
            (-40.0, 233.15)
        ]

        for celsius, expected in test_cases:
            print("Testing Celsius to Kelvin:", celsius, "C")
            self.assertAlmostEqual(
                conversions.convertCelsiusToKelvin(celsius),
                expected,
                places=2
            )

    def testCelsiusToFahrenheit(self):
        test_cases = [
            (0.0, 32.0),
            (100.0, 212.0),
            (-40.0, -40.0),
            (300.0, 572.0),
            (-20.0, -4.0)
        ]

        for celsius, expected in test_cases:
            print("Testing Celsius to Fahrenheit:", celsius, "C")
            self.assertAlmostEqual(
                conversions.convertCelsiusToFahrenheit(celsius),
                expected,
                places=2
            )


if __name__ == '__main__':
    unittest.main()
