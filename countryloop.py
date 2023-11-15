#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:26:12 2023

@author: jasonhardjawidjaja
"""

countries = {}
with open("country_info.txt") as country_info:
    country_info.readline()
    for row in country_info:
        data = row.strip("\n").split("|")
        country, capital, code, code3, dialing, timezone, currency = data
        country_dict = {
            "name": country,
            "capital": capital,
            "country_code": code,
            "cc3": code3,
            "dialing_code": dialing,
            "timezone": timezone,
            "currency": currency,
        }
        
        print(country_dict)
        print("")
        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict

country_list = ["", "quit"]

for chosen_country in country_list:
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif chosen_country == "quit".casefold():
        break