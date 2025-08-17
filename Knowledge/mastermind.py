from logic import *

colours = ["red", "blue", "green", "yellow"]
symbols = []

for i in range(4):
    for colour in colours:
        symbols.append(Symbol(f"{colour}{i}"))

knowledge = And()

# Each colour has a position
for colour in colours:
    knowledge.add(
        Or(
            Symbol(f"{colour}0"),
            Symbol(f"{colour}1"),
            Symbol(f"{colour}2"),
            Symbol(f"{colour}3")
        )
    )

# Only one position per colour
for colour in colours:
    for i in range(4):
        for j in range(4):
            if i != j:
                knowledge.add(
                    Implication(Symbol(f"{colour}{i}"), Not(Symbol(f"{colour}{j}")))
                )
            
# Only one colour per position
for i in range(4):
    for c1 in colours:
        for c2 in colours:
            if c1 != c2:
                knowledge.add(
                    Implication(Symbol(f"{c1}{i}"), Not(Symbol(f"{c2}{i}")))
                )

knowledge.add(
    Or(
        And(Symbol("red0"), Symbol("blue1"), Not(Symbol("green2")), Not(Symbol("yellow3"))),
        And(Symbol("red0"), Symbol("green2"), Not(Symbol("blue1")), Not(Symbol("yellow3"))),
        And(Symbol("red0"), Symbol("yellow3"), Not(Symbol("blue1")), Not(Symbol("green2"))),
        And(Symbol("blue1"), Symbol("green2"), Not(Symbol("red0")), Not(Symbol("yellow3"))),
        And(Symbol("blue1"), Symbol("yellow3"), Not(Symbol("red0")), Not(Symbol("green2"))),
        And(Symbol("green2"), Symbol("yellow3"), Not(Symbol("red0")), Not(Symbol("blue1")))
    )
)

knowledge.add(
    And(
        Not(Symbol("blue0")),
        Not(Symbol("red1")),
        Not(Symbol("green2")),
        Not(Symbol("yellow3"))
    )
)

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)