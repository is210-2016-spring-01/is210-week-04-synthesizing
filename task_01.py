#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Converts Fahrenheit to Celcius"""


import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """ This function converts fahrenheit to celsius (task_01)

    Args:
        degrees(int): Temperature in degrees Fahrenheit.

    Returns:
        decimal: Degrees Celcius represented

    Example:

       >>>fahrenheit_to_celsius(32)
       Decimal ('0.0')
    """
    return (5*(decimal.Decimal(degrees)-32))/9


def celsius_to_kelvin(degrees):
    """This function converts celsius to kelvin (task_02)

    Args:
        degrees(int): Temperature in degrees Celsius

    Returns:
        decimal: Degrees Kelvin

    Example:

        >>>celsius_to_kelvin (0)
        Decimal ('273.15')

    """
    return decimal.Decimal(degrees) + ABSOLUTE_DIFFERENCE


def fahrenheit_to_kelvin(degrees):
    """This function converts fahrenheit to kelvin (task_03)

    Args:
        degrees(int): Input degrees in fahrenheit

    Returns:
        decimal: degrees in kelvin.

    Examples:

        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')
    """
    return celsius_to_kelvin(fahrenheit_to_celsius(degrees))
