#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Converts F to C"""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')

def farenheit_to_celcius(degrees):
    degrees = decimal.Decimal(((degrees) - 32) * 5)/9
    return degrees

def celcius_to_kelvin(degrees):
    degrees = ((degrees) + ABSOLUTE_DIFFERENCE)
    return degrees

def farenheit_to_kelvin(degrees):
    degrees = farenheit_to_celcius(degrees)
    degrees = celcius_to_kelvin(degrees)
    return degrees
