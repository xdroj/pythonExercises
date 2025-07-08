# Probability Calculator

A Python program that estimates the probability of drawing certain combinations of colored balls from a hat using Monte Carlo simulation.

## Overview

This project simulates drawing balls from a hat to estimate probabilities through repeated experiments. It's particularly useful for complex probability problems where mathematical calculation would be difficult.

## Features

- **Hat Class**: Creates a hat containing colored balls
- **Random Drawing**: Simulates drawing balls without replacement
- **Probability Estimation**: Uses Monte Carlo method to estimate probabilities

## Usage

### Creating a Hat

```python
hat = Hat(blue=5, red=4, green=2)
# Creates a hat with 5 blue, 4 red, and 2 green balls
```

### Drawing Balls

```python
drawn_balls = hat.draw(3)
# Draws 3 random balls from the hat
```

### Running Experiments

```python
probability = experiment(
    hat=Hat(black=6, red=4, green=3),
    expected_balls={'red': 2, 'green': 1},
    num_balls_drawn=5,
    num_experiments=2000
)
# Estimates probability of drawing at least 2 red and 1 green ball
```

## Example

```python
# What's the probability of drawing at least 1 red and 2 green balls 
# when drawing 4 balls from a hat with 5 blue, 4 red, and 2 green balls?

hat = Hat(blue=5, red=4, green=2)
probability = experiment(
    hat=hat,
    expected_balls={'red': 1, 'green': 2},
    num_balls_drawn=4,
    num_experiments=10000
)
print(f"Probability: {probability}")
```

## Implementation Details

- Uses `random` module for ball selection
- Uses `copy.deepcopy()` to preserve original hat state
- Returns all remaining balls if draw request exceeds available balls
- Probability calculated as successful_experiments / total_experiments

## How to Run

```bash
python main.py
```

This will run the example probability calculations and display the results.

## Requirements

- Python 3.x
- No external dependencies (uses built-in modules only)

## Testing

The implementation passes the following test criteria:
1. Hat object creation adds correct contents
2. Draw method reduces number of items in contents
3. Draw method handles requests exceeding available balls
4. Experiment method returns varying probabilities based on random draws