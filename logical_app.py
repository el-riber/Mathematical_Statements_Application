def conjunction(a, b):
    return a and b

def disjunction(a, b):
    return a or b

def negation(a):
    return not a

def implication(a, b):
    return (not a) or b

def biconditional(a, b):
    return a == b

def boolean_input(prompt):
    while True:
        value = input(prompt + " (1 for True, 0 for False): ").strip()
        if value in ["1", "0"]:
            return bool(int(value))
        else:
            print("Invalid input. Please enter 1 or 0.")

def display_results(a, b):
    print("\n--- Logical Operation Results ---")
    print(f"A AND B = {conjunction(a, b)}")
    print(f"A OR B = {disjunction(a, b)}")
    print(f"NOT A = {negation(a)}")
    print(f"NOT B = {negation(b)}")
    print(f"A → B (Implication) = {implication(a, b)}")
    print(f"A ↔ B (Biconditional) = {biconditional(a, b)}")

def generate_truth_table():
    print("\n--- Truth Table ---")
    print(" A | B | AND | OR  | NOT A | NOT B | A → B | A ↔ B")
    print("---|---|-----|-----|--------|--------|-------|-------")
    for a in [False, True]:
        for b in [False, True]:
            print(f" {int(a)} | {int(b)} |  {int(conjunction(a, b))}  |  {int(disjunction(a, b))}  |   {int(negation(a))}   |   {int(negation(b))}   |   {int(implication(a, b))}   |   {int(biconditional(a, b))}")

def main():
    print("Welcome to the Logical Statement Evaluator!")
    a = boolean_input("Enter value for A")
    b = boolean_input("Enter value for B")
    display_results(a, b)
    generate_truth_table()

if __name__ == "__main__":
    main()
