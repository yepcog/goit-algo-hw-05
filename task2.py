import re
import decimal
from decimal import Decimal
from typing import Callable

def generator_numbers(text: str):
    words = text.split()
    for word in words:
        if re.search(r"\d+\.?\,?\d+", word):
            word = Decimal(word)
            yield word
        else:
            pass

def sum_profit(text: str, func: Callable):
    sum_profit = Decimal("0.00")
    for number in func(text):
        sum_profit += number
    return sum_profit

text = "The employee's total income consists of several parts: 1000.01 as the main income, supplemented by additional income of 27.45 and 324.00 dollars."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")
