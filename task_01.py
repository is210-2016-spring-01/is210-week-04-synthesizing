#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring"""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """Does some math and returns a string.

    Args:
        degrees (int): Arg to be artithmetically configure with a formula

    Returns:
        int: All arguments reduced by 32 then multiplied by 5 and divided by 9

    Examples:

        >>> fahrenheit_to_celsius(212)
        'Decimal('100')'
    """
    return decimal.Decimal('{}'.format((decimal.Decimal('{}'.format(degrees))
                                        -32) * 5/9))


def celsius_to_kelvin(degrees):
    """Does some math and returns a string.

    Args:
        degrees (int): Arg to be arithmetically incremented

    Returns:
        int: All arguments increased by variable

    Examples:

        >>> celsius_to_kelvin(100)
        'Decimal('373.15')'
    """
    return decimal.Decimal('{}'.format(degrees+ABSOLUTE_DIFFERENCE))


def fahrenheit_to_kelvin(degrees):
    """Does some math and returns a string.

    Args:
        degrees (int): Arg to be arithmetically configured

    Returns:
        int: All arguments modified by two defs

    Examples:

        >>> fahrenheit_to_kelvin(212)
        'Decimal('373.15')'
    """
    return celsius_to_kelvin(fahrenheit_to_celsius(degrees))
