#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Program to convert temperature in Fahrenheight to Celsius."""



ABSOLUTE_DIFFERENCE = 273.15
def farenheit_to_kelvin(degrees):


    def celsius_to_kelvin(degrees):
        Kelvin = float(ABSOLUTE_DIFFREENCE + degrees)
    return Kelvin


def farenheit_to_celsius(degrees):
    Farenheit = float(degrees - 32) * 5/9
    return Farenheit
    """ This program converts farenheit to celsius and vice-versa.

        Args:
            degrees = float(degrees)

        Returns:
            float: All arguments as a float

        Examples:
            >>> degrees = 100
            >>> print float(degrees - 32) * 5/9
            37.7777777778

            >>> degrees = 75
            >>>print float(degrees - 32) * 5/9
            23.8888888889

            >>> degrees = 95
            >>> ABSLOUTE_DIFFERENCE = 273.15
            >>> print float(ABSLOUTE_DIFFERENCE + degrees)
            368.15

            >>> degrees = 500
            >>> print float(degrees - 32) * 5/9
            260.0
            >>> degrees = 260.0
            >>> ABSLOUTE_DIFFERENCE = 273
            >>> print float(ABSLOUTE_DIFFERENCE + degrees)
            533.0
            >>> degrees = 1500
            >>> print float(degrees - 32) * 5/9
            815.555555556
            >>> degrees = 815.555555556
            >>> print float(ABSLOUTE_DIFFERENCE + degrees)
            1088.55555556
            """
    Kelvin = float(ABSOLUTE_DIFFREENCE + degrees)
    return Kelvin
    Farenheit = float(degrees - 32) * 5/9
    return Farenheit
