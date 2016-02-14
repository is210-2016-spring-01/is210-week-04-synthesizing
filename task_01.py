#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Functions to convert degrees (Fahrenheit, Celsius and Kelvin)."""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal(273.15)


def celsius_to_kelvin(degrees):
    """A function to change celsius to kelvin.

    Args:
        degrees (int): Degrees in celsius.

    Returns:
        decimal: Degrees in kelvin.

    Examples:
        >>> celsius_to_kelvin(70)
        Decimal('343.1499999999999772626324557')

        >>> celsius_to_kelvin(100)
        Decimal('373.1499999999999772626324557')
    """
    kelvin = ABSOLUTE_DIFFERENCE + degrees
    return kelvin


def fahrenheit_to_celsius(degrees):
    """A function to change fahrenheit to celsius.

    Args:
        degrees (int): Degrees in fahrenheit.

    Returns:
        decimal: Degrees in celsius.

    Examples:
        >>> fahrenheit_to_celsius(76)
        Decimal('24.44444444444444444444444444')

        >>> fahrenheit_to_celsius(80)
        Decimal('26.66666666666666666666666667')
    """
    celsius = (decimal.Decimal(degrees - 32) * 5) / 9
    return celsius


def fahrenheit_to_kelvin(degrees):
    """A function to change fahrenheit to kelvin.

    Args:
        degrees (int): Degrees in fahrenheit.

    Returns:
        decimal: Degrees in kelvin.

    Examples:
        >>> fahrenheit_to_kelvin(70)
        Decimal('294.2611111111110883737435668')

        >>> fahrenheit_to_kelvin(212)
        Decimal('373.1499999999999772626324557')
    """
    kelvin2 = celsius_to_kelvin(fahrenheit_to_celsius(degrees))
    return kelvin2
