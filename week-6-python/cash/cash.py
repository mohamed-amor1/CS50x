# pset/week 6/cash
from cs50 import get_float

while True:
    cash = float(input(("Change owed: ")))
    if cash > 0:
        break

cash = round (cash*100)
n=0

while cash >= 25:
    n = n+1
    cash = cash - 25

while cash >= 10 and cash < 25:
    n = n+1
    cash = cash - 10

while cash >= 5 and cash < 10:
    n = n+1
    cash = cash - 5

while cash >= 1 and cash < 5:
    n = n+1
    cash = cash - 0.01

print(cash)
print(f"Number of coins is {n}")