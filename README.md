# Monte Carlo Simulation: The Impact of Inflation on Savings

This repository provides a Monte Carlo simulation model that estimates the real value of savings over time, accounting for inflation. The project analyzes how inflation erodes purchasing power and offers a probabilistic approach to quantify this effect.

## Features
- Simulates the impact of inflation on savings over a 5-year horizon.
- Utilizes historical inflation data (2000-2023) for realistic modeling.
- Includes visualization tools for result analysis (distribution plots and historical inflation trends).
- Provides an easily adjustable codebase for custom scenarios.

## Mathematics Behind the Project
This project uses well-established mathematical concepts to simulate inflation's impact:

1. **Real Value of Savings**:
The real value of savings after $t$ years is calculated as:
```math
P_t=P_0\cdot\prod^t_{n=1}\frac{1}{1+i_n}
```
Where:
- $P_0$: Initial savings amount.
- $i_n$: Inflation rate for year $n$.
- $t$: Number of years.

2. **Inflation Rate Simulation**:
Inflation rates are modeled using a normal (Gaussian) distribution:
```math
\text{simulare\_inflatie} = max(0,N(\mu,\sigma))
```
Where:
- $\mu$: Historical mean of inflation rates.
- $\sigma$: Historical standard deviation of inflation rates.

To avoid unrealistic values (e.g., extreme negative inflation), the simulation ensures values are truncated at a logical lower bound (e.g., no large negative values).

3. **Convergence of Estimates**:
According to the Central Limit Theorem, the mean of the simulated values converges to the expected real value as the number of simulations increases. The margin of error is calculated as:
```math
\text{Error =}\alpha\frac{\sigma}{\sqrt{N}}
```
Where:
- $N$: Number of simulations

This mathematical foundation ensures that the model produces robust, statistically valid results while allowing flexibility for customization.

## Methodology
1. **Historical Data**: Uses inflation rates from 2000-2023 to calculate mean and standard deviation.
2. **Monte Carlo Simulations**:
   - Generates 100,000 simulations based on a normal distribution of inflation rates.
   - Adjusts savings value iteratively for 5 years using simulated inflation rates.
3. **Result Analysis**:
   - Calculates the mean, standard deviation, and confidence intervals of the real savings value.
   - Visualizes results with histograms and historical inflation trends.

## Results
On average, a 100-unit saving today has an estimated real value of 67.32 units after 5 years.

## Installation
Clone the repository and install the required Python libraries:

```bash
git clone https://github.com/Bogdanctx/inflation-monte-carlo.git
cd inflation-monte-carlo
pip install numpy matplotlib
```

## Usage
1. **Adjust Parameters**:
   Modify `suma_economisita`, `peste_ani`, and `numar_simulari` in the script to fit your scenario.
2. **Run the Simulation**:
   ```bash
   python inflation_simulation.py
   ```
3. **Interpret Results**:
   - Check the output mean, standard deviation, and visualizations in the generated plots.
   - Analyze how inflation impacts savings in different scenarios.

## Limitations
- Assumes a normal distribution of inflation rates, which simplifies real-world behavior.
- Ignores external economic factors, such as recessions or policy changes.
- Does not account for interest rates or investment returns on savings.

## Potential Extensions
- Add annual savings yields (e.g., interest rates).
- Incorporate more complex inflation models (e.g., log-normal distributions).
- Simulate scenarios like hyperinflation or economic recessions.

## References
- Class courses and laboratories held by professor Mihai Bucătaru at the University of Bucharest
- [Numpy Documentation: Random Normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html)
- Probability and Statistics for Computer Scientists, page 90.
