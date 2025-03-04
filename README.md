# Generalized Kelly Criterion Calculator

This program calculates the optimal wager fraction using a generalized version of the Kelly Criterion, which incorporates a risk aversion parameter ($$\gamma$$) via a CRRA utility function. It also computes several bet statistics, including the winnings multiplier, bookmaker's implied probability (converted from various odds formats), expected profit, expected final wealth, variance of wealth, and expected utility.

The purpose of this tool is to help bettors or investors determine the optimal fraction of wealth to wager on a bet given their own probability of winning, a bookmaker’s odds (in American, Decimal, Fractional, or directly as implied probability), and their risk aversion level. Unlike the standard Kelly Criterion, this generalized approach accounts for risk preferences by substituting the logarithmic utility function with the CRRA utility function.

## Derivation

Starting with the objective of maximizing expected utility:

$$
\underset{f}{\text{max}}\ \mathbf{E}[u(W_{\text{final}})] = \underset{f}{\text{max}}\left[p \cdot u(W \cdot (1 + fb)) + (1 - p) \cdot u(W \cdot (1 - f))\right]
$$

Assuming an initial wealth $$W = 1$$ (since the fraction $$f^*$$ is scale-invariant), and substituting the CRRA utility function, we have:

$$
\underset{f}{\text{max}}\ \mathbf{E}[u(W_{\text{final}})] = \underset{f}{\text{max}}\left[p \cdot \frac{(1 + fb)^{1 - \gamma} - 1}{1 - \gamma} + (1 - p) \cdot \frac{(1 - f)^{1 - \gamma} - 1}{1 - \gamma}\right]
$$

Taking the first-order condition with respect to $$f$$ and setting it to zero yields:

$$
p b \cdot (1 + f b)^{-\gamma} - (1 - p) (1 - f)^{-\gamma} = 0
$$

This condition can be rearranged and solved for $$f$$ to yield the generalized Kelly fraction:

$$
f^* = \frac{\left( \frac{p b}{1 - p} \right)^{\frac{1}{\gamma}} - 1}{b + \left( \frac{p b}{1 - p} \right)^{\frac{1}{\gamma}}}
$$

Notably, when $$\gamma = 1$$, the CRRA function becomes the natural logarithm, and the formula simplifies directly to the standard Kelly Criterion.

## Odds Conversion

The program accepts input in one of four formats:

1. **American Odds:**  
   - For positive odds (e.g., +150):  
     $$\text{Probability} = \frac{100}{\text{Odds} + 100}$$  
   - For negative odds (e.g., -200):  
     $$\text{Probability} = \frac{-\text{Odds}}{-\text{Odds} + 100}$$

2. **Decimal Odds:**  
   $$\text{Probability} = \frac{1}{\text{Decimal Odds}}$$

3. **Fractional Odds:**  
   For odds expressed as $$\frac{A}{B}$$:  
   $$\text{Probability} = \frac{B}{A + B}$$

4. **Implied Probability:**  
   Enter directly as a probability between 0 and 1.

Once the implied probability is determined, the winnings multiplier $$b$$ is computed as:

$$
b = \frac{1}{\text{implied probability}} - 1
$$

## Usage

1. **Input Data:**  
   - Your assessed probability of winning.
   - Your risk aversion parameter ($$\gamma$$).
   - The odds type (American, Decimal, Fractional, or Implied Probability) along with the corresponding odds value.

2. **Output:**  
   The program outputs the optimal Kelly fraction along with the winnings multiplier $$b$$, the bookmaker’s implied probability, expected profit, expected final wealth, variance of wealth, and expected utility.

This tool is a practical resource for evaluating bets and determining optimal bet sizing under varying risk preferences.
