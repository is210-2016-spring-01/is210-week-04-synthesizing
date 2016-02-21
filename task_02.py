#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 2"""

import decimal
import task_01

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def celsius_to_kelvin(degrees):
    """Calculate degrees in kelvin.

    ARGS:
        degrees (decimal): degrees in celsius.

    RETURNS:
        decimal: degrees converted from celsius to kelvin.

    EXAMPLES:

        >>> celsius_to_kelvin(100)
        'Decimal('373.15')'

        >>> celsius_to_kelvin(520)
        'Decimal('793.15')'
    """
    kelvin = degrees + ABSOLUTE_DIFFERENCE
    return decimal.Decimal(kelvin)
