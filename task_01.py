#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring"""


ABSOLUTE_DIFFERENCE = 273.15

def fahrenheit_to_celsius(degrees):
    """Does some math and returns a string.

    Args:
        degrees (int): Arg to be artithmetically configure with a formula

    Returns:
        int: All arguments reduced by 32 then multiplied by 5 and divided by 9

    Examples:

        >>> fahrenheit_to_celsius(212)
        '100.000'
    """

    '{:.3f}'.format(degrees)
    celsius = (degrees - 32) * 5 / 9
    return '{:.3f}'.format(celsius)


def celsius_to_kelvin(degrees):
    """Does some math and returns a string.

    Args:
        degrees (int): Arg to be arithmetically incremented

    Returns:
        int: All arguments increased by variable

    Examples:

        >>> celsius_to_kelvin(100)
        '373.15'
    """
    
    kelvin = ABSOLUTE_DIFFERENCE + degrees
    return kelvin


def fahrenheit_to_kelvin(degrees):
    """Does some math and returns a string.

    Args:
        degrees (int): Arg to be arithmetically configured

    Returns:
        int: All arguments modified by two defs

    Examples:

        >>> fahrenheit_to_kelvin(212)
        '373.15'
    """
    ftokelvin =((degrees - 32) * 5 / 9)  + ABSOLUTE_DIFFERENCE
    return ftokelvin
