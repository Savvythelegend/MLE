# How to write a functional code in python using all the concepts of python programming language.
import math
def problem():
    """ Writing great functions in Python
As a programmer, you will spend most of your time writing and using functions. Python offers many features to make your functions powerful and flexible. Let's explore some of these by solving a problem:

Radha is planning to buy a house that costs $1,260,000. She considering two options to finance her purchase:

Option 1: Make an immediate down payment of $300,000, and take loan 8-year loan with an interest rate of 10% (compounded monthly) for the remaining amount.
Option 2: Take a 10-year loan with an interest rate of 8% (compounded monthly) for the entire amount.
Both these loans have to be paid back in equal monthly installments (EMIs). Which loan has a lower EMI among the two?

Since we need to compare the EMIs for two loan options, defining a function to calculate the EMI for a loan would be a great idea. The inputs to the function would be cost of the house, the down payment, duration of the loan, rate of interest etc. We'll build this function step by step.

First, let's write a simple function that calculates the EMI on the entire cost of the house, assuming that the loan must be paid back in one year, and there is no interest or down payment."""


def emi_calculator(cost,duration, rate ,down_payment):
    """formula to calculate the emi:
    emi = (cost - down_payment) * (rate/1200) * (1 + rate/1200)**duration / ((1 + rate/1200)**duration - 1)
 """
    try:
        loan_amount = cost - down_payment
        emi = loan_amount * (rate/1200) * (1 + rate/1200)**duration / ((1 + rate/1200)**duration - 1)
        
    except ZeroDivisionError:
        print('The rate of interest cannot be zero')

    return f'The Monthly EMI is ${math.ceil(emi)}'

print(emi_calculator(1260000,10*12, 0.08/12, 300000))

print(help(emi_calculator))