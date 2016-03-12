#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Docstring for fahrenheit temp to celsius"""


import decimal

decimal.getcontext().prec = 5

ABSOLUTE_DIFFERENCE = decimal.Decimal(273.15)


def fahrenheit_to_celsius(degrees):
    """ This will convert temperature from farenheit to celsius.

    Args:
        degrees(int): the temperature to be converted

    Returns(int):
        the new converted temperature

    Example:
        >>>farenheit_to_celsius(212)
        ('100')
    """
    total = (decimal.Decimal(degrees) - 32)*5/9
    return decimal.Decimal(total)

print fahrenheit_to_celsius(212)


def celsius_to_kelvin(degrees):
    """ This will convert temperature from celsius to kelvin.

    Args:
        degrees(int): the temperature to be converted

    Returns(int):
        the new converted temperature

    Example:
        >>>celsius_to_kelvin(100)
        ('373.15')
    """
    total = ABSOLUTE_DIFFERENCE + decimal.Decimal(degrees)

    return decimal.Decimal(total)

print celsius_to_kelvin(100)


def fahrenheit_to_kelvin(degrees=decimal.Decimal):
    """ This will convert temperature from fahrenheit to kelvin.

    Args:
        degrees(int): the temperature to be converted

    Returns(int):
        the new converted temperature

    Example:
        >>>fahrenheit_to_kelvin(212)
        ('373.15')
    """
    total = fahrenheit_to_celsius(degrees) + ABSOLUTE_DIFFERENCE
    return decimal.Decimal(total)

print fahrenheit_to_kelvin(212)
