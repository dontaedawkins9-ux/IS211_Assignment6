
def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = celsius + 273.15
    
    return kelvins


def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = (celsius * 9 / 5) + 32
    
    return fahrenheit

def convertFahrenheitToCelsius(fahrenheit):
    """Takes in a Fahrenheit measurement and returns Celsius"""
    celsius = (fahrenheit - 32) * 5 / 9

    return celsius


def convertFahrenheitToKelvin(fahrenheit):
    """Takes in a Fahrenheit measurement and returns Kelvin"""
    kelvins = (fahrenheit - 32) * 5 / 9 + 273.15

    return kelvins


def convertKelvinToFahrenheit(kelvin):
    """Takes in a Kelvin measurement and returns Fahrenheit"""
    fahrenheit = (kelvin - 273.15) * 9 / 5 + 32

    return fahrenheit


def convertKelvinToCelsius(kelvin):
    """Takes in a Kelvin measurement and returns Celsius"""
    celsius = kelvin - 273.15

    return celsius
