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
    def testFahrenheitToCelsius(self):
        test_cases = [
            (32.0, 0.0),
            (212.0, 100.0),
            (-40.0, -40.0),
            (572.0, 300.0),
            (-4.0, -20.0)
        ]

        for fahrenheit, expected in test_cases:
            print("Testing Fahrenheit to Celsius:", fahrenheit, "F")
            self.assertAlmostEqual(
                conversions.convertFahrenheitToCelsius(fahrenheit),
                expected,
                places=2
            )
            
    def testFahrenheitToKelvin(self):
        test_cases = [
            (32.0, 273.15),
            (212.0, 373.15),
            (-40.0, 233.15),
            (572.0, 573.15),
            (-4.0, 253.15)
        ]

        for fahrenheit, expected in test_cases:
            print("Testing Fahrenheit to Kelvin:", fahrenheit, "F")
            self.assertAlmostEqual(
                conversions.convertFahrenheitToKelvin(fahrenheit),
                expected,
                places=2
            )

    def testKelvinToFahrenheit(self):
        test_cases = [
            (273.15, 32.0),
            (373.15, 212.0),
            (233.15, -40.0),
            (573.15, 572.0),
            (253.15, -4.0)
        ]

        for kelvin, expected in test_cases:
            print("Testing Kelvin to Fahrenheit:", kelvin, "K")
            self.assertAlmostEqual(
                conversions.convertKelvinToFahrenheit(kelvin),
                expected,
                places=2
            )

    def testKelvinToCelsius(self):
        test_cases = [
            (273.15, 0.0),
            (373.15, 100.0),
            (233.15, -40.0),
            (573.15, 300.0),
            (253.15, -20.0)
        ]

        for kelvin, expected in test_cases:
            print("Testing Kelvin to Celsius:", kelvin, "K")
            self.assertAlmostEqual(
                conversions.convertKelvinToCelsius(kelvin),
                expected,
                places=2
            )


if __name__ == '__main__':
    unittest.main()
