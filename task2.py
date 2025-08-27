import re
import decimal
from decimal import Decimal
from typing import Callable

def generator_numbers(text: str):
    numbers = re.findall(r"\ \d+\.\d+\ ", text)
    for number in numbers:
        yield Decimal(number)

def sum_profit(text: str, func: Callable):
    sum_profit = Decimal("0.00")
    for number in func(text):
        sum_profit += number
    return sum_profit

text = "The employee's total income consists of several parts: 1000.01 as the main income, supplemented by additional income of 27.45 and 324.00 dollars."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")

# additional testing
other = "20.12 or 12.28 . 333.1  and 2.9  or 0.2 and 2 or4.4 end 5.5."
other_total = sum_profit(other, generator_numbers)
print(f"other: {other_total}")
