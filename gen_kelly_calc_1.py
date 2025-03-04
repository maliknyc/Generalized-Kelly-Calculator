import math

def generalized_kelly(assessed_p, implied_p, gamma):
    b = (1 / implied_p) - 1
    factor = (assessed_p * b / (1 - assessed_p)) ** (1 / gamma)
    f_star = (factor - 1) / (b + factor)
    edge = assessed_p * b - (1 - assessed_p)
    expected_profit = f_star * edge
    wealth_win = 1 + f_star * b
    wealth_lose = 1 - f_star
    expected_wealth = assessed_p * wealth_win + (1 - assessed_p) * wealth_lose
    var_wealth = assessed_p * (wealth_win - expected_wealth)**2 + (1 - assessed_p) * (wealth_lose - expected_wealth)**2
    if gamma == 1:
        util_win = math.log(wealth_win)
        util_lose = math.log(wealth_lose)
    else:
        util_win = (wealth_win**(1 - gamma) - 1) / (1 - gamma)
        util_lose = (wealth_lose**(1 - gamma) - 1) / (1 - gamma)
    expected_utility = assessed_p * util_win + (1 - assessed_p) * util_lose
    return {
        'f_star': f_star,
        'b': b,
        'edge': edge,
        'expected_profit': expected_profit,
        'expected_wealth': expected_wealth,
        'wealth_variance': var_wealth,
        'expected_utility': expected_utility
    }

def main():
    try:
        assessed_p = float(input("Enter your assessed probability of winning (0 < p < 1): "))
        gamma = float(input("Enter risk aversion gamma (> 0): "))
        if not (0 < assessed_p < 1):
            print("Error: your assessed probability must be between 0 and 1.")
            return
        if gamma <= 0:
            print("Error: gamma must be greater than 0.")
            return
        print("Choose odds type:")
        print("1: American Odds")
        print("2: Decimal Odds")
        print("3: Fractional Odds")
        print("4: Implied Probability")
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            odds = float(input("Enter American odds (e.g., +150 or -200): "))
            if odds > 0:
                implied_p = 100 / (odds + 100)
            else:
                implied_p = -odds / (-odds + 100)
        elif choice == 2:
            decimal_odds = float(input("Enter Decimal odds (e.g., 2.50): "))
            implied_p = 1 / decimal_odds
        elif choice == 3:
            frac = input("Enter Fractional odds as A/B (e.g., 3/2): ")
            A, B = frac.split('/')
            A, B = float(A), float(B)
            implied_p = B / (A + B)
        elif choice == 4:
            implied_p = float(input("Enter the bookmaker's implied probability (0 < p < 1): "))
        else:
            print("Error: Invalid choice.")
            return
        if not (0 < implied_p < 1):
            print("Error: implied probability must be between 0 and 1.")
            return
        stats = generalized_kelly(assessed_p, implied_p, gamma)
        print()
        print(f"Optimal Kelly fraction (f*): {stats['f_star']:.4f}")
        print()
        print(f"Winnings multiplier (b): {stats['b']:.4f}")
        print(f"Bookmaker's implied probability: {implied_p:.4f}")
        print(f"Expected profit (fraction of wealth): {stats['expected_profit']:.4f}")
        print(f"Expected final wealth: {stats['expected_wealth']:.4f}")
        print(f"Variance of final wealth: {stats['wealth_variance']:.6f}")
        print(f"Expected utility: {stats['expected_utility']:.6f}")
        # print(f"Edge (p*b - (1-p)): {stats['edge']:.4f}")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()
