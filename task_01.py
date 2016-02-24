#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function to perform Fahrenheit to Celsius
conversion."""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """This function returns the Celsius equivalent of the given Fahrenheit
       degrees.

    Args:
        dgrees (mixed): the degrees in Fahrenheit.

    Returns:
        decimal: resultant dgrees in Celsius.

    Examples:

        >>> fahrenheit_to_celsius(212)
        Decimal('100')

        >>> fahrenheit_to_celsius(32)
        Decimal('0')

        >>> fahrenheit_to_celsius(-40)
        Decimal('-40')
    """

    return (decimal.Decimal(degrees) - 32) * 5 / 9


def celsius_to_kelvin(degrees):
    """This function returns the Kelvin equivalent of the given degrees
       Celsius.

    Args:
        degrees (mixed): the degrees in Celsius.

    Returns:
        decimal: resultant dgrees in Kelvin.

    Examples:

        >>>celsius_to_kelvin(0)
        Decimal('273.15')

        >>>celsius_to_kelvin(100)
        Decimal('373.15')

        >>>celsius_to_kelvin(-273.15)
        Decimal('0')
    """

    return decimal.Decimal(degrees) + ABSOLUTE_DIFFERENCE


def fahrenheit_to_kelvin(degrees):
    """This function returns the Kelvin equivalent of the given Fahrenheit
       degrees.

    Args:
        dgrees (mixed): the degrees in Fahrenheit.

    Returns:
        decimal: resultant dgrees in Kelvin.

    Examples:

        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')

        >>> fahrenheit_to_kelvin(32)
        Decimal('273.15')

        >>> fahrenheit_to_kelvin(-40)
        Decimal('233.15')

        >>> fahrenheit_to_kelvin(-459.67)
        Decimal('0')
    """

    return celsius_to_kelvin(fahrenheit_to_celsius(degrees))
