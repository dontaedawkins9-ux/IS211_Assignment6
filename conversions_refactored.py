class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):
    temperature_units = ['Celsius', 'Fahrenheit', 'Kelvin']
    distance_units = ['Miles', 'Yards', 'Meters']

    # Converting a unit to itself
    if fromUnit == toUnit:
        return float(value)

    # Do not allow temperature and distance conversions
    if ((fromUnit in temperature_units and toUnit in distance_units) or
            (fromUnit in distance_units and toUnit in temperature_units)):
        raise ConversionNotPossible(
            "Cannot convert from {} to {}".format(fromUnit, toUnit)
        )

    # Temperature conversions
    if fromUnit == 'Celsius':
        celsius = float(value)
    elif fromUnit == 'Fahrenheit':
        celsius = (float(value) - 32) * 5 / 9
    elif fromUnit == 'Kelvin':
        celsius = float(value) - 273.15
    else:
        celsius = None

    if celsius is not None:
        if toUnit == 'Celsius':
            return celsius
        elif toUnit == 'Fahrenheit':
            return (celsius * 9 / 5) + 32
        elif toUnit == 'Kelvin':
            return celsius + 273.15

    # Distance conversions
    if fromUnit == 'Miles':
        meters = float(value) * 1609.344
    elif fromUnit == 'Yards':
        meters = float(value) * 0.9144
    elif fromUnit == 'Meters':
        meters = float(value)
    else:
        meters = None

    if meters is not None:
        if toUnit == 'Miles':
            return meters / 1609.344
        elif toUnit == 'Yards':
            return meters / 0.9144
        elif toUnit == 'Meters':
            return meters

    raise ConversionNotPossible(
        "Cannot convert from {} to {}".format(fromUnit, toUnit)
    )
