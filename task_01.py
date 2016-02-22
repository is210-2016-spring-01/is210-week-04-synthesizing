#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Converts F to C"""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def farenheit_to_celcius(degrees):
    """Converts Farenheit to Celcius and returns a decimal.

        Args:
            degrees(int): Arg to be converted into Celcius.

        Returns:
            decimal: Argument converted into Celcius.

        Examples:

            >>> farenheit_to_celcius(212)
            Decimal('100')
     """
    degrees = decimal.Decimal(((degrees) - 32) * 5)/9
    return degrees


def celcius_to_kelvin(degrees):
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
    degrees = farenheit_to_celcius(degrees)
    degrees = celcius_to_kelvin(degrees)
    return degrees
