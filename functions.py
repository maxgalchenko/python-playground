def celsius_to_fahrenheit(celsius: float) -> float:
    """Takes a temperature in Celsius and converts it to Fahrenheit.

    Args:
        celsius (float): temperature in celsius

    Returns:
        float: temperature in fahrenheit
    """
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Takes a temperature in Fahrenheit and converts it to Celsius.

    Args:
        fahrenheit (float): temperature in fahrenheit

    Returns:
        float: temperature in celsius
    """
    return (fahrenheit - 32) * 5 / 9


from typing import Literal


def convert_temperature(temperature: float, unit: Literal["F", "C"]) -> float:
    if unit == "F":
        return fahrenheit_to_celsius(temperature)
    else:
        return celsius_to_fahrenheit(temperature)


temperature_c = 25
temperature_f = 77

converted_f = convert_temperature(temperature_c, "C")
converted_c = convert_temperature(temperature_f, "F")

print(f"{temperature_c}°C is equal to {converted_f}°F")
print(f"{temperature_f}°F is equal to {converted_c}°C")
