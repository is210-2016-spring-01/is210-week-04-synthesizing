#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module converts Fahrenheit temperature to Celsius."""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """A function to convert Fahrenheit to Celsius.

    Args:
        degrees (dec): Fahrenheit input to be converted to Celsius.

    Returns:
        dec: Arithmetically calculated Celsius temperature conversion.

    Examples:

        >>> fahrenheit_to_celsius(32)
        Decimal('0')

        >>> fahrenheit_to_celsius(100)
        Decimal('100')
    """   
    return decimal.Decimal((degrees - 32) * 5) / 9


def celsius_to_kelvin(degrees):
    """A function to convert Celsius to Kelvin.

    Args:
        degrees (dec): Celsius input to be converted to Kelvin.

    Returns:
        dec: Arithmetically converted Celsius temperature from Kelvin.

    Examples:

        >>> celsius_to_kelvin(100)
        Decimal('373.15')
    """    
    return decimal.Decimal(degrees) + ABSOLUTE_DIFFERENCE


def fahrenheit_to_kelvin(degrees):
    """A function to convert Fahrenheit temperature to Kelvin.

    Args:
        degrees (dec): Fahrenheit input to be converted to Kelvin.

    Returns:
        dec: Arithmetically converted Kelvin temperature from Fahrenheit.

    Examples:

        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')
    """    
    return celsius_to_kelvin(fahrenheit_to_celsius(degrees))
