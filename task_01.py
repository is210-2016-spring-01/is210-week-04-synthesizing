#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function to convert Fahrenheit temperature to Celcius."""


import decimal

import task_02

def fahrenheit_to_celcius(degrees):
    """Converts temperature from fahrenheit to celcius.

    Args:
        degrees (int): Argument to be arithmetically converted.

    Returns:
        decimal: conversion result returned as decimal.

    Examples:

        >>> def fahrenheit_to_celcius(212)
        Decimal('100')
        
    """
    return (decimal.Decimal(degrees - 32) * 5) / 9

def fahrenheit_to_kelvin(degrees):
    """

    """
    return decimal.Decimal(task_02.celcius_to_kelvin(fahrenheit_to_celcius))
    
    
