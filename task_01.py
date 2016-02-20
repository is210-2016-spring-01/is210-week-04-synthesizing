#!usr/bin/env/python
# -*- coding: utf-8 -*-
"""Converting a temperatures."""


import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """Coverting a Fahrenheit temperature to Celsius.

    Args:
        degrees (mixed): Arg to be converted.

    Returns:
        decimal: Argument in Celsius.

    Examples:

        >>>fahrenheit_to_celsius(212)
        Decimal('100')

        >>>fahrenheit_to_celsius(95)
        Decimal('35')

        >>>fahrenheit_to_celsius(-10)
        Decimal('-23.33333333333333333333333333')
    """
    return ((decimal.Decimal(degrees) - 32) * 5) /9


def celsius_to_kelvin(degrees):
    """Converting Celsius to Kelvin.

    Args:
        degrees (mixed): Arg to be converted.

    Returns:
        decimal: Argument in Kelvin.

    Examples:

        >>>celsius_to_kelvin(100)
        Decimal('373.15')

        >>>celsius_to_kelvin(50)
        Decimal('323.15')

        >>>celsius_to_kelvin(-15)
        Decimal('258.15')
    """
    return decimal.Decimal(degrees) + ABSOLUTE_DIFFERENCE


def fahrenheit_to_kelvin(degrees):
    """Converting Fahrenheit to Kelvin."

    Args:
        degrees (mixed): Arg to be converted.

    Returns:
        decimal: Argument in Kelvin.

    Examples:

        >>>fahrenheit_to_kelvin(212)
        Decimal('373.15')

        >>>fahrenheit_to_kelvin(75)
        Decimal('297.0388888888888888888888889')

        >>>fahrenheit_to_kelvin(-5)
        Decimal('252.5944444444444444444444444')
    """

    return celsius_to_kelvin(fahrenheit_to_celsius(degrees))
