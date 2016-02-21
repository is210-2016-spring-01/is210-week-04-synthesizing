#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 1"""

import decimal


def fahrenheit_to_celsius(degrees):
    """Calculate degrees in celsius.

    Args:
        degrees(decimal): degress in fahrenheit.

    Returns:
        decimal: degrees converted from fahrenheit to celsius.

    Examples:

        >>> fahrenheit_to_celsius(212)
        'Decimal('100')'

        >>> fahrenheit_to_celsius(520)
        'Decimal('271')'
    """
    celsius = ((degrees - 32)*5/9)
    return decimal.Decimal(celsius)


ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def celsius_to_kelvin(degrees):
    """Calculate degrees in kelvin.

    Args:
        degrees (decimal): degrees in celsius.

    Returns:
        decimal: degrees converted from celsius to kelvin.

    Examples:

        >>> celsius_to_kelvin(100)
        'Decimal('373.15')'

        >>> celsius_to_kelvin(520)
        'Decimal('793.15')'
    """
    kelvin = degrees + ABSOLUTE_DIFFERENCE
    return decimal.Decimal(kelvin)


def fahrenheit_to_kelvin(degrees):
    """Calculate degrees in kelvin.

    Args:
        degrees (decimal): degrees in fahrenheit.

    Returns:
        decimal: degrees converted from fahrenheit to kelvin.

    Examples:

        >>> fahrenheit_to_kelvin(212)
        'Decimal('373.15')'

        >>> fahrenheit_to_kelvin(520)
        'Decimal('544.25')'
    """
    celsius = ((degrees - 32)*5/9)
    kelvin = celsius + ABSOLUTE_DIFFERENCE
    return decimal.Decimal(kelvin)
