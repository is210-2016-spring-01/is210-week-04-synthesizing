#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function to convert Celsius temperature to Kelvin."""

import decimal
ABSOLUTE_DIFFERENCE = 273.15


def celcius_to_kelvin(degrees):
    """Converts Celcius temperature to kelvin and returns a decimal.

    Args:
        degrees (int): Agrument to be converted.

    Returns:
        decimal: the result of argument conversion.

    Examples:

        >>> celsius_to_kelvin(100)
        Decimal('375.15')
        
    """
    CONVERT = decimal.Decimal(degrees + ABSOLUTE_DIFFERENCE)
    return round(CONVERT, 2)
