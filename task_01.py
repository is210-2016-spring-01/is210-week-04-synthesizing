#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function to convert Fahrenheit temperature to Celcius."""


import decimal

import task_02
def fahrenheit_to_celcius(degrees):
    """Converts temperature from fahrenheit to celcius.

    Args:
        degrees (int): Argument to be converted.

    Returns:
        decimal: conversion result returned as decimal.

    Examples:

        >>> fahrenheit_to_celcius(212)
        Decimal('100')
        
    """
    return (decimal.Decimal(degrees - 32) * 5) / 9

def fahrenheit_to_kelvin(degrees):
    """Converts temperatures from fahrenheit to kelvin.

    Args:
        degrees (int): Argument to be converted.

    Returns:
        decimal: conversion result returned as decimal.

    Examples:

        >>> fahrenheit_to_kelvin(212)
        Decimal(373.15')
        
    """
    CONVERT2 = decimal.Decimal((((degrees - 32) * 5) / 9) + task_02.ABSOLUTE_DIFFERENCE)
    return round(CONVERT2, 2)
