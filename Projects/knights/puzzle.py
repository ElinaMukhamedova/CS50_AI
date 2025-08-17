from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
statement0 = Symbol("A is both a Knight and a Knave")

knowledge0 = And()

knowledge0.add(
    And(
        Implication(AKnight, statement0),
        Implication(AKnave, Not(statement0))
    )
)
knowledge0.add(
    Or(AKnight, AKnave)
)
knowledge0.add(
    And(
        Implication(AKnight, Not(AKnave)),
        Implication(AKnave, Not(AKnight))
    )
)
knowledge0.add(
    Implication(statement0, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
statement1_A = And(AKnave, BKnave)

knowledge1 = And()

knowledge1.add(
    And(
        Implication(AKnight, statement1_A),
        Implication(AKnave, Not(statement1_A))
    )
)
knowledge1.add(
    And(
        Or(AKnight, AKnave),
        Or(BKnight, BKnave)
    )
)
knowledge1.add(
    And(
        Implication(AKnight, Not(AKnave)),
        Implication(AKnave, Not(AKnight)),
        Implication(BKnight, Not(BKnave)),
        Implication(BKnave, Not(BKnight))
    )
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
statement2_A = Or(
    And(AKnight, BKnight),
    And(AKnave, BKnave)
)
statement2_B = Or(
    And(AKnight, BKnave),
    And(AKnave, BKnight)
)

knowledge2 = And()

knowledge2.add(
    And(
        Implication(AKnight, statement2_A),
        Implication(AKnave, Not(statement2_A)),
        Implication(BKnight, statement2_B),
        Implication(BKnave, Not(statement2_B))
    )
)

knowledge2.add(
    And(
        Or(AKnight, AKnave),
        Or(BKnight, BKnave)
    )
)
knowledge2.add(
    And(
        Implication(AKnight, Not(AKnave)),
        Implication(AKnave, Not(AKnight)),
        Implication(BKnight, Not(BKnave)),
        Implication(BKnave, Not(BKnight))
    )
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
A_says_x = Symbol("A says 'I am a knight.'")
A_says_y = Symbol("A says 'I am a knave.'")

statement3_A_x = AKnight
statement3_A_y = AKnave

statement3_B_x = A_says_y
statement_3_B_y = CKnave
statement3_C = AKnight

knowledge3 = And()

knowledge3.add(
    And(
        Or(A_says_x, A_says_y),
        Implication(A_says_x, Not(A_says_y)),
        Implication(A_says_y, Not(A_says_x))
    )
)

knowledge3.add(
    And(
        Implication(And(A_says_x, AKnight), statement3_A_x),
        Implication(And(A_says_x, AKnave), Not(statement3_A_x)),
        Implication(And(A_says_y, AKnight), statement3_A_y),
        Implication(And(A_says_y, AKnave), Not(statement3_A_y))
    )
)

knowledge3.add(
    And(
        Implication(BKnight, And(statement3_B_x, statement_3_B_y)),
        Implication(BKnave, And(Not(statement3_B_x), Not(statement_3_B_y))),
        Implication(CKnight, statement3_C),
        Implication(CKnave, Not(statement3_C))
    )
)

knowledge3.add(
    And(
        Or(AKnight, AKnave),
        Or(BKnight, BKnave),
        Or(CKnight, CKnave)
    )
)
knowledge3.add(
    And(
        Implication(AKnight, Not(AKnave)),
        Implication(AKnave, Not(AKnight)),
        Implication(BKnight, Not(BKnave)),
        Implication(BKnave, Not(BKnight)),
        Implication(CKnight, Not(CKnave)),
        Implication(CKnave, Not(CKnight))
    )
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
