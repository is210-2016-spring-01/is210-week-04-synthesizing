#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01"""


import decimal
ABSOLUTE_DIFFERENCE = decimal.Decimal(('{:.2f}'.format(273.15)))


def fahrenheit_to_celsius(degrees):
    """a function called ``fahrenheit_to_celsius()`` that has one parameter:

    1.  ``degrees``

    3.  Use the following formula to convert the degrees Fahrenheit
    to a *decimal* representation of degrees Celsius

    1. Deduct 32 from ``degrees``, then multiply by 5, then divide by 9"""
    celsius = int()
    celsius = decimal.Decimal(((degrees -32) * 5)/9)
    return decimal.Decimal(('{:.2f}'.format(celsius)))


def celsius_to_kelvin(degrees):
    """a second function called ``celsius_to_kelvin()`` that has one
    parameter:

    1.  ``degrees``
    4.  Use the following formula to convert the degrees
    Celsius to degrees Kelvin:

    1.  add ``ABSOLUTE_DIFFERENCE`` to degrees"""
    kelvin = decimal.Decimal(degrees + ABSOLUTE_DIFFERENCE)
    return decimal.Decimal(('{:.2f}'.format(kelvin)))


def fahrenheit_to_kelvin(degrees):
    """a third and final function ``fahrenheit_to_kelvin()`` that has one
    parameter:

    1.  ``degrees``
    3.  Use ``fahrenheit_to_celsius()`` and ``celsius_to_kelvin()`` to convert
    Fahrenheit temperatures to Kelvin and return the result as a number."""
    f_to_c = fahrenheit_to_celsius(degrees)
    f_to_k = (f_to_c + ABSOLUTE_DIFFERENCE)
    return decimal.Decimal(f_to_k)
