#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Converts F to C"""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def farenheit_to_celsius(degrees):
    """Converts Farenheit to Celsius and returns a decimal.

        Args:
            degrees(int): Arg to be converted into Celsius.

        Returns:
            decimal: Argument converted into Celsius.

        Examples:

            >>> farenheit_to_celsius(212)
            Decimal('100')
     """
    degrees = decimal.Decimal(((degrees) - 32) * 5)/9
    return degrees


def celsius_to_kelvin(degrees):
    """Converts Celcius to Kelvin and returns a decimal.

        Args:
            degrees(int): Arg to be converted into Kelvin.

        Returns:
            decimal: Argument converted into Kelvin.

        Examples:

            >>> celcius_to_kelvin(100)
            Decimal('373.15')
     """
    degrees = ((degrees) + ABSOLUTE_DIFFERENCE)
    return degrees


def farenheit_to_kelvin(degrees):
    """Converts Farenheit to Kelvin and returns a decimal.

        Args:
            degrees(int): Arg to be converted into Kelvin.

        Returns:
            decimal: Argument converted into Kelvin.

        Examples:

            >>> farenheit_to_kelvin(212)
            Decimal('373.15')
     """
    degrees = farenheit_to_celsius(degrees)
    degrees = celsius_to_kelvin(degrees)
    return degrees
