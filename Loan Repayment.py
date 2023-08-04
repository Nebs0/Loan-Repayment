#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:48:15 2023

@author: nebiyousamuel
"""

def compute_monthly_repayment(PV, r, n):
    # Convert annual interest rate to monthly interest rate
    monthly_rate = r / (12 * 100)

    # Calculate the monthly repayment amount using the formula
    Pmt = monthly_rate * PV / (1 - (1 + monthly_rate) ** -n)

    return Pmt

# Given inputs
PV = 12000
r = 7.45
n = 48

# Calculate the monthly repayment amount
monthly_repayment_amount = compute_monthly_repayment(PV, r, n)

print(f"The monthly repayment amount is: ${monthly_repayment_amount:.2f}")
