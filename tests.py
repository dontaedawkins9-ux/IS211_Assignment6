import unittest
import conversions
import conversions_refactored

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
        def testRefactoredTemperatureConversions(self):
        test_cases = [
            ('Celsius', 'Fahrenheit', 0.0, 32.0),
            ('Celsius', 'Kelvin', 100.0, 373.15),
            ('Fahrenheit', 'Celsius', 212.0, 100.0),
            ('Fahrenheit', 'Kelvin', 32.0, 273.15),
            ('Kelvin', 'Celsius', 273.15, 0.0),
            ('Kelvin', 'Fahrenheit', 373.15, 212.0)
        ]

        for fromUnit, toUnit, value, expected in test_cases:
            print("Testing", fromUnit, "to", toUnit)
            self.assertAlmostEqual(
                conversions_refactored.convert(fromUnit, toUnit, value),
                expected,
                places=2
            )

    def testRefactoredDistanceConversions(self):
        test_cases = [
            ('Miles', 'Yards', 1.0, 1760.0),
            ('Miles', 'Meters', 1.0, 1609.344),
            ('Yards', 'Miles', 1760.0, 1.0),
            ('Yards', 'Meters', 1.0, 0.9144),
            ('Meters', 'Miles', 1609.344, 1.0),
            ('Meters', 'Yards', 0.9144, 1.0)
        ]

        for fromUnit, toUnit, value, expected in test_cases:
            print("Testing", fromUnit, "to", toUnit)
            self.assertAlmostEqual(
                conversions_refactored.convert(fromUnit, toUnit, value),
                expected,
                places=4
            )

    def testSameUnitConversions(self):
        units = [
            'Celsius',
            'Fahrenheit',
            'Kelvin',
            'Miles',
            'Yards',
            'Meters'
        ]

        for unit in units:
            print("Testing same unit conversion:", unit)
            self.assertEqual(
                conversions_refactored.convert(unit, unit, 100.0),
                100.0
            )

    def testIncompatibleConversions(self):
        print("Testing incompatible conversion")
        with self.assertRaises(
                conversions_refactored.ConversionNotPossible):
            conversions_refactored.convert(
                'Celsius',
                'Meters',
                100.0
            )

if __name__ == '__main__':
    unittest.main()
